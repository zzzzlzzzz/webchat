from flask_restful import Resource


class User(Resource):
    def get(self):
        """Get alive username

        :return: [{'username': <username>}, ...]
        """
        return ''
