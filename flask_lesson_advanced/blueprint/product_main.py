from flask import Blueprint, render_template, request, Response
import os

from werkzeug.utils import secure_filename

from infractructure import DB
from models import Product_class

product = Blueprint('product', __name__, template_folder='template_product', static_folder='static_product')


@product.route('/product', methods=['GET'])
def products_fun():
    print("products_fun")
    arg_price = request.args.get("price")
    products_list = [{"name": rest.name, "id": rest.id, "price": rest.price,
              "img_name": rest.img_name, "description": rest.description} for rest in DB['products']]
    product_filter = [i for i in products_list if str(i["price"]) == str(arg_price)]
    if len(product_filter) > 0:
        return render_template('all_products.html', value=product_filter)
    return render_template('all_products.html', value=products_list)


@product.route('/product/<id>', methods=['GET'])
def product_id_fun(id):
    print("product_id_fun")
    products_list = [{"name": rest.name, "id": rest.id, "price": rest.price,
              "img_name": rest.img_name, "description": rest.description} for rest in DB['products']]
    for product_dict in products_list:
        if product_dict['id'] == id:
            return render_template('product.html',
                                   name=product_dict["name"],
                                   description=product_dict['description'],
                                   price=product_dict["price"],
                                   img_name=product_dict["img_name"])


@product.route('/product', methods=['POST'])
def products_create_fun():
    print("products_create_fun")
    data = request.form
    print(data)
    f = request.files['img_name']
    filename = secure_filename(f.filename)
    f.save(os.path.join('blueprint/static_product/', filename))
    DB['products'].append(Product_class(data["name"], data["description"],
                                         data["price"], filename))
    list_p = DB['products']
    print(str(list_p))
    print(filename)
    return Response("The product has been added", status=200)


@product.route('/add-product', methods=['GET'])
def add_product():
    return render_template('add_product.html')

# @product.route('/product', methods=['GET'])
# def product_fun():
#     return json.dumps(DB['products'])
#
# @product.route('/product', methods=['POST'])
# def product_create_fun():
#     DB['products'].append(request.json)
#     return request.json