from functools import total_ordering

@total_ordering
class Person():

   
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __ne__(self, other):
        return self.age != other.age
    
    def __lt__(self, other):
        return self.age < other.age
    
