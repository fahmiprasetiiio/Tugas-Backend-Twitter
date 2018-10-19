import os 
from flask import Flask, blueprints, request, abort
from resources.dataUsers import dataUsers_api

# #  import middleware


app = Flask(__name__)
app.register_blueprint(dataUsers_api, url_prefix = "/api/v1/")
# app.wsgi_app = middleware.SimpleMiddleware(app.wsgi_app)


@app.route('/')
def hello():
    return "Welcome Tugas 2"
        
if __name__ == '__main__':
    app.run(debug = True, host = os.getenv('HOST'), port = os.getenv('PORT'))