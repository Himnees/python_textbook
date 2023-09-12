# Program 6: A python program to store data into instances using mutator methods and to retrieve data from the instances using accessor methods.
class students:

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name
    
    def setMarks(self,marks):
        self.marks=marks

    def getMarks(self):
        return self.marks
    
n=int(input('How many students:'))
i=0
while i<n:
    s=students()
    name=input('Enter name:')
    s.setName(name)
    marks=int(input('Enter marks:'))
    s.setMarks(marks)

    print('Hi',s.getName())
    print('Your marks',s.getMarks())
    i+=1
    print('-----------------------')