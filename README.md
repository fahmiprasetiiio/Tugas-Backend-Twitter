# ***Backend Twitter***

> Dalam Tugas Backend Twitter berisikan code program bagaimana melakukan LogIn data user, SignUp Data user, kemudian berisi kode pemograman  bagaimana data user yang sudah tersedia melakukan tweet
* dibawah ini adalah isi Data user dan Tweeters
```python
dataUser = [{
        "username": "John",
        "email": "john@haha.com",
        "password": "Hahaha123",
        "fullname": "John Rukmana"
    },
    {
        "username": "jeff",
        "email": "jeff@haha.com",
        "password": "Hahaha456",
        "fullname": "Jeff Abidin"
    }]

Tweeters = [{
        "email": "john@haha.com",
        "tweet": "john_93"
    },
    {
        "email": "jeff@haha.com",
        "tweet": "jeff_abidin03"

    }]
```
Jadi bagaimana dengan data diatas, kita bisa membuat program selayaknya twitter yang bisa LogIn, SignUP dan men- Tweet dari setiap email dan user name yang sudah terdaftar. Dengan syarat setiap SignUp data bisa langsung tersimpan(save) ke dalam file.json dan setiap Login harus bisa mengabil data dari file.json yang tersimpan, intinya seperti berikut :
```signUP = save ke file
login = cek login ke file 
tweet (bisa)	- post		:save tweet ke file dengan format tweet:
	        - get			tweet = { 
	        - Delete		text            : 
	        - Put			time/date       :
	    				sender/.email   :  
                                         }                       

```
di bawah ini salah satu Syntax program dari LogIn dan Signup
# ***Fitur-Fitur***

* LogIn Data user with Post 
```python
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
```

* Sign Up Data user with post
```python
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
        updateDataUser(dataUser) 
        return req
```
untuk lebih lanjut dan lebih lengkapnya silakan clone atau buka file diatas, dan jangan lupa untuk menjalan atau mencek menggunakan software tambahan seperti insomnia atau Postman. 

# Lisensi

*Lisensi proyek direktori Python ini merupakan Program Bootcamp Makers Institute dan merupakan domain publik (public domain)*

*Silakan untuk dipelajari jika di butuhkan, Semoga bermanfaat*