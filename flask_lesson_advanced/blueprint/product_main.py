from flask import Blueprint, jsonify, render_template, request, Response
import json

from infractructure import DB
from models import Product_class

product = Blueprint('product', __name__, template_folder='template_product')


@product.route('/product', methods=['GET'])
def products_fun():
    products_all = [{"product": rest.product, "id": rest.id, "price": rest.price,
              "img_name": rest.img_name, "desc": rest.desc} for rest in DB['products']]
    data = json.dumps(products_all)
    return Response(data, 200)

@product.route('/product', methods=['POST'])
def products_create_fun():
    data = request.json
    DB['products'].append(Product_class(data['product'], data['price'],
                                        data['img_name'], data['desc']))
    print(DB['products'])
    return Response(status=200)

# @product.route('/product', methods=['GET'])
# def product_fun():
#     return json.dumps(DB['products'])
#
# @product.route('/product', methods=['POST'])
# def product_create_fun():
#     DB['products'].append(request.json)
#     return request.json