from flask import Blueprint, jsonify, render_template

supermarket = Blueprint('supermarket_list', __name__, template_folder='template_supermarket')

supermarket_list = [
    {
        "id":"00001",
        "name":"Novus",
        "location":"Kyiv",
        "img_name":"novus.jpg",
    }
]

@supermarket.route('/supermarket')
def product_fun():
    return render_template('all_supermarkets.html', supermarket_list=supermarket_list)

