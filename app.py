from flask import Flask, render_template, request, flash
import pymongo
import tmdb_download
import gridfs

client = pymongo.MongoClient('localhost', 5000)
mydb=client["movie_poster"]
mycol=mydb["posters"]
sss=[]
url=""
app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/")
def index():
	flash("what's the movie name your looking for?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	sss=(request.form['name_input'])
	movie_n=(tmdb_download.final_download(sss))
	flash("WWooooWWW    " + str(sss) + ",Movie  is a great choice !")
	for x in mycol.find({"name": "hiba"}):
		url=(x["url"])
	print(movie_n)
	print(sss)
	######  gridfs part - storing the image in mongodb ########3
	# Create an object of GridFs for the above database.
	fs = gridfs.GridFS(mydb)

	# define an image object with the location.
	file = "poster_0.jpeg"

	# Open the image in read-only format.
	with open(file, 'rb') as f:
		contents = f.read()

	# Now store/put the image via GridFs object.
	fs.put(contents, filename=sss)
	gout = fs.get_last_version(sss)
	fout = open("lastimg.jpg", 'wb')
	fout.write(gout.read())
	fout.close()
	gout.close()
	return render_template("greetold.html",poster_name=movie_n)
##################################################################################################################################
############################################ tmd download content ##########



