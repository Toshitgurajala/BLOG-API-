from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,models
from ..hashing import hash
from ..database import get_db 
from sqlalchemy.orm import Session
from .. import JWTtoken
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user = db.query(models.user).filter(models.user.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid Credentials")
    
    if not hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect Password")
    
    JWTtoken.access_token_expires = timedelta(minutes=JWTtoken.ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = JWTtoken.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}