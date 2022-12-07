from flask_restx import Resource, Namespace


FbAuth = Namespace('FbAuth')

@FbAuth.route('/test')
class AuthTest(Resource):
    def get(self):
        return "OK",200