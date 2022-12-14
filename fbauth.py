import json
from flask import request
from flask_restx import Resource, Namespace
from firebase_admin import auth

from fbInitallize import pb

FbAuth = Namespace('FbAuth')


@FbAuth.route("/signup")
class SignUp(Resource):
    def post(self):
        email = request.form.get('email')
        password = request.form.get('password')
        displayName = request.form.get('displayName')
        if email =="" or password =="" :
            error=[]
            if email =="" :
                error.append("Username is Missing ")                
            if password =="":
                error.append("Password is Missing ")
            return error, 400
        else:
            try :
                user = auth.create_user(
                    email = email,
                    password = password,
                    display_name = displayName
                )
                return {'token':user['idToken'],'displayName':displayName}, 200
            except:
                return "Error occur in creating user",400

@FbAuth.route('/signin')
class SignIn(Resource):
    def post(self):
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = pb.auth().sign_in_with_email_and_password(email,password)
            jwt = user['idToken']
            info = pb.auth().get_account_info(jwt)
            displayName = info['users'][0]['displayName']
            return {'token':jwt,'displayName':displayName},200
        except:
            return {'message':'There was an error logging in'},400
        
