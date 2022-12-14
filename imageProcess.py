import os
from flask import request
from flask_restx import Resource, Namespace
from jwtParse import ParseJwtPayLoad
from convertImg import machinRunning, PngToSvg, SvgToPng
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
            filemanager = file.split('.')
            if filemanager[len(filemanager)-1] =='png' or filemanager[len(filemanager)-1]=='svg':
                os.remove(file)     
    return 

@ImageProcess.route('/processing')
class ImageProcessing(Resource):
    def post(self):
        tok = request.headers['Authorization']
        user_email = ParseJwtPayLoad(tok)['email']
        filename = request.form.get("filename")
        all_files = pbstorage.list_files()
        for file in all_files:
            fn = file.name.split('/')
            if len(fn)>2 :
                if  fn[0]==user_email and fn[1] == "Image" and fn[2]==filename:
                    file.download_to_filename(filename)
        machinRunning(filename)
        pbstorage.child(user_email+'/convertImage/'+filename).put("convertImg"+filename)
        png_result_url = pbstorage.child(user_email+'/convertImage/'+filename).get_url(tok)
        svg_fliename = PngToSvg("convertImg"+filename)
        svg_fliename = svg_fliename[10:len(svg_fliename)]
        pbstorage.child(user_email+'/Coloring/'+svg_fliename).put(svg_fliename)
        svg_result_url = pbstorage.child(user_email+'/Coloring/'+svg_fliename).get_url(tok)
        FileManage()
        return {
            'png':png_result_url,
            'svg':svg_result_url
            }

@ImageProcess.route('/ColoringSubmit')
class ImageProcessing(Resource):
    def post(self):
        tok = request.headers['Authorization']
        user_email = ParseJwtPayLoad(tok)['email']
        filename = request.form.get("filename")
        all_files = pbstorage.list_files()
        for file in all_files:
            fn = file.name.split('/')
            if len(fn)>2 :
                if  fn[0]==user_email and fn[1] == "Coloring" and fn[2]==filename:
                    file.download_to_filename(filename)
        png_filename = SvgToPng(filename)
        pbstorage.child(user_email+'/Submit/'+png_filename).put(png_filename)
        png_result_url = pbstorage.child(user_email+'/Submit/'+png_filename).get_url(tok)
        FileManage()
        return png_result_url
                    
    
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
    
@ImageProcess.route('/getfile/beforeConvert')
class ImageProcessing(Resource):
    def get(self):
        tok = request.headers['Authorization']
        user_email = ParseJwtPayLoad(tok)['email']
        request_filename =  request.args.get('filename')
        my_files_url=[]
        all_files = pbstorage.list_files()
        for file in all_files:
            fn = file.name.split('/')
            if len(fn)>2:
                if  fn[0]==user_email and fn[1]=='Image'and fn[2]==request_filename:
                    my_files_url.append(pbstorage.child(file.name).get_url(tok))
        if len(my_files_url)==0:
            return {'ErrorMessage':"There is no File "+request_filename+" before Convert for "+user_email},400
        return my_files_url[0],200

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

@ImageProcess.route('/getfile/afterConvert')
class ImageProcessing(Resource):
    def get(self):
        tok = request.headers['Authorization']
        user_email = ParseJwtPayLoad(tok)['email']
        request_filename =  request.args.get('filename')
        my_files_url=[]
        all_files = pbstorage.list_files()
        for file in all_files:
            fn = file.name.split('/')
            if len(fn)>2:
                if  fn[0]==user_email and fn[1]=='convertImage'and fn[2]==request_filename:
                    my_files_url.append(pbstorage.child(file.name).get_url(tok))
        if len(my_files_url)==0:
            return {'ErrorMessage':"There is no File "+request_filename+" after Convert for "+user_email},400
        return my_files_url[0],200
    
    
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

