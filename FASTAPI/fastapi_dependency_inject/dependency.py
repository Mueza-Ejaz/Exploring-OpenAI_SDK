from fastapi import FastAPI, Depends, Query, HTTPException
from typing import Annotated

from streamlit import status

app = FastAPI()

# Dependency function
def get_simple_goal():
    return {"goal": "We are building AI Agents Workforce"}


# Dependency injection in route
@app.get("/get-simple-goal")
def simple_goal(response :  Annotated[dict, Depends(get_simple_goal)]):
    return response

#--------------------------- Dependency injection in route with a parameter--------------------------------------------------

# dependency function with parameter
def get_goal(username: str):
    return {"goal": "We are building AI Agents Workforce", "username": username}
    
@app.get("/get-goal")
def get_my_goal(response :  Annotated[dict, Depends(get_goal)]):
    return response



#----------------------------------Dependency with Query Parameters------------------------------------------------ 

# depency function
def dep_login(username : str = Query(None), password : str = Query(None)):
    if username == "admin" and password == "admin":
        return {"message" : "Login Successful"}
    else:
        return {"message" : "Login Failed"}
    
@app.get("/signin")
def login_api(user :  Annotated[dict,Depends(dep_login)]):
    return user




#----------------------------------Multiple Dependencies------------------------------------------------

def depfunc1(num:int): 
    num = int(num)
    num += 1
    return num

def depfunc2(num): 
    num = int(num)
    num += 2
    return num

@app.get("/main/{num}")
def get_main(num: int, num1:  Annotated[int,Depends(depfunc1)], num2: Annotated[int,Depends(depfunc2)]):
    # Assuming you want to use num1 and num2 in some way
    #       1      2      3
    total = num + num1 + num2
    return f"Pakistan {total}"

# usage:
# http://127.0.0.1:8000/main/5

# num = 5
# depfunc1(5) returns 6
# depfunc2(5) returns 7
# Total = 5 + 6 + 7 = 18
# Response: "Pakistan 18"    


#---------------------------------------Dependency with Class------------------------------------------------

blogs = {
    "1": "Generative AI Blog",
    "2": "Machine Learning Blog",
    "3": "Deep Learning Blog"
}

users = {
    "8": "Ahmed",
    "9": "Mueza Ejaz"
}

class GetObjectOr404():
    def __init__(self, model)->None:
        self.model = model

    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Object ID {id} not found")
        return obj

blog_dependency = GetObjectOr404(blogs)

@app.get("/blog/{id}")
def get_blog(blog_name: Annotated[str, Depends(blog_dependency)]):
    return blog_name

user_dependency = GetObjectOr404(users)

@app.get("/user/{id}")
def get_user(user_name: Annotated[str, Depends(user_dependency)]):
    return user_name






