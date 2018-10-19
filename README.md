## *Backend Twitter*
___________________
> Dalam Tugas Backend Twitter berisikan code program bagaimana melakukan LogIn data user, SignUp Data user, kemudian berisi kode pemograman  bagaimana data user yang sudah tersedia melakukan tweet

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
        updateDataUser(dataUser) #
        return req
```
-----------
# Lisensi
-------
*Lisensi proyek direktori Python ini merupakan domain publik (public domain)*
*Program Bootcamp Makers Institute*

mau nyoba merge 
oke masih mencoba

kenapa ini ???? 