@ImageProcess.route('/getfile/Coloring')
class ImageProcessing(Resource):
    def get(self):
        tok = request.headers['Authorization']
        user_email = ParseJwtPayLoad(tok)['email']
        request_filename =  request.args.get('filename')
        my_files_url=[]
        all_files = pbstorage.list_files()
        for file in all_files:
            fn = file.name.split('/')
            if len(fn)>2:
                if  fn[0]==user_email and fn[1]=='Coloring'and fn[2]==request_filename:
                    my_files_url.append(pbstorage.child(file.name).get_url(tok))
        if len(my_files_url)==0:
            return {'ErrorMessage':"There is no Coloring File "+request_filename+" for "+user_email},400
        return my_files_url[0],200

@ImageProcess.route('/myfiles/groupby')
class ImageProcessing(Resource):
    def get(self):
        tok = request.headers['Authorization']
        user_email = ParseJwtPayLoad(tok)['email']
        my_files_url=[]
        real_filename = ""
        all_files = sorted(pbstorage.list_files(),key=lambda x:x.updated,reverse=True)
        for file in all_files:
            filename = file.name.split('/')
            if len(filename)>2:
                if filename[0]==user_email and filename[1]=='Coloring' and not filename[2]=="":
                    filename = filename.split('.')[0]
                    real_filename = filename[10:len(filename)]
                    file_info = {"filename":real_filename,"svg":pbstorage.child(file.name).get_url(tok)}
                    my_files_url.append(file_info)
        for info in my_files_url:
            for file in all_files:
                fn = file.name.split('/')
                if len(fn)>2:
                    if fn[0]==user_email and fn[2].split('.')[0]==info.filename:
                        if fn[1]=='Image':
                            info['origin'] = pbstorage.child(file.name).get_url(tok)
                        elif fn[1]=='convertImg':
                            info['convert'] = pbstorage.child(file.name).get_url(tok)
        if len(my_files_url)==0:
            return {'ErrorMessage':"There is no Coloring Files for "+user_email},400
        return my_files_url,200
    
@ImageProcess.route('/getfile/Submit')
class ImageProcessing(Resource):
    def get(self):
        tok = request.headers['Authorization']
        user_email = ParseJwtPayLoad(tok)['email']
        request_filename =  request.args.get('filename')
        my_files_url=[]
        all_files = pbstorage.list_files()
        for file in all_files:
            fn = file.name.split('/')
            if len(fn)>2:
                if  fn[0]==user_email and fn[1]=='Submit'and fn[2]==request_filename:
                    my_files_url.append(pbstorage.child(file.name).get_url(tok))
        if len(my_files_url)==0:
            return {'ErrorMessage':"There is no Submitted File "+request_filename+" for "+user_email},400
        return my_files_url[0],200
    
@ImageProcess.route('/myfiles/groupby')
class ImageProcessing(Resource):
    def get(self):
        tok = request.headers['Authorization']
        user_email = ParseJwtPayLoad(tok)['email']
        my_files_url=[]
        real_filename = ""
        all_files = sorted(pbstorage.list_files(),key=lambda x:x.updated,reverse=True)
        for file in all_files:
            filename = file.name.split('/')
            if len(filename)>2:
                if filename[0]==user_email and filename[1]=='Coloring' and not filename[2]=="":
                    fn = filename[2].split('.')[0]
                    real_filename = fn[10:len(fn)]
                    file_info = {"filename":real_filename,"svg":pbstorage.child(file.name).get_url(tok)}
                    my_files_url.append(file_info)
        for info in my_files_url:
            for file in all_files:
                fn = file.name.split('/')
                if len(fn)>2:
                    if fn[0]==user_email and fn[2].split('.')[0]==info['filename']:
                        if fn[1]=='Image':
                            info['origin'] = pbstorage.child(file.name).get_url(tok)
                        elif fn[1]=='convertImage':
                            info['convert'] = pbstorage.child(file.name).get_url(tok)
        if len(my_files_url)==0:
            return {'ErrorMessage':"There is no Coloring Files for "+user_email},400
        return my_files_url,200

      