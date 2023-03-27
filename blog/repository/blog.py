from .. import models
from fastapi import HTTPException,status

# get all blogs

def get_all(db):
    blogs=db.query(models.Blog).all()
    return blogs

# create new blogs

def createnewblog(db,blognew,current_user):
    userid=db.query(models.user).filter(models.user.email==current_user.get("sub")).first()
    new_blog = models.Blog(title=blognew.title,body=blognew.body,user_id=userid.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# get blogs with specific id

def getblogwithid(db,id):
    blogs=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blogs:
       # response.status_code= status.HTTP_404_NOT_FOUND
       # return {'detail':f"Blog with {id} not availiable"}
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} is not availiable")

    return blogs

# delete the blog

def deleteblog(db,id):
     blogs=db.query(models.Blog).filter(models.Blog.id==id)
     if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No Data found with id {id}")
     blogs.delete(synchronize_session=False)
     db.commit()
     return 'Done'

# update blog with id

def updateblog(db,requested,id):
    blogs=db.query(models.Blog).filter(models.Blog.id==id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No Data found with id {id}")
    blogs.update(dict(requested))
    #blogs.update({'title':'Titled Hello'})
    db.commit()
    return 'Updated Successfully'