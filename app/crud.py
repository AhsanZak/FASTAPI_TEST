from sqlalchemy.orm import Session
from models import Students
from schemas import StudentSchema

def get_student(db:Session):
    return db.query(Students).all()

def create_student(db:Session, students: StudentSchema):
    _student = Students(full_name=students.full_name, email=students.email, password=students.password, 
    phone=students.phone_number)
    db.add(_student)
    db.commit()
    db.refresh(_student)
    return _student