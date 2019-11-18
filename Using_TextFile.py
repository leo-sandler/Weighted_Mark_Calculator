class Subject:
    def __init__(self, classname):
        self.knowledge = None
        self.thinking = None
        self.communication = None
        self.application = None
        self.classname = classname
        self.weights = {"K/U": self.knowledge, "T/I": self.thinking, "C": self.communication, "A": self.application}

class Student:
    def __init__(self):
        self.class_dict = {}
        self.starting()

        self.marks_dict = {}

        self.subject = None
        self.subject_picker()

        self.knowledge_total = None
        self.knowledge_mark = None

        self.mark_collection()

    def starting(self):
        txtfile = open("Classes.txt", "r")
        data = [[n for n in line.split(sep=",")] for line in txtfile]
        for x in range(len(data)):
            self.class_dict[data[x][0]] = data[x][1]
        print(self.class_dict)

    def subject_picker(self):
        while True:
            for x in self.class_dict.keys():
                print("Course: " + str(x))
            course_picked = str(input("What course is this assignment in: "))
            if course_picked in self.class_dict.keys():
                self.subject = course_picked
                break
            else:
                print("You didn't select one of the classes")
                continue

    def mark_collection(self):
        while True:
            self.knowledge_total = input("How many K/U marks: ")
            if self.knowledge_total.isdigit() and int(self.knowledge_total) > 0:
                self.knowledge_mark = input("Mark in K/U\nOut of " + str(self.knowledge_total) + ": ")
                if self.knowledge_mark.isdigit() and int(self.knowledge_mark) > 0 and self.knowledge_mark <= self.knowledge_total:
                    self.marks_dict["K/U"] = int(self.knowledge_mark)
                    break
            elif self.knowledge_total == str:
                self.marks_dict["K/U"] = None
                break
            else:
                continue


def run_code():
    user = Student()
    print("Enter 'N' as your mark in a category if it is not assessed in this project.")


    thinking_total = input("How many T/I marks: ")
    if thinking_total.upper() == "N":

    thinking_mark = int(input("Mark in T/I\nOut of " + str(thinking_total) + ": "))

    communication_total = (input("How many C marks: "))
    if communication_total.upper() == "N":

    communication_mark = int(input("Mark in C\nOut of " + str(communication_total) + ": "))

    application_total = input("How many A marks: ")
    if application_total.upper() == "N":

    application_mark = int(input("Mark in A\nOut of " + str(application_total) + ": "))

