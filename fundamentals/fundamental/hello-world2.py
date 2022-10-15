#1 print "hello world"
print("Hello World")
#2 print "hello noelle!" with the name in a variable
name="Noelle"
print("Hello",name,"!")
print("Hello "+name+"!")
#2a "hello brooke!" with comma notation
name="Brooke"
print("Hello",name,"!")
print(f"Hello {name}!") #extra
#2b "hello brooke!" with plus notation
name="Brooke"
print("Hello "+name+"!")
#3 print "hello 42!" with the number in a variable
name=42
print("Hello",name,"!")
print("Hello "+str(42)+"!")
#3a "hello num!" with favorite number and comma
num=3
print("Hello",num,"!")
#3b "hello num!" with fav number and +
num=22
print("Hello "+str(22)+"!")
#4 print "I love to eat sushi and pizza." with the foods in variables
fave_food1="sushi"
fave_food2="pizza"
print("I love to eat {} and {}.".format(fave_food1,fave_food2))
print(f"I love to eat {fave_food1} and {fave_food2}.")
#4a&b two favorite foods
true_fav1="huevos et arroz"
true_fav2="cinnamon applesauce"
print("I love to eat {} and {}!".format(true_fav1,true_fav2))
print(f"I love to eat {true_fav1} and {true_fav2}!")
