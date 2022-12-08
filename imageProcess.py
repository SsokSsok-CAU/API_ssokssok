import os
from flask import request
from flask_restx import Resource, Namespace
from jwtParse import ParseJwtPayLoad
from convertImg import machinRunning
from json import dumps
from datetime import date, datetime

from fbInitallize import pbstorage

ImageProcess = Namespace('ImageProcess')

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

def FileManage():
    file_list = os.listdir()
    png_list = []
    for file in file_list:
        if '.' in file:
            if file.split('.')[1] =='png':
                os.remove(file)     
    return 

@ImageProcess.route('/processing')
class ImageProcessing(Resource):
    def post(self):
        tok = request.headers['Authorization']
        user_email = ParseJwtPayLoad(tok)['email']
        filename = request.form.get("filename")
        all_files = sorted(pbstorage.list_files(),key=lambda x:x.updated,reverse=True)
        result = []
        for file in all_files:
            fn = file.name.split('/')
            if len(fn)>2 :
                if  fn[0]==user_email and fn[1] == "Image" and fn[2]==filename:
                    file.download_to_filename(filename)
        machinRunning(filename)
        pbstorage.child(user_email+'/convertImage/'+filename).put("convertImg"+filename)
        result_url = pbstorage.child(user_email+'/convertImage/'+filename).get_url(tok)
        FileManage()
        return result_url
    
@ImageProcess.route('/myfiles')
class ImageProcessing(Resource):
    def get(self):
        tok = request.headers['Authorization']
        user_email = ParseJwtPayLoad(tok)['email']
        my_files_url=[]
        all_files = sorted(pbstorage.list_files(),key=lambda x:x.updated,reverse=True)
        for file in all_files:
            filename = file.name.split('/')
            if len(filename)>2 :
                if filename[0]==user_email and not filename[2]=="":
                    my_files_url.append([filename[2],pbstorage.child(file.name).get_url(tok)])
        if len(my_files_url)==0:
            return {'ErrorMessage':"There is no Files for "+user_email},400
        return my_files_url,200


@ImageProcess.route('/myfiles/beforeConvert')
class ImageProcessing(Resource):
    def get(self):
        tok = request.headers['Authorization']
        user_email = ParseJwtPayLoad(tok)['email']
        my_files_url=[]
        all_files = sorted(pbstorage.list_files(),key=lambda x:x.updated,reverse=True)
        for file in all_files:
            filename = file.name.split('/')
            if len(filename)>2:
                if  filename[0]==user_email and filename[1]=='Image'and not filename[2]=="":
                    my_files_url.append([filename[2],pbstorage.child(file.name).get_url(tok)])
        if len(my_files_url)==0:
            return {'ErrorMessage':"There is no File before Convert for "+user_email},400
        return my_files_url,200

@ImageProcess.route('/myfiles/afterConvert')
class ImageProcessing(Resource):
    def get(self):
        tok = request.headers['Authorization']
        user_email = ParseJwtPayLoad(tok)['email']
        my_files_url=[]
        all_files = sorted(pbstorage.list_files(),key=lambda x:x.updated,reverse=True)
        for file in all_files:
            filename = file.name.split('/')
            if len(filename)>2 :
                if filename[0]==user_email and filename[1]=='convertImage' and not filename[2]=="":
                    my_files_url.append([filename[2],pbstorage.child(file.name).get_url(tok)])
        if len(my_files_url)==0:
            return {'ErrorMessage':"There is no Converted Files for "+user_email},400
        return my_files_url,200
    
    
@ImageProcess.route('/myfiles/Coloring')
class ImageProcessing(Resource):
    def get(self):
        tok = request.headers['Authorization']
        user_email = ParseJwtPayLoad(tok)['email']
        my_files_url=[]
        all_files = sorted(pbstorage.list_files(),key=lambda x:x.updated,reverse=True)
        for file in all_files:
            filename = file.name.split('/')
            if len(filename)>2:
                if filename[0]==user_email and filename[1]=='Coloring' and not filename[2]=="":
                    my_files_url.append([filename[2],pbstorage.child(file.name).get_url(tok)])
        if len(my_files_url)==0:
            return {'ErrorMessage':"There is no Coloring Files for "+user_email},400
        return my_files_url,200
        