from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas,database,oauth2
from typing import List
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import blog

router = APIRouter(
    tags=['Blogs'],
    prefix='/blog'
)

@router.get('/',response_model=List[schemas.BlogBase])
async def get(db:Session=Depends(database.get_db),current_user:schemas.user=Depends(oauth2.get_current_user)):
    return blog.get_all(db)
   


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(blognew:schemas.blog,db:Session=Depends(get_db),current_user:schemas.user=Depends(oauth2.get_current_user)):
      return blog.createnewblog(db,blognew,current_user)
   

@router.get('/{id}',status_code=200,response_model=schemas.BlogBase)
async def getid(id,db:Session=Depends(get_db),current_user:schemas.user=Depends(oauth2.get_current_user)):
    return blog.getblogwithid(db,id)

    


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def deleteid(id,db:Session=Depends(get_db),current_user:schemas.user=Depends(oauth2.get_current_user)):
    return blog.deleteblog(db,id)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
async def update(id,requested:schemas.blog,db:Session=Depends(get_db),current_user:schemas.user=Depends(oauth2.get_current_user)):
    return blog.updateblog(db,requested,id)

