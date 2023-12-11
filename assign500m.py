class Student:
    
    user_input = input("Checking all the ptoperties and methods")
    
    def __init__(self,n,r)->None:
        self.name = n
        self.roolnumber = r
        
        
    def setName(self,name):
        self.__name =name
    
    def getName(self):
        return self.__name
    
    def setRollNumber(self,RollNumber):
        self.__RollNumber =RollNumber
    
    def getRollNumber(self):
        return self.__RollNumber
    
print("Expecting perfectly defined fields and getter/setters")
    
    