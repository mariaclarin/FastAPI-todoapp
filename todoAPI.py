from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

todo = FastAPI()

class Todo(BaseModel):
    title : str
    description : str
    status : str

class UpdateTodo(BaseModel):
    title : Optional[str] = None
    description :Optional[str] = None
    status :  Optional[str] = None

class User(BaseModel):
    auth : str
    name : str
    email : str

class UpdateUser(BaseModel):
    auth : Optional[str] = None
    name :  Optional[str] = None
    email : Optional[str] = None

todos = {
    1: Todo(title="Cook dinner", description="Spaghetti Bolognese and Aglio Olio Ravioli", status="incomplete"),
    2: Todo(title="Exercise and cardio", description="Jog for 30 mins and yoga", status="completed")
}

users ={
    1:User(auth="google", name="Harry Styles", email="hs@gmail.com"),
    2:User(auth="local", name="Taylor Swift", email="tswift@yahoo.com")
}


@todo.get("/")
def index():
    return {"Maria Clarin":"FastAPI TodoApp"}


#User Functions====================================================
#GET ALL USERS
@todo.get("/get-all-user/")
def get_user():
    return users

#GET USER BY THEIR ID
@todo.get("/get-user-by-id/{user_id}")
def get_user(user_id: int = Path(description="ID of the user to view")):
    return users[user_id]

#GET USER BY THEIR NAME
@todo.get("/get-user-by-name/{name}")
def get_user(name: str = Path(description="Name of the user to view")):
    for user_id in users:
        if users[user_id].name== name:
            return users[user_id]
    return {"Error":"User does not exist"}

#FILTER USER BY THE AUTH METHOD
@todo.get("/filter-user-auth/{auth}")
def filter_user(auth: str = Path(description="Enter auth method to view user (google or local)")):
    for user_id in users:
        if users[user_id].auth== auth:
            return users[user_id]
    return {"Message":"No user found with this auth method"}

#CREATE USER
@todo.post("/create-user/{user_id}")
def create_user(user_id: int, user:User):
    if user_id in users:
        return {"Error":"User already exists"}
    users[user_id]=user
    return users[user_id]

#UPDATE USER
@todo.put("/update-user/{user_id}")
def update_user(user_id:int, user:UpdateUser):
    if user_id not in users:
        return {"Error": "User does not exist"}
    
    #so to only update the specific attribute
    if user.auth != None:
        users[user_id].auth = user.auth
    if user.name != None:
        users[user_id].name = user.name
    if user.email != None:
        users[user_id].email = user.email

    return users[user_id]

#DELETE USER
@todo.delete("/delete-user/{user_id}")
def delete_user(user_id:int):
    if user_id not in users:
        return {"Error" : "User does not exist"}
    
    del users[user_id]
    return {"Message": "User deleted successfully"}


#Todo Item Functions===============================================
#GET EVERY TODOITEM
@todo.get("/get-all-todo/")
def get_todo():
    return todos

#GET TODOITEM BY THE ID
@todo.get("/get-todo-by-id/{todo_id}")
def get_todo(todo_id: int = Path(description="ID of the todo item to view")):
    return todos[todo_id]

#GET TODOITEM BY THE TITLE
@todo.get("/get-todo-by-title/{title}")
def get_todo(title: str = Path(description="Name of the todo item to view")):
    for todo_id in todos:
        if todos[todo_id].title== title:
            return todos[todo_id]
    return {"Error":"Todo item does not exist"}

#FILTER TODOITEMS BY THEIR STATUS
@todo.get("/filter-todo-status/{status}")
def filter_todo(status: str = Path(description="Enter completed or incomplete todos to view")):
    for todo_id in todos:
        if todos[todo_id].status== status:
            return todos[todo_id]
    return {"Message":"No todo items found for this status"}

#CREATE TODOITEM
@todo.post("/create-todo/{todo_id}")
def create_todo(todo_id: int, todo:Todo):
    if todo_id in todos:
        return {"Error":"Todo item already exists"}
    todos[todo_id]=todo
    return todos[todo_id]

#UPDATE TODOITEMS
@todo.put("/update-todo/{todo_id}")
def update_todo(todo_id:int, todo:UpdateTodo):
    if todo_id not in todos:
        return {"Error": "Todo item does not exist"}
    
    #so to only update the specific attribute
    if todo.title != None:
        todos[todo_id].title = todo.title
    if todo.description != None:
        todos[todo_id].description = todo.description
    if todo.status != None:
        todos[todo_id].status = todo.status

    return todos[todo_id]

#DELETE TODOITEMS
@todo.delete("/delete-todo/{todo_id}")
def delete_todo(todo_id:int):
    if todo_id not in todos:
        return {"Error" : "Todo item does not exist"}
    
    del todos[todo_id]
    return {"Message": "Todo item deleted successfully"}