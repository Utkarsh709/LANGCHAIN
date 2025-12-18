from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class Student(BaseModel):
    name:str
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,description='decimal value representing the cgpa of a students')
new_student={'name':'utkarsh','email':'utkarshvinay74@gmail.com','cgpa':7.8}
student=Student(**new_student)
student_dict=dict(student)
print(student_dict['age'])  