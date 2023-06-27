from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import StudentSchema, RequestStudent, Response
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
async def create(request: RequestStudent, db: Session = Depends(get_db)):
    crud.create_student(db, students=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Student created successfully").dict(exclude_none=True)

@router.get("/")
async def get(db:Session=Depends(get_db)):
    _student = crud.get_student(db)
    return Response(code=200, status="Ok", message="Success Fethced all", result=_student).dict(exclude_none=True)


