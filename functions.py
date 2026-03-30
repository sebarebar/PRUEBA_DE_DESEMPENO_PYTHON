def register_student(db, id, name, ege, course, status):
    student = {
        'id': id,
        'name': name,
        'age': ege,
        'course': course,
        'status': status
    }
    db.append(student)

    return db


def consult_list(db):

    if len(db) == 0:

        print("The student list is empty")
    else:
        for student in db:
            print("──────────────────────────────")
            print(f"ID: {student['id']}")
            print(f"name: {student['name']}")
            print(f"age: {student['age']}")
            print(f"course: {student['course']}")
            print(f"status: {student['status']}")
            print("──────────────────────────────")


def search_student(db, id):
    for student in db:
        if student['id'] == id:
            return student
    return None


def update_student(db, id, new_name, new_age=None, new_course=None, new_status=None):

    for student in db:
        if student['id'] == id:

            if new_name is not None:
                student['name'] = new_name

            if new_age is not None:
                student['age'] = new_age

            if new_course is not None:
                student['course'] = new_course

            if new_status is not None:
                student['status'] = new_status

            return True

    return False


def delete_product(db, id):

    for i, student in enumerate(db):
        if student['id'] == id:
            del db[i]
            return True
    return False
