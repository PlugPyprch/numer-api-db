from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends, Body
from app.config import SessionLocal
from sqlalchemy.orm import Session
from app.schemas import EquaSchema, Request, Response, RequestEqua
from app.auth.jwt_handler import signJWT
from app.auth.jwt_bearer import jwtBearer
from app.model import PostSchema, UserSchema, UserLoginSchema

import app.crud

router = APIRouter()
users =[UserSchema(fullname='Plug', email='plug@example.com', password='123')]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create", dependencies=[Depends(jwtBearer())])
async def create_equa_service(request: RequestEqua, db: Session = Depends(get_db)):
    app.crud.create_equa(db, equa=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Equation created successfully").dict(exclude_none=True)


@router.get("/")
async def get_equas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _equa = app.crud.get_equa(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_equa)

def check_user(data : UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False
    
@router.post('/login')
def user_login(user : UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error" : "Invalid login details"
        }


# @router.patch("/update")
# async def update_book(request: RequestEqua, db: Session = Depends(get_db)):
#     _book = app.crud.update_book(db, book_id=request.parameter.id,
#                             title=request.parameter.title, description=request.parameter.description)
#     return Response(status="Ok", code="200", message="Success update data", result=_book)


# @router.delete("/delete")
# async def delete_book(request: RequestEqua,  db: Session = Depends(get_db)):
#     app.crud.remove_book(db, book_id=request.parameter.id)
#     return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
