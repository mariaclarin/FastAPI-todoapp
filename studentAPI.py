from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        "name":"Bagus",
        "age" :17,
        "year":"L4AC"
    },
    2:{
        "name":"Manuaba",
        "age" :20,
        "year":"L4AC"
    }
}

class Student(BaseModel):
    name : str
    age : int
    year : str

#to update only so that the user dont have to change all name year and age in order to update,
#can jst change 1 attribute at a time also
class UpdateStudent(BaseModel):
    name : Optional[str]=None
    age : Optional[int]=None
    year : Optional[str]=None

@app.get("/")
def index():
    return {"Testing":"first"}

#if the attribute is called in the get function, its a path parameter
@app.get("/get-student/{student_id}")
def get_student(student_id:int):
    return students[student_id]

#if the attribute isnt called in the .get() but is a parameter in the function, its a query parameter. 
#so student_id is a path parameter while name, test is a query parameter
@app.get("/get-by-name/{student_id}")
def get_student(*,name:str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data":"Not found"}

@todo.get("/get-by-name/")
def get_todo(*,title:str):
    for todo_id in todos:
        if todos[todo_id]["title"] == title:
            return students[student_id]
    return {"Data":"Not found"}


#create a new object but in memory only not permanently put
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error":"Student exists"}
    
    students[student_id]=student
    return students[student_id]

#to update post objects
@app.put("/update-student/{student_id}")
def update_student(student_id:int, student:UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    #so to only update the specific attribute
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return {"Error" : "Student does not exist"}
    
    del students[student_id]
    return {"Message": "Student deleted successfully"}

