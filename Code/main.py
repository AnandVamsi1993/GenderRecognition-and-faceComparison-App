from flask import *
import views
import json
import scipy.misc
import re
import warnings
import os
from werkzeug.utils import secure_filename



app = Flask(__name__)

app.add_url_rule('/base','Landing Page',views.base)
app.add_url_rule('/', 'Home Page', views.index)
app.add_url_rule('/faceapp','FaceApp',views.faceapp)
app.add_url_rule('/faceapp/gender','gender',views.gender,methods = ['GET','POST'])
app.add_url_rule('/face_match','face_match',views.compare,methods = ['GET','POST'])
app.add_url_rule('/face_match/<filename>','display_image', views.display_image)


if __name__=='__main__':
	app.run(debug = True)