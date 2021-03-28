from fastapi import FastAPI
from typing import Optional

app= FastAPI()

# we have different http requests such as get,put,post,delete are called as operations here.

@app.get('/')
def root():
    return {"data":"blog list"}

@app.get("/about")              #"/about" is called as path and the entire statement is called as path operation decorator
def about():                     #this is path operation function
    return {"data":"this is about page"}

@app.get("/blog/unpublished")   #Now this works fine
def unpublished():
    return {'data':'All unpublished'}

@app.get("/blog/{id}")          #Here variable in the route can be used inside thee function needs to be declared in {}
def blog_id(id:int):                #the same variable in the route needs to be placed in parameters
    #this api helps us to fetch the blog with some blog_id = id
    return {"blog_id":id}

@app.get("/blog/{id}/comments")
def blog_comments(id:int):              #this data validation using pydentic module which is built in for fastapi
    # fetch comments of specified blog_id
    return {"data":{1,2,2},"id":id}

@app.get("/blog/unpublished")
# we get error because routes doesnot support function overloading and interpreter reads line by line
#if you want this to work you need to put this above the "/blog/{id}"
def unpublished():
    return {'data':'All unpublished'}

''' It is always a issue for the backend developers who deals with building the APIS.
So we make use of tools like POSTMAN and so on. Fast API comes with builtin features that helps the developers to do validations, encryptions
and also lets the developers to look and understand the flow of data.
 '''

'''
If you are unsure whether you will be sending the parameters to the url, then you can pass them in the paramenter list
without specifying them in the decorator. like the code snippet mentioned below using optional
'''

@app.get("/blog")
def blog_Data(limit:int = 10,published:bool = False , sort: Optional[str] = None):
    if published:
        return {"data":f"{limit} are published"}
    else:
        return {"data":f"{limit} are unpublished"}

#27-03-2021 : ended at -   https://youtu.be/7t2alSnE2-I?t=3361

