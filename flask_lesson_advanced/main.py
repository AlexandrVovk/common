from flask import Flask, render_template, request
from blueprint.product_main import product
from blueprint.supermarket_main import supermarket
from infractructure import DB


def setup_db():
    DB['products'] = []
    DB['supermarkets'] = []

def create_app():
    setup_db()
    app = Flask(__name__, instance_relative_config=False)
    with app.app_context():
        app.register_blueprint(product)
        app.register_blueprint(supermarket)
        return app

app = create_app()


@app.route('/')
def index():
    print(request.args.get('product'))
    return request.args.get('product')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)