class AllSubjects:
    def __init__(self):
        self.class_dict = {}
        self.starting()

    def starting(self):
        txtfile = open("Classes.txt", "r")
        data = [[n for n in line.split(sep=",")] for line in txtfile]
        for x in range(len(data)):
            self.class_dict[data[x][0]] = data[x][1]
        print(self.class_dict)


class Subject:
    def __init__(self, classname):
        self.knowledge = None
        self.thinking = None
        self.communication = None
        self.application = None
        self.classname = classname
        self.weights = {"K/U": self.knowledge, "T/I": self.thinking, "C": self.communication, "A": self.application}


def run_code():
    classes = AllSubjects()
    print("Enter 'N' as your mark in a category if it is not assessed in this project.")
    while True:
        for x in classes.class_dict.keys():
            print("Course: " + str(x))
        course_picked = str(input("What course is this assignment in: "))
        if course_picked in classes.class_dict.keys():
            break
        else:
            print("You didn't select one of the classes")
            continue
    knowledge_total = input("How many K/U marks: ")
    if knowledge_total.upper() == "N":
        del classes.class_dict[course_picked][1][0]
    else:
        knowledge_mark = int(input("Mark in K/U\nOut of " + str(knowledge_total) + ": "))
    thinking_total = input("How many T/I marks: ")
    if thinking_total.upper() == "N":
        del classes.class_dict[course_picked][1][1]
    else:
        thinking_mark = int(input("Mark in T/I\nOut of " + str(thinking_total) + ": "))
    communication_total = (input("How many C marks: "))
    if communication_total.upper() == "N":
        del classes.class_dict[course_picked][1][2]
    else:
        communication_mark = int(input("Mark in C\nOut of " + str(communication_total) + ": "))
    application_total = input("How many A marks: ")
    if application_total.upper() == "N":
        del classes.class_dict[course_picked][1][3]
    else:
        application_mark = int(input("Mark in A\nOut of " + str(application_total) + ": "))

    print("Your weighted mark on this assessment is")