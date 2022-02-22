#object oriented programm (oop)
#procedure oop/function oop

class Student:
    city='kathmandu'
    country='nepal'
    def read(self):
        print('read logic')
    def write(self):
        print('write logic')
    def info(self):
        print(self.countryname)
student1=Student()
student2=Student()
student2.read()
student1.write()
student1.info()
print(student1)