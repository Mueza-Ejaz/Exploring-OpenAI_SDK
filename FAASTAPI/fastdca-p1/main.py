from fastapi import FastAPI # import FastAPI framework for building APIs

app = FastAPI() # create an instance of FastAPI


# Handle GET request for the homepage route
@app.get("/")
def read_root():
    return {"Welcome" : "Mueza Ejaz!"} # returns a JSON response with inital code 



@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}




    