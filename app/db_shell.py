from app.models import Employee
import random
import string
#exec(open(r"C:\Users\mypc\Desktop\pythonclass\Django\CSV\app\db_shell.py").read())
des = ['Software Engineer', 'sr. Software Engineer', 'Linux Adminstrator', 'Associate','CEO', 'Python Devolper']

for i in range(50):
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(10))

    letters = string.ascii_uppercase
    comp = ''.join(random.choice(letters) for i in range(10))

    letters = string.digits
    sal = ''.join(random.choice(letters) for i in range(5))

    des = random.choice(des)
    emp = Employee(name=name, salary=sal, company=comp, designation=des)
    emp.save()


