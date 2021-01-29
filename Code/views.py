from flask import render_template,request
import os
from flask import redirect, url_for
from PIL import Image
from utils import pipeline_model,compare_faces
import face_recognition as fr
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'

#app.secret_key = "secret key"
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def base():
    return render_template('base.html')


def index():
    return render_template('index1.html')

def faceapp():
    return render_template('faceapp.html')

def getwidth(path):
    img = Image.open(path)
    size = img.size
    aspect = size[0]/size[1]
    w = 300*aspect
    return int(w)

def display_image(filename):
    return redirect(url_for('static/compare/', filename = filename, code = 301))

def gender():
    if request.method == 'POST':
        f = request.files['image']
        filename = f.filename
        path = os.path.join(UPLOAD_FOLDER,filename)
        f.save(path)
        w = getwidth(path)
        img = pipeline_model(path,filename= filename)
        return render_template('gender.html',fileupload = True, img_name = filename, w = w)

    return render_template('gender.html',fileupload = False, img_name= 'freeai.png', w = '300')

def compare():
    if request.method == 'POST':
        print('Post')
        print(type(request.files), request.files)
        print(request.files.getlist)
        print(request.files.getlist('file'))
        pathlist = []
        upload_files = request.files.getlist('file')
        for file in upload_files:
            print(file)
            pathlist.append(os.path.join(UPLOAD_FOLDER, file.filename))
            if file.filename != '':
                file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        

        # if 'files' not in request.files:
        #     flash('No file')
        #     return redirect(request.url)
        # files = request.files.getlist('files[]')
        # file_names = []
        # path_list = []
        # for file in files:
        #     if file and allowed_file(file.filename):
        #         filename = secure_filename(file.filename)
        #         file_names.append(filename)
        #         path = os.path.join(UPLOAD_FOLDER1,filename)
        #         path_list.append(path)
        #         file.save(path)
        response_string = compare_faces(pathlist[0], pathlist[1]) 
        return render_template('comparefaces.html', filenames = pathlist, response_string=response_string)
                 
    return render_template('comparefaces.html',fileupload = False, img_name= 'xyz.png', w = '300')
    