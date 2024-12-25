from datetime import datetime, timedelta

class Teacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def create_homework(self, text, deadline):
        homework = Homework(text, deadline)
        return homework

    def __str__(self):
        return(f"First name: {self.first_name}\n"
               f"Last name: {self.last_name}\n")

class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework):
        if homework.is_active():
            return str(homework)
        else:
            print("You are late")
            return None

    def __str__(self):
        return (f"First name: {self.first_name}\n"
                f"Last name: {self.last_name}\n")

class Homework:
    def __init__(self, text, days_to_complete):
        self.text = text
        self.deadline = timedelta(days=days_to_complete)
        self.created = datetime.now()

    def is_active(self):
        """Checks, if homework is still active (not overdue)."""
        current_time = datetime.now()
        deadline_time = self.created + self.deadline
        return current_time <= deadline_time

    def __str__(self):
        return (f"Task: {self.text}\n"
                f"Created: {self.created.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Deadline: {self.deadline}\n")

if __name__ == '__main__':
    teacher = Teacher('Dmitry', 'Orlyakov')
    student = Student('Vladislav', 'Popov')
    #teacher.last_name  # Daniil
    #student.first_name  # Petrov

    print(str(teacher))
    print(str(student))

    expired_homework = teacher.create_homework('Learn functions', 0)
    #expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    #expired_homework.deadline  # 0:00:00
    #expired_homework.text  # 'Learn functions'

    print(str(expired_homework))

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    #oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late