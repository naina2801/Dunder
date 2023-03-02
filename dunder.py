class Employee:
    raise_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last +'@gmail.com'
    def fullname(self):
        return '{}.{}@gmail.com'.format(self.first,emp1.last)
    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amt)
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)
    def __str__(self):
        return '{}-{}'.format(self.fullname(),self.email)
emp1 = Employee("Naina","Mohamed",20000,)
emp2 = Employee("Star","Boy",30000)
print(emp1.__repr__())
print(emp1.__str__())