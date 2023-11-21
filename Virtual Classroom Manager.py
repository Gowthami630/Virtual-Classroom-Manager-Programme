class ClassroomManager:
    def _init_(self):
        self.classrooms = []
        self.students = []
        self.assignments = []

    def add_classroom(self, class_name):
        self.classrooms.append({"name": class_name, "students": [], "assignments": []})
        print(f"Classroom '{class_name}' has been created.")

    def list_classrooms(self):
        print("List of Classrooms:")
        for classroom in self.classrooms:
            print(f"- {classroom['name']}")

    def remove_classroom(self, class_name):
        for classroom in self.classrooms:
            if classroom["name"] == class_name:
                self.classrooms.remove(classroom)
                print(f"Classroom '{class_name}' has been removed.")
                break

    def enroll_student(self, student_id, class_name):
        for classroom in self.classrooms:
            if classroom["name"] == class_name:
                classroom["students"].append(student_id)
                self.students.append({"id": student_id, "class": class_name})
                print(f"Student '{student_id}' has been enrolled in '{class_name}'.")

    def list_students_in_classroom(self, class_name):
        for classroom in self.classrooms:
            if classroom["name"] == class_name:
                print(f"Students in '{class_name}':")
                for student_id in classroom["students"]:
                    print(f"- {student_id}")
                break

    def schedule_assignment(self, class_name, assignment_details):
        for classroom in self.classrooms:
            if classroom["name"] == class_name:
                classroom["assignments"].append(assignment_details)
                self.assignments.append({"class": class_name, "details": assignment_details})
                print(f"Assignment for '{class_name}' has been scheduled.")
                break

    def submit_assignment(self, student_id, class_name, assignment_details):
        for student in self.students:
            if student["id"] == student_id and student["class"] == class_name:
                self.assignments.append({"class": class_name, "student": student_id, "details": assignment_details})
                print(f"Assignment submitted by Student '{student_id}' in '{class_name}'." )
                break

    # Other methods remain the same

# Example Usage:
class_manager = ClassroomManager()

while True:
    user_input = input("Enter command: ")
    parts = user_input.split()

    if parts[0] == "add_classroom":
        class_manager.add_classroom(parts[1])
    elif parts[0] == "list_classrooms":
        class_manager.list_classrooms()
    elif parts[0] == "remove_classroom":
        class_manager.remove_classroom(parts[1])
    elif parts[0] == "enroll_student":
        class_manager.enroll_student(parts[1], parts[2])
    elif parts[0] == "list_students":
        class_manager.list_students_in_classroom(parts[1])
    elif parts[0] == "schedule_assignment":
        assignment_details = ' '.join(parts[2:])
        class_manager.schedule_assignment(parts[1], assignment_details)
    elif parts[0] == "submit_assignment":
        assignment_details = ' '.join(parts[3:])
        class_manager.submit_assignment(parts[1], parts[2], assignment_details)
    else:
        print("Invalid command.")

    # Print counts or other required information if needed