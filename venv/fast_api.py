from fastapi import FastAPI, UploadFile, APIRouter
from pydantic import BaseModel
from datetime import date
# from .routers import items, users

app = FastAPI(title="2024/06/18 FastAPI Practice")
# app.include_router(users.router)
router = APIRouter()
# router.include_router(router1.router)
fake_db = {
    "users": {
        1: {
            "name": "John",
            "age": 35,
            "email": "john@fakemail.com",
            "birthday": "2000-01-01",
        },
        2: {
            "name": "Jane",
            "age": 25,
            "email": "jane@fakemail.com",
            "birthday": "2010-12-04",
        }
    }
}

class User(BaseModel):
    id: int
    neme: str
    email: str
    birthday: date

# items_db = [{"Max": 22}, {"item_name": "Item-2"}]

@app.get("/{name}", description="Hello name")
async def root(name: str):
    return {f'message": "Hello World {name}'}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

@router.get("/users/{user_id}", tags=["users"])
async def get_users(user_id: int, qry: str = None):
    if user_id not in fake_db["users"]:
        return {"error": "User not found"}
    return {"user": fake_db['users'][user_id], "query": qry }

@router.get("/users/test", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.delete("/users/{user_id}", tags=["users"])
async def delete_item(user_id: int):
    fake_db["users"].pop(user_id)
    return fake_db

app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)