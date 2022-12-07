import os
from flask import Flask
from flask_restx import Api
from fbauth import FbAuth
from imageProcess import ImageProcess

app = Flask(__name__)
api = Api(app)

api.add_namespace(FbAuth,'/auth')
api.add_namespace(ImageProcess,'/image')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))