from werkzeug.utils import secure_filename
class Expose:
    def __init__(self, name):
        import os
        self.name = name
        
    def server(self):
        from flask import Flask, render_template, request, flash, redirect, url_for 
        from werkzeug.utils import secure_filename
        import os

        UPLOAD_FOLDER = '/path/to/the/uploads'
        ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

        app = Flask(__name__)
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

        def allowed_file(filename):
            return '.' in filename and \
                filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS