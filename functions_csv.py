import csv


def save_student_list(db, filename, include_header=True):
    try:
        if len(db) == 0:
            print("List the students is empty. No data to save.")
            return
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(
                file, fieldnames=['id', 'name', 'age', 'course', 'status'])
            if include_header:
                writer.writeheader()
            writer.writerows(db)
        print(f"Student list saved to: {filename}")
    except Exception as e:
        print(f"Error occurred while saving student list: {e}")


def upload_list(path):
    try:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            if reader.fieldnames != ['id', 'name', 'age', 'course', 'status']:
                print(
                    "Error: CSV file must have id', 'name', 'age', 'course' and 'status' columns.")
                return []
            db = []
            invalid_rows = 0
            for row in reader:
                try:
                    id = int(row['id'])
                    name = row['name']
                    age = int(row['age'])
                    course = row['course']
                    status = row['status']

                    if age < 0:
                        raise ValueError(
                            "Price and quantity must be non-negative.")
                    db.append(
                        {'id': id, 'name': name, 'age': age, 'course': course, 'status': status})
                except ValueError as e:
                    print(f"Warning: Skipping invalid row: {row} - Error: {e}")
                    invalid_rows += 1
            print(f"{invalid_rows} invalid rows skipped.")
            return db
    except FileNotFoundError:
        print("Error: file not found.")
        return []
    except UnicodeDecodeError:
        print("Error: file encoding not supported.")
        return []
