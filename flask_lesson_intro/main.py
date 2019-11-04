from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route('/<item>')
def get_page(item):
    for i in get_data():
        if i['title'] == item:
            return render_template("page.html", title=i['title'],
                                   text=i['text'])


if __name__ == "__main__":
    app.run(debug=True)
