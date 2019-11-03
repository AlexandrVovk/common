from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())

@app.route('/clock')
def clock_page():
    return render_template("clock.html")


if __name__ == "__main__":
    app.run(debug=True)
