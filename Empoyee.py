class Person(object):
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class Employmee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        Person. __init__(self,name,idnumber)
a-Employee('Rahul',996012,200000,"Intern")
a.display()



