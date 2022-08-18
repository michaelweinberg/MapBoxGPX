import flask
from flask import request, url_for, render_template, redirect, send_from_directory


app = flask.Flask(__name__, static_url_path='',static_folder='static')

@app.route('/',methods=['GET','POST'])
def my_maps():

	mapbox_access_token = 'pk.eyJ1Ijoiam9obmhqb3JkYW4iLCJhIjoiY2tsOWg0ZTAxMm85MzMwdDc0d2kzY2xjMyJ9.iBomyJC6VGy3jeqgFaPKdw'

	return render_template('index.html',
		mapbox_access_token=mapbox_access_token)

if __name__ == '__main__':
	app.run(debug=True)

