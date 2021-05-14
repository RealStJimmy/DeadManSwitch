from flask import Flask, render_template, redirect, url_for, send_file
from flask.templating import render_template_string


app = Flask(__name__)

@app.route("/M2PMavToIbuJutmknngE/avery")
def download_file_avery():
	path = "avery.obt"
	return send_file(path, as_attachment=True)


@app.route("/M2PMavToIbuJutmknngE/alex")
def download_file_alex():
	path = "alex.obt"
	return send_file(path, as_attachment=True)


@app.route("/M2PMavToIbuJutmknngE/regan")
def download_file_regan():
	path = "regan.obt"
	return send_file(path, as_attachment=True)


@app.route("/M2PMavToIbuJutmknngE/makenzie")
def download_file_makeznie():
	path = "makenzie.obt"
	return send_file(path, as_attachment=True)


@app.route("/M2PMavToIbuJutmknngE/lauren")
def download_file_lauren():
	path = "lauren.obt"
	return send_file(path, as_attachment=True)

@app.route("/M2PMavToIbuJutmknngE/will")
def download_file_will():
	path = "will.obt"
	return send_file(path, as_attachment=True)


@app.route('/M2PMavToIbuJutmknngE')
def downloads():
    return render_template("download.html")

@app.route("/")
def redir():
    return render_template("index.html")


@app.route("/my-link")
def my_link():
    file = open('deadoralive.txt', 'w')
    file.write('alive')
    file.close()
    return render_template("alive.html")



# host='192.168.1.193', port = '80',
if __name__ == "__main__":
    app.run(debug=True)
