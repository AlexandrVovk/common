from flask import Blueprint, render_template, request, session
import os
from werkzeug.utils import secure_filename
from infractructure import DB
from models import Supermarket_class

supermarket = Blueprint('supermarket', __name__,
                        template_folder='template_supermarket',
                        static_folder='static_supermarket')


@supermarket.route('/supermarket', methods=['GET'])
def supermarkets_fun():
    arg_location = request.args.get("location")
    supermarkets_list = [{"id": rest.id, "name": rest.name,
                          "location": rest.location,
                          "img_name": rest.img_name}
                         for rest in DB['supermarkets']]
    supermarket_filter = [i for i in supermarkets_list if str(i["location"]) == str(arg_location)]
    sess = session.keys()
    if len(supermarket_filter) > 0:
        return render_template('all_supermarkets.html', value=supermarket_filter, sess=sess)
    return render_template('all_supermarkets.html', value=supermarkets_list, sess=sess)


@supermarket.route('/supermarket/<id>', methods=['GET'])
def supermarket_id_fun(id):
    print("supermarket_id_fun")
    supermarkets_list = [{"id": rest.id,
                          "name": rest.name, "location": rest.location,
                          "img_name": rest.img_name}
                         for rest in DB['supermarkets']]
    for supermarket_dict in supermarkets_list:
        if supermarket_dict['id'] == id:
            session[supermarket_dict["name"]] = True
            return render_template('supermarket.html',
                                   name=supermarket_dict["name"],
                                   location=supermarket_dict["location"],
                                   img_name=supermarket_dict["img_name"])


@supermarket.route('/supermarket', methods=['POST'])
def supermarkets_create_fun():
    data = request.form
    f = request.files['img_name']
    filename = secure_filename(f.filename)
    f.save(os.path.join('blueprint/static_supermarket/', filename))
    DB['supermarkets'].append(Supermarket_class(data["name"],
                                                data["location"], filename))
    return render_template('supermarket-post.html')


@supermarket.route('/add-supermarket', methods=['GET'])
def add_supermarket():
    return render_template('add_supermarket.html')
