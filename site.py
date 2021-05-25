from flask import Flask, render_template, redirect, url_for, send_file
from flask.templating import render_template_string


app = Flask(__name__)

@app.route("/M2PMavToIbuJutmknngE/avery")
def download_file_avery():
	path = "/home/stjimmy/DeadManSwitch/ReleaseDocs/avery.odt"
	return send_file(path, as_attachment=True)


@app.route("/M2PMavToIbuJutmknngE/alex")
def download_file_alex():
	path = "/home/stjimmy/DeadManSwitch/ReleaseDocs/alex.odt"
	return send_file(path, as_attachment=True)


@app.route("/M2PMavToIbuJutmknngE/regan")
def download_file_regan():
	path = "/home/stjimmy/DeadManSwitch/ReleaseDocs/regan.odt"
	return send_file(path, as_attachment=True)


@app.route("/M2PMavToIbuJutmknngE/makenzie")
def download_file_makeznie():
	path = "/home/stjimmy/DeadManSwitch/ReleaseDocs/makenzie.odt"
	return send_file(path, as_attachment=True)


@app.route("/M2PMavToIbuJutmknngE/lauren")
def download_file_lauren():
	path = "/home/stjimmy/DeadManSwitch/ReleaseDocs/lauren.odt"
	return send_file(path, as_attachment=True)

@app.route("/M2PMavToIbuJutmknngE/will")
def download_file_will():
	path = "/home/stjimmy/DeadManSwitch/ReleaseDocs/will.odt"
	return send_file(path, as_attachment=True)


@app.route('/M2PMavToIbuJutmknngE')
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
