from person import *

class Person_manager:
    
    persons: Person
    
    def __init__(self, persons : Person):
        self.persons = persons
               
    def sort_persons_desc(self):
        for i in range(len(self.persons)): 
            for j in range(len(self.persons)-1): 
                if (self.persons[i] > self.persons[j]):
                    self._swap_persons(i, j)
                    
    def sort_persons_asc(self):
        for i in range(len(self.persons)): 
            for j in range(len(self.persons)-1): 
                if (self.persons[i] < self.persons[j]):
                    self._swap_persons(i, j)  
                
                
    def _swap_persons(self, index1, index2):
            cache = self.persons[index2]
            self.persons[index2] = self.persons[index1]
            self.persons[index1] = cache
        
    


