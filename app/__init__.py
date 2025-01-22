from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)

    from app.routes import routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app
