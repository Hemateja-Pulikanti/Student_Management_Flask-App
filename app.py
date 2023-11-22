from flask import Flask, render_template, request, redirect, url_for, json

app = Flask(__name__)

def get_data():
    with open('data/details.json') as json_file:
        return json.load(json_file)

def save_data(data):
    with open('data/details.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)

def calculate_average_marks(student):
    marks = student['Marks'].values()
    result = sum(marks) / len(marks) if len(marks) > 0 else 0
    return round(result,2)

def calculate_percentage(average_marks):
    result = round(average_marks, 2)
    return f"{result} %"

def calculate_grade(average_marks):
    if average_marks >= 90:
        return 'A+'
    elif 80 <= average_marks < 90:
        return 'A'
    elif 70 <= average_marks < 80:
        return 'B'
    elif 60 <= average_marks < 70:
        return 'C'
    elif 50 <= average_marks < 60:
        return 'D'
    else:
        return 'F'

@app.route('/')
def main_page():
    data = get_data()
    students = data['students']
    student_names = [student['Full Name'] for student in students]
    return render_template('home_page.html', student_names=student_names)

@app.route('/student/<int:index>')
def get_student_details(index):
    data = get_data()
    students = data['students']

    if 0 <= index < len(students):
        student_details = students[index]
        average_marks = calculate_average_marks(student_details)
        percentage = calculate_percentage(average_marks)
        grade = calculate_grade(average_marks)
        return render_template(
            'home_page.html',
            student_names=[student['Full Name'] for student in students],
            student_details=student_details,
            average_marks=average_marks,
            percentage=percentage,
            grade=grade
        )
    else:
        return "<h1> Student not Found </h1>"

@app.route('/delete_student/<name>', methods=['POST'])
def delete_student(name):
    data = get_data()
    students = data['students']

    for index, student in enumerate(students):
        if student['Full Name'] == name:
            deleted_student = students.pop(index)
            save_data(data)
            break

    return redirect(url_for('main_page'))

@app.route('/add_student', methods=['GET'])
def add_student_page():
    return render_template('add_student.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    new_student_name = request.form.get('new_student_name')
    new_student_age = int(request.form.get('new_student_age'))
    new_student_dob = request.form.get('new_student_dob')
    new_student_class = request.form.get('new_student_class')

    new_subjects = request.form.getlist('new_subjects[]')
    new_marks = request.form.getlist('new_marks[]')

    data = get_data()
    students = data['students']

    # Check if the student with the same name already exists
    for student in students:
        if student['Full Name'] == new_student_name:
            return "<h1>Student with the same name already exists!</h1>"

    # Add the new student
    new_student = {
        "Full Name": new_student_name,
        "Age": new_student_age,
        "Date of Birth": new_student_dob,
        "Class": new_student_class,
        "Subjects List": new_subjects,
        "Marks": {subject: int(mark) for subject, mark in zip(new_subjects, new_marks)}
    }

    students.append(new_student)
    save_data(data)

    return redirect(url_for('main_page'))

if __name__ == "__main__":
    app.run(host = '0.0.0.0')
