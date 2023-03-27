from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import users


router = APIRouter(
    tags=['User'],
    prefix='/user'
)

@router.post('/',response_model=schemas.usershoe)
async def createuser(request:schemas.user,db:Session = Depends(get_db)):
   return users.newuser(request,db)
   

@router.get('/{id}',response_model=schemas.usershoe)
async def showuser(id,db:Session=Depends(get_db)):
    return users.getuser(db,id)