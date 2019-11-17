class Subject:
    def __init__(self, classname):
        self.knowledge = None
        self.thinking = None
        self.communication = None
        self.application = None
        self.classname = classname
        self.weights = {"K/U": self.knowledge, "T/I": self.thinking, "C": self.communication, "A": self.application}


    def weight_filling(self):
        for n in self.weights:
            present = input("Is the " + str(n) + " category assessed (T/F): ")
            if present.upper() == "T":
                continue
            else:
                weight = float(input("What is the weighted percentage for the " + str(n) + " category: %"))
                self.weights[n] = weight
        print(self.weights)


newclass = Subject("Chemistry")

