from flask import Blueprint, render_template, request, session
import os
from werkzeug.utils import secure_filename
from infractructure import DB
from models import Product_class

product = Blueprint('product', __name__, template_folder='template_product',
                    static_folder='static_product')


@product.route('/product', methods=['GET'])
def products_fun():
    arg_price = request.args.get("price")
    products_list = [{"name": rest.name, "id": rest.id, "price": rest.price,
                      "img_name": rest.img_name,
                      "description": rest.description}
                     for rest in DB['products']]
    product_filter = [i for i in products_list if str(i["price"]) == str(arg_price)]
    sess = session.keys()
    message = False
    if len(products_list) == 0:
        message = "There are no products"
    if len(product_filter) > 0:
        return render_template('all_products.html', value=product_filter,
                               message=message, sess=sess)
    return render_template('all_products.html', value=products_list, message=message, sess=sess)


@product.route('/product/<id>', methods=['GET'])
def product_id_fun(id):
    products_list = [{"name": rest.name, "id": rest.id, "price": rest.price,
                      "img_name": rest.img_name,
                      "description": rest.description}
                     for rest in DB['products']]
    for product_dict in products_list:
        if product_dict['id'] == id:
            session[product_dict["name"]] = True
            return render_template('product.html',
                                   name=product_dict["name"],
                                   description=product_dict['description'],
                                   price=product_dict["price"],
                                   img_name=product_dict["img_name"])


@product.route('/product', methods=['POST'])
def products_create_fun():
    data = request.form
    f = request.files['img_name']
    filename = secure_filename(f.filename)
    f.save(os.path.join('blueprint/static_product/', filename))
    DB['products'].append(Product_class(data["name"], data["description"],
                                        data["price"], filename))
    return render_template("product-post.html")


@product.route('/add-product', methods=['GET'])
def add_product():
    return render_template('add_product.html')
