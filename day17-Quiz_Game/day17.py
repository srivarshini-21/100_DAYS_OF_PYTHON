# Class and constructor
class User():
    def __init__(self,user_id,name,salary,location):
        self.name=name
        self.id=user_id
        self.salary=salary
        self.address=location 
        self.ph_no = 0; # If you want the attribute to be modified at a later stage and do not want to assign a value initially
        self.followers=0
        self.following=0
    
    def follow(self,user):
        self.following+=1
        user.followers+=1
user_1=User("001","Henry",50000,"Bengaluru")
user_2=User("002","Ronnie",400000,"Hyderabad")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)