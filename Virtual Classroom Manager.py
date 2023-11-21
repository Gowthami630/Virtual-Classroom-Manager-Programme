# ClassroomManager class to manage classrooms, students, and assignments
class ClassroomManager:
    def __init__(self):
        # Initialize empty lists to store classrooms, students, and assignments
        self.classrooms = []
        self.students = []
        self.assignments = []

    # Method to add a new classroom
    def add_classroom(self, class_name):
        # Append a new classroom with its name, an empty list of students, and an empty list of assignments
        self.classrooms.append({"name": class_name, "students": [], "assignments": []})
        # Print a message indicating the creation of the classroom
        print(f"Classroom '{class_name}' has been created.")

    # Method to list all existing classrooms
    def list_classrooms(self):
        # Print the header for the list of classrooms
        print("List of Classrooms:")
        # Iterate through each classroom and print its name
        for classroom in self.classrooms:
            print(f"- {classroom['name']}")

    # Method to remove a classroom
    def remove_classroom(self, class_name):
        # Find and remove the specified classroom from the list of classrooms
        for classroom in self.classrooms:
            if classroom["name"] == class_name:
                self.classrooms.remove(classroom)
                # Print a message indicating the removal of the classroom
                print(f"Classroom '{class_name}' has been removed.")
                break

    # Method to enroll a student into a classroom
    def enroll_student(self, student_id, class_name):
        # Find the specified classroom and append the student ID to its list of students
        for classroom in self.classrooms:
            if classroom["name"] == class_name:
                classroom["students"].append(student_id)
                # Add the student to the list of students
                self.students.append({"id": student_id, "class": class_name})
                # Print a message indicating the enrollment of the student
                print(f"Student '{student_id}' has been enrolled in '{class_name}'.")

    # Method to list all students in a specific classroom
    def list_students_in_classroom(self, class_name):
        # Find the specified classroom and print the list of its students
        for classroom in self.classrooms:
            if classroom["name"] == class_name:
                print(f"Students in '{class_name}':")
                for student_id in classroom["students"]:
                    print(f"- {student_id}")
                break

    # Method to schedule an assignment for a classroom
    def schedule_assignment(self, class_name, assignment_details):
        # Find the specified classroom and append the assignment details to its list of assignments
        for classroom in self.classrooms:
            if classroom["name"] == class_name:
                classroom["assignments"].append(assignment_details)
                # Add the assignment to the list of assignments
                self.assignments.append({"class": class_name, "details": assignment_details})
                # Print a message indicating the scheduling of the assignment
                print(f"Assignment for '{class_name}' has been scheduled.")

    # Method to submit an assignment by a student for a specific classroom
    def submit_assignment(self, student_id, class_name, assignment_details):
        # Find the specified student and classroom and add the assignment details to the list of assignments
        for student in self.students:
            if student["id"] == student_id and student["class"] == class_name:
                self.assignments.append({"class": class_name, "student": student_id, "details": assignment_details})
                # Print a message indicating the submission of the assignment by the student
                print(f"Assignment submitted by Student '{student_id}' in '{class_name}'." )

# Example Usage:
class_manager = ClassroomManager()

# Continuously prompt the user for commands
while True:
    user_input = input("Enter command: ")
    parts = user_input.split()

    # Execute commands based on user input
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
