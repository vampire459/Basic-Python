class student : 
    def __init__(self,name,major,gpa,is_on_probation) : 
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def worthy(self) :
        if self.gpa >= 4.5 :
            print(self.name ,"is Worthy")
        else :
            print(self.name ,"is Not Worthy")
        
