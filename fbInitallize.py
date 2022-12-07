import os
import json
import firebase_admin
import pyrebase

from flask import request
from flask_restx import Resource, Api, Namespace
from firebase_admin import credentials



cred = credentials.Certificate("fbAdminConfig.json")
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))
pbstorage = pb.storage()


