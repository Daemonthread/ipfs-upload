import base62
import ipfsapi
import os

from flask import Flask, request, redirect, url_for, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from sqlite3 import IntegrityError
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    uploaded_objects = Upload.query.all()
    return render_template('index.html', uploaded=uploaded_objects)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['uploadedFile']

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        ipfs_api = ipfsapi.connect(app.config['IPFS_HOST'], app.config['IPFS_PORT'])
        result = ipfs_api.add(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        try:
            new_upload = Upload(result['Name'], result['Hash'])
            db.session.add(new_upload)
            db.session.commit()

            new_upload_object = Upload.query.filter_by(filename=filename).first()
            shortened = base62.encode(new_upload_object.id)
            new_upload_object.short_url = shortened
            db.session.commit()

            flash('Upload Complete', 'success')
        except:
            flash('That hash already exists, passing.', 'danger')
    return redirect(url_for('index'))

@app.route('/s/<short>')
def redirect_to_short(short):
    id = base62.decode(short)
    uploaded_object = Upload.query.filter_by(id=id).first()
    return redirect("{0}{1}".format(app.config['REDIRECT_BASE_URL'], uploaded_object.ipfs_hash), code=302)


class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120))
    ipfs_hash = db.Column(db.String(200), unique=True)
    short_url = db.Column(db.String(50), unique=True)

    def __init__(self, filename, ipfs_hash, short_url=None):
        self.filename = filename
        self.ipfs_hash = ipfs_hash
        self.short_url = short_url

    def __repr__(self):
        return '<Name %r>' % self.name

if '__main__' in __name__:

    if not app.config['DB_CREATED']:
        db.create_all()

    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG'],
        use_reloader=app.config['USE_RELOADER']
    )
