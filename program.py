from person_manager import *
from reader import *


persons = Csv_reader().read('person.csv')

persons = [Person(first_name=row[0], last_name=row[1], age=row[2]) for row in persons]

manager = Person_manager(persons)
    
manager.sort_persons_desc()


for person in manager.persons:
    print("firstname = " + person.first_name)
    print("lastname = " +  person.last_name)
    print("age = " + person.age)

    
print("--------------")
manager.sort_persons_asc()
    
for person in manager.persons:
    print("firstname = " + person.first_name)
    print("lastname = " +  person.last_name)
    print("age = " + person.age)

