class User:
    def __init__(self,fname,lname,email,year):
        self.first_name=fname
        self.last_name=lname
        self.email=email
        self.age=year
        self.is__rewards_method=False
        self.gold_card_points=0
    def display_info(self):
        print(f"My first name is: {self.first_name}")
        print(f"My last name is: {self.last_name}")
        print(f"My email: {self.email}")
        print(f"I am {self.age} years old.")
    def enroll(self):
        self.is__rewards_method=True
        self.gold_card_points=200
        print(self.gold_card_points)
        if self.is__rewards_method==True:
            print(f"You are a gold card member!")
    def spend_points(self, amount):
        self.gold_card_points=self.gold_card_points-(amount)
        print(self.gold_card_points)

brooke=User("Brooke","Buroughs","brooke.buroughs102@gmail.com","21")
bradley=User("Bradley","Beumer","bradley.beumer@yahoo.com","22")
geck=User("Therapy","Gecko","nomail@gmail.com","1000")

brooke.display_info()
brooke.enroll()
brooke.spend_points(50)
bradley.enroll()
bradley.spend_points(80)
bradley.display_info()
geck.display_info()

#bonus Implement the logic to prevent over-spending and call the spend_points method with 40 points on the 3rd user.



