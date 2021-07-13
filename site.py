from flask import Flask, render_template, redirect, url_for, send_file
from flask.templating import render_template_string


app = Flask(__name__)

@app.route("/placeholder/placeholder")
def download_file_avery():
	path = "/placeholder"
	return send_file(path, as_attachment=True)


@app.route("/placeholder")
def download_file_alex():
	path = "/placeholder"
	return send_file(path, as_attachment=True)


@app.route("/placeholder")
def download_file_regan():
	path = "/placeholder"
	return send_file(path, as_attachment=True)


@app.route("/placeholder/placeholder")
def download_file_makeznie():
	path = "/placeholder"
	return send_file(path, as_attachment=True)


@app.route("/placeholder/placeholder")
def download_file_lauren():
	path = "/placeholder"
	return send_file(path, as_attachment=True)

@app.route("/placeholder/placeholder")
def download_file_will():
	path = "placeholder"
	return send_file(path, as_attachment=True)


@app.route('/placeholder')
def downloads():
    return render_template("download.html")

@app.route("/")
def redir():
    return render_template("index.html")


@app.route("/alive")
def my_link():
    file = open('deadoralive.txt', 'w')
    file.write('alive')
    print('alive  and well')
    file.close()
    return render_template("alive.html")



# host='192.168.1.193', port = '80',
if __name__ == "__main__":
    app.run(host='192.168.1.193', port = '443')
