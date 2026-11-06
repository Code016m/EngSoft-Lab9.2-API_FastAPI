from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo para requisição POST
class User(BaseModel):
    name: str

# Rota GET principal
@app.get("/")
def home():
    return {"message": "Hello World!"}

# Rota GET com parâmetro
@app.get("/salutation")
def salutation(name: str = "Guest"):
    return {"message": "Hello " + name + "!"}

# Rota POST
@app.post("/salutation")
def user_salutation(user: User):
    return {"message": "Hello " + user.name + "!"}

# Rota PUT
@app.get("/user/{name}/update")
@app.put("/user/{name}/update")
def update_user(name: str):
    return {"message": "User name updated: " + name}

# Rota DELETE
@app.get("/user/{name}/delete")
@app.delete("/user/{name}/delete")
def delete_user(name: str):
    return {"message": "Deleted user name: " + name + "!"}
