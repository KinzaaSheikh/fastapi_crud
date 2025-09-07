from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
def index():
    return {"message": "Welcome to FastAPI nerds"}

valid_users = []

@app.get("/user/login")
def login(username:str, password:str):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    else:
        user = valid_users.get(username)
        if checkpw(password.encode(), user.passphrase.e):
            return user
        else:
            return {"message": "incorrect password"}
        
@app.post("/user/signup")
def signup(uname:str, passwd:str):
    if (uname == None and passwd == None):
        return {"message": "invalid user"}
    elif not valid_users.get(uname) == None:
        return {"message": "user exists"}
    else:
        user = User(username = uname, password = passwd)
        pending_users[uname] = user
        return user

