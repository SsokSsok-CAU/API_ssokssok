from flask_restx import Resource, Namespace

ImageProcess = Namespace('ImageProcess')

@ImageProcess.route('/test')
class ImageTest(Resource):
    def get(self):
        return "OK",200