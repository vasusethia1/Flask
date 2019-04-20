from flask import Flask,render_template
app = Flask(__name__)
UPLOAD_FOLDER="/tmp"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def index_page():
	return render_template('index.html')

@app.route('/upload')
def file_upload():
	return render_template('upload.html')


@app.route('/uploader', methods=['POST'])
def file():
	if request.method == 'POST':
		file = request.files['file']
      	filename = secure_filename(file.filename)
      	f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      	return render_template('uploaded.html')

if __name__=="__main__":
	app.run(debug=True)