from flask_restful import Resource


class Post(Resource):
    def post(self, username: str):
        """Post new user post

        :param username: Requesting user
        :return: None
        """
        return '', 201

    def get(self, username: str):
        """Get user posts

        :param username: Requesting user
        :return: [{'time': <time>, 'username': <username>, 'message': <message>}, ...]
        """
        return ''
