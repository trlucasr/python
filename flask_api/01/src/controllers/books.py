from flask import Flask
from flask_restplus import Api, Resource

from src.server.instance import server

app, api = server.app, server.api

books_db = [
    {'id':0, 'title':'War1'},
    {'id':1, 'title':'War2'}

]

class BookList(Resource):
    def get(self, ):
        return books_db