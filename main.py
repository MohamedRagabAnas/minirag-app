from fastapi import FastAPI
app=FastAPI()

@app.get("/welcome")
def welocome ():
    return{
        "message":"Hello RAG!"
    }