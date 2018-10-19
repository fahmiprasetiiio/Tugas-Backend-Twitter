from flask import Flask, jsonify, Blueprint, request
from flask_restful import Resource, Api, reqparse, inputs, abort
from datetime import datetime #untuk menambahkan tanggal dan waktu
import json

# dataUser = [{
#         "username": "John",
#         "email": "john@haha.com",
#         "password": "Hahaha123",
#         "fullname": "John Rukmana"
#     },
#     {
#         "username": "jeff",
#         "email": "jeff@haha.com",
#         "password": "Hahaha456",
#         "fullname": "Jeff Abidin"
#     }]

# Tweeters = [{
#         "email": "john@haha.com",
#         "tweet": "john_93"
#     },
#     {
#         "email": "jeff@haha.com",
#         "tweet": "jeff_abidin03"

#     }]


#####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~######
# # langkah 1 
# # ini buat update data ke file 
# with open('dataUser.json', 'w') as outfile:  
#     json.dump(dataUser, outfile)
#     outfile.close()

# with open('Tweeters.json', 'w') as outfile:  
#     json.dump(Tweeters, outfile)
#     outfile.close()  

# #jika sudah ganti dump to load

######~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~######
#langkah 2
#berfungsi untuk memanggil data dari file yang sudah tersimpan 

dataUser = []
dataTweeters = []
with open('dataUser.json') as outfile:  
    dataUser = json.load(outfile)
    outfile.close()

with open('Tweeters.json') as outfile:  
    Tweeters = json.load(outfile)
    outfile.close()
    
#*note: restart proggram sebelum menjalankan 
#####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~###### 
#langkah 3
#berfungsi untuk mengupdate file jika ada perubahan 

def updateDataUser(dataUser):
    with open('datauser.json', 'w') as file:
        file.write(json.dumps(dataUser))
        file.close()

def updateDataTweeters(Tweeters):
    with open('Tweeters.json', 'w') as file:
        file.write(json.dumps(Tweeters))
        file.close()
    return

#####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~######
class data(Resource):
    def get(self):
        return dataUser

#####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~######

class logIn(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "email",
            help = "Email Tidak Tersedia",
            required = True,
            location = ["json"]
        )
        self.reqparse.add_argument(
            "password",
            help = " Password Salah ",
            required  = True,
            location = ["json"]
        )

    def post(self):
        self.reqparse.parse_args()
        req = request.json 
        for user in dataUser:
            if user['email'] == req['email'] and user['password'] == req['password']:
                return user, 200
        
        return abort (400, message = 'Email tidak tersedia dan password salah') 
            
#####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#####
       
def userNameandEmailhaveExist(username,email):
    for data in dataUser:
        if data["username"] == username or data["email"] == email:
            abort(400, message = "Data Sudah Tersedia")
    return username,email

class signUP(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "email",
            help = "masukan email",
            required = True,
            location = ["json"]
        )
        self.reqparse.add_argument(
            "username",
            help = "masukan username",
            required =True,
            location = ["json"]
        )
    def post(self):
        self.reqparse.parse_args()
        req = request.json
        userNameandEmailhaveExist(req["username"], req["email"])
        dataUser.append(req)
        updateDataUser(dataUser) #
        return req

#####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#######

def checkEmail(email):
    for user in dataUser:
        if user['email'] == email:
            return email

    return abort (400, message = 'Email tidak ditemukan')

######~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~########
#datetime 
def checkEmailinTweet(req):
    for alamat in Tweeters:
        if alamat['email'] == req['email']:
            alamat['tweet'] = req['tweet']
            alamat['date'] = req['date']
            
            return    
         
    req['tweet'] = [req['tweet']]
    req['date'] = [req['date']]
    Tweeters.append(req)
    return

#####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#######
###
def checkEmailandTweet(email,tweet):
    index = 0
    for data in Tweeters:
        if data ['email'] == email and data['tweet'] == tweet:
            return index
        index += 1
    
    abort (400, message="cannot delete")
        
class tweet(Resource):
    
    def get(self):
        return Tweeters
 
    def post(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "email",
            help = "masukan Email",
            required = True,
            location = ["json"]
        )
        self.reqparse.add_argument(
            "tweet",
            help = "masukan tweet",
            required = True,
            location = ["json"]
        )
        self.reqparse.parse_args()
        req = request.json
        date = datetime.now() #date
        req['date'] = str(date) #
        checkEmail(req['email'])
        
        checkEmailinTweet(req)#
       
        updateDataTweeters(Tweeters)#
        return req
        
     
    def put(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "email",
            help = "masukan Email",
            required = True,
            location = ["json"]
        )
        self.reqparse.add_argument(
           "tweet",
           help = "masukan tweet",
           required = True,
           location = ["json"]
        )
        self.reqparse.add_argument(
            "tweetBaru",
            help = "masukan tweet baru",
            required = True,
            location = ["json"]
        )

        
        self.reqparse.parse_args()
        req = request.json

        for dataT in Tweeters:
            if dataT["email"] == req["email"] and dataT["tweet"] == req["tweet"]:
                dataT["tweet"] = req["tweetBaru"]
                updateDataTweeters(Tweeters)
                return dataT
        return "Gagal", 400
        
        # index = 0
        # for data in dataUser:
        #     if data["email"] == req["email"]:
        #         Tweeters[index]['tweet'] = req["tweetbaru"]
        #         return Tweeters[index]
        #     index += 1

    def delete(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            "email",
            help = "masukan email",
            required = True,
            location = {"json"}
        )
        self.reqparse.add_argument(
            "tweet",
            help = " masukan tweet",
            required = True,
            location = {"json"}

        )
        self.reqparse.parse_args()
        req = request.json
        index=checkEmailandTweet(req['email'],req['tweet'])
        Tweeters.pop(index)
        updateDataTweeters(Tweeters) 

        return {"message" : "has been deleted"}, 200

      

####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##### 


dataUsers_api = Blueprint('resources/dataUsers', __name__)

api = Api(dataUsers_api)

api.add_resource(data, 'dataUser')
# api.add_resource(dataTweet, 'Tweeters')
api.add_resource(logIn, "login")
api.add_resource(signUP, 'signup')
api.add_resource(tweet, 'tweet')

