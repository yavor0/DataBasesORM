from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref


engine = create_engine('mysql://root:123456y@127.0.0.1/test', echo=True)
Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    num = Column(Integer, nullable=False)
    classnum = Column(Integer, nullable=False)
    classletter = Column(String(1), nullable=False)
    nickname = Column(String(150))


class StudentPrivateInfo(Base):
    __tablename__ = 'studentsprivateinfo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    EGN = Column(String(10), nullable=False, unique=True)
    address = Column(String(100), nullable=False)
    student_id = Column(Integer,ForeignKey('students.id'), unique=True)
    
    parent = relationship("Student", backref=backref("StudentPrivateInfo", uselist=False))


students = [
    Student(name='Исидор Иванов', num=15, classnum=10, classletter='б'),
    Student(name='Панчо Лалов', num=20, classnum=10, classletter='б'),
    Student(name='Петраки Ганьов', num=20, classnum=10, classletter='а'),
    Student(name='Александър Момчев', num=1, classnum=8, classletter='а')
]

students_private_info = [
    StudentPrivateInfo(EGN='0042294120', address='Mladost 4', student_id=1),
    StudentPrivateInfo(EGN='0042394100', address='Mladost 4', student_id=4),
    StudentPrivateInfo(EGN='0442649280', address='Lulin', student_id=2),
    StudentPrivateInfo(EGN='0445192940', address='Boyana', student_id=3)
]

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
session.add_all(students)
session.add_all(students_private_info)
session.commit()

for x in session.query(Student, StudentPrivateInfo).filter(Student.id == StudentPrivateInfo.student_id).all():
   print (f"Name: {x.Student.name}\nEGN: {x.StudentPrivateInfo.EGN}\nAddress: {x.StudentPrivateInfo.address}\n")
