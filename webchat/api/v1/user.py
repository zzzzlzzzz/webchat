from flask_restful import Resource


class User(Resource):
    def get(self, username: str):
        """Get alive username

        :param username: Requesting user
        :return: [{'username': <username>}, ...]
        """
        return ''
