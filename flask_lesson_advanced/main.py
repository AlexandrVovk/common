from flask import Flask, render_template, Response
from blueprint.product_main import product
from blueprint.supermarket_main import supermarket
from infractructure import DB
from config import Config

def setup_db():
    DB['products'] = []
    DB['supermarkets'] = []


def create_app():
    setup_db()
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    with app.app_context():
        app.register_blueprint(product)
        app.register_blueprint(supermarket)
        return app


app = create_app()


@app.route('/')
def index():
    return render_template('home.html')


@app.errorhandler(404)
def not_found(e):
    return Response("404 Page not found", status=404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)
