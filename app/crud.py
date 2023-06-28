from sqlalchemy.orm import Session
from models import Students
from schemas import StudentSchema, Response
import dbconnect as dbc

def get_student(db:Session):
    return db.query(Students).all()

def create_student(db:Session, students: StudentSchema):
    _student = Students(full_name=students.full_name, email=students.email, password=students.password, 
    phone=students.phone_number)
    
    try:
        db.add(_student)
        db.flush()
        db.commit()
        profile_data = {"_id":_student.id, "file_path": students.profile_image}
        result = dbc.insert_profile_image(profile_data)
        db.refresh(_student)
        return Response(status="Ok",
                    code="200",
                    message="Student created successfully").dict(exclude_none=True)
    except:
        print("Excption  ")
        return Response(status="Failed",
                    code="409",
                    message="Email Already Exist").dict(exclude_none=True)