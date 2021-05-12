from flask import Flask, render_template, redirect, url_for
from flask.templating import render_template_string


app = Flask(__name__)


@app.route("/")
def redir():
    return render_template("index.html")


@app.route("/my-link")
def my_link():
    file = open('deadoralive.txt', 'w')
    file.write('alive')
    return render_template("alive.html")



# host='192.168.1.193', port = '80',
if __name__ == "__main__":
    app.run(debug=True)
