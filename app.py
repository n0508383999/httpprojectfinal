from flask import Flask, render_template, request, flash
import tmdb_download
sss=[]
app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/")
def index():
	flash("what's the movie name your looking for?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	sss=(request.form['name_input'])
	print (tmdb_download.final_download(sss))
	flash("Hi " + str(sss) + ", is a great choice !")
	#tmdb_download.tmdb_posters()
	#flash(imghdr(poster_0.jpeg))
	return render_template("greet.html")
##################################################################################################################################
############################################ tmd download content ##########



