class Student:
    def __init__(self, name):
        self.name = name
        self.Nt = self.Notebook()

    def show(self):
        print(self.name, end=" ")
        self.Nt.show()

    class Notebook:
        def __init__(self):
            self.model = "HP"
            self.CPU = "i7"
            self.RAM = "16"

        def show(self):
            print(f"=> {self.model}, {self.CPU}, {self.RAM}")


s1 = Student("Roman")
s2 = Student("Vladimir")
s1.show()
s2.show()
