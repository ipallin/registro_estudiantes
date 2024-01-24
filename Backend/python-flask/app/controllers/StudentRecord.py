from flask import Blueprint, request, jsonify
from datetime import datetime
import time
from ..models.Students import StudentModel, student_schema, students_schema


student_bp = Blueprint('student', __name__)


@student_bp.route('/student', methods=['GET'])
def get_student():
    id = request.args.get('id')

    try:
        if(id != None):
            id = int(id)
            student = StudentModel.get_student(id)
            if student != None:
                data = student_schema.dump(StudentModel.get_student(id))
                return jsonify({'status': 200, 'data': data, 'ok': True})
            else:
               return jsonify({'status': 404, 'title': 'Not found', 'detail': 'No record for this student', 'ok': False}), 404 
        else:
            return jsonify({'status': 400, 'title': 'Bad Request', 'detail': 'Missing query paramenter, you have to specify an id.', 'ok': False}), 400
    except Exception as e:
        return jsonify({'status': 500, 'title': 'Error', 'detail': e.args[0], 'ok': False}), 500
    
@student_bp.route('/students', methods=['GET'])
def get_students():
    start = request.args.get('start')
    end = request.args.get('end')
    try:
        if (start == None or end == None):
            data = students_schema.dump(StudentModel.get_all())
            return jsonify({'status': 200, 'data': data, 'ok': True})
        else:
            parsedDate1 = datetime.strptime(start, "%Y-%m-%d")
            startunixdate = time.mktime(parsedDate1.timetuple())
            parsedDate2 = datetime.strptime(end, "%Y-%m-%d")
            endunixdate = time.mktime(parsedDate2.timetuple())
            data = students_schema.dump(StudentModel.get_studentsbetweendates(startunixdate, endunixdate))
            return jsonify({'status': 200, 'data': data, 'ok': True})
    except Exception as e:
        return jsonify({'status': 500, 'title': 'Error', 'detail': e, 'ok': False}), 500

@student_bp.route('/currentstudents', methods=['GET'])
def get_currentstudents():
    try:
        data = students_schema.dump(StudentModel.get_currentStudents())
        return jsonify({'status': 200, 'data': data, 'ok': True})
    except Exception as e:
        return jsonify({'status': 500, 'title': 'Error', 'detail': e, 'ok': False}), 500

@student_bp.route('/add-student', methods=['POST'])
def add_student():
    data = request.get_json()
    try:
        StudentModel.add_student( data.get('name'), data.get('lastname'), data.get('shift'),
            data.get('startDate'), data.get('endDate'))
        return jsonify({'status': 200, 'data': data, 'ok': True})
    except Exception as e:
        return jsonify({'status': 500, 'title': 'Error', 'detail': str(e), 'ok': False}), 500


@student_bp.route('/edit-student', methods=['PUT'])
def edit_student():
    data = request.get_json()

    try:
        if(data.get('id')):
            StudentModel.edit_student( data.get('id'), data.get('name'), data.get('lastname'), data.get('shift'),
                data.get('startDate'), data.get('endDate'))
            return jsonify({'status': 200, 'data': data, 'ok': True})
        else:
            return jsonify({'status': 400, 'title': 'Bad Request', 'detail': 'Missing paramenter, you have to specify a student.', 'ok': False}), 400
    except Exception as e:
        return jsonify({'status': 500, 'title': 'Error', 'detail': str(e), 'ok': False}), 500


@student_bp.route('/delete-student', methods=['DELETE'])
def delete_student():
    id = int(request.args.get('id'))

    try:
        if(id):
            StudentModel.detele_student(id)
            return jsonify({'status': 200, 'ok': True})
        else:
            return jsonify({'status': 400, 'title': 'Bad Request', 'detail': 'Missing paramenter, you have to specify a student id.', 'ok': False}), 400
    except Exception as e:
        return jsonify({'status': 500, 'title': 'Error', 'detail': str(e), 'ok': False}), 500

