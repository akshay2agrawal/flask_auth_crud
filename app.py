from routes import *
from routes.main import main
from routes.auth import auth
from models import *

def create_app():
    app = Flask(__name__ , template_folder='templates')
     
    app.config.from_pyfile('config.cfg')
    Bootstrap(app)
    app.config.from_object(Config)
    
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(id)#in the documentation examples query is not written but is required 
    
    app.register_blueprint(main)
    app.register_blueprint(auth)
    return app

def db_init():
    app = create_app()
    db.init_app(app)
    app.test_request_context().push()
    db.create_all()

    db.session.commit()


if __name__ == '__main__':

    args  =  sys.argv
    
    if len(args) == 1: 
        print("Error: Plese provide one of positional arguments (run or db)")
        sys.exit()      
    elif args[1]== "run":
        app = create_app()
        
        # db_init()
        app.run(debug=True)
    elif args[1]=="db":
        db_init()


