from flask import Flask,render_template,request
from werkzeug import secure_filename
import os


app = Flask(__name__)
UPLOAD_FOLDER="tmp"								#/at the begining will save it in /tmp (root of your Linux machine)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index_page():
	return render_template('index.html')

@app.route('/upload')
def file_upload():
	return render_template('upload.html')

@app.route('/uploader', methods=['POST'])
def files():											#cant have keyword as function
	if request.method == 'POST':
		fil = request.files['myfile']						#cant have keyword as variable
      	fil.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(fil.filename)))
      	return render_template('uploaded.html')


if __name__=="__main__":
	app.run(debug=True)