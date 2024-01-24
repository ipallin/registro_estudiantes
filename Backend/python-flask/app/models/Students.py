from marshmallow import fields
from datetime import date
import time
from sqlalchemy import func

from app import db, ma

class StudentModel(db.Model):
    __tablename__ = 'Student'

    id = db.Column(db.Integer() , primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    lastname = db.Column(db.String())
    shift = db.Column(db.String())
    startDate = db.Column(db.Date())
    endDate = db.Column(db.Date())

    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_student(cls, id):
        try:
            return cls.query.get(id)
        except Exception:
            raise Exception('Error inesperado ha impedido retornar el estudiante')

    @classmethod
    def get_currentStudents(cls):
       currentDate = date.today()
       unixdate = time.mktime(currentDate.timetuple())
       return cls.query.filter(unixdate < func.extract('epoch', cls.endDate))

    @classmethod
    def get_studentsbetweendates(cls, start, end):
        try:
            return cls.query.filter(start < func.extract('epoch', cls.endDate) and end >func.extract('epoch', cls.endDate))
        except Exception as e:
            raise e  

    @classmethod
    def add_student(cls, name, lastname, shift, startDate, endDate):
        try:
                student = StudentModel(
                    name=name, lastname=lastname, shift=shift, startDate=startDate, endDate=endDate)
                db.session.add(student)
                db.session.commit()
        except Exception as e:
            raise e

    @classmethod
    def edit_student(cls,id, name, lastname, shift, startDate, endDate):
        try:
            if db.session.query(cls.query.filter(cls.id == id).exists()).scalar():
                cls.query.filter(cls.id == id).update(
                    {'name': name, 'lastname': lastname, 'shift': shift, 'startDate':startDate, 'endDate':endDate})
                db.session.commit()
            else:
                raise Exception(
                    'There is not a record for this student.')
        except Exception as e:
            raise e

    @classmethod
    def detele_student(cls, id):
        try:
            if db.session.query(cls.query.filter(cls.id == id).exists()).scalar():
                cls.query.filter(
                    cls.id == id).delete()
                db.session.commit()
            else:
                raise Exception('There are not records for this student.')
        except Exception as e:
            raise e


class StudentSchema(ma.Schema):
    id = fields.Integer()
    name = fields.Str()
    lastname = fields.Str()
    shift = fields.Str()
    startDate = fields.Date()
    endDate = fields.Date()


student_schema = StudentSchema()
students_schema = StudentSchema(many=True)