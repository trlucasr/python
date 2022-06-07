from flask import Flask
from flask_restplus import Api

#from src.server.instance import Server

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.api = Api(self.app, 
            version='1.0',
            title='Book Api',
            description='A Simple Book Api',
            doc='/docs'
        )

    def run(self, ):
        self.app.run(
            debug=True
        )

    
server = Server()