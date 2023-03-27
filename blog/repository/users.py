from .. import hashing
from .. import models
from fastapi import HTTPException,status

# create new user

def newuser(request,db):
    new_user = models.user(name=request.name,email=request.email,password=hashing.hash.hashing(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# get new user 

def getuser(db,id):
    user = db.query(models.user).filter(models.user.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} not found")
    return user
    