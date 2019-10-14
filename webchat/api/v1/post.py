from flask_restful import Resource


class Post(Resource):
    def post(self):
        """Post new user post

        :return: None
        """
        return '', 201

    def get(self):
        """Get user posts

        :return: [{'time': <time>, 'username': <username>, 'message': <message>}, ...]
        """
        return ''
