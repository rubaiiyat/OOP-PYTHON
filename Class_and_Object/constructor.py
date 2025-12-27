class Student:
    def __init__(self,name, roll, mark):
        self.name=name
        self.roll=roll
        self.mark=mark 

    def display(self):
        if self.mark>=40:
            print(f"{self.name} has been passed with mark {self.mark}")
        else:
            print(f"{self.name} has been failed with mark {self.mark}")

std1=Student("Alice",1,85)
std2=Student("Bob",2,35)
std1.display()
std2.display()