# input for name 
name = input("Enter your name: ")

# age input 
age = int(input("Enter your age: "))
# using an if statement to check the age input by the user 
if age > 18 :
    print(str(name), "is an adult")
else :
    print(str(name), "is not yet an adult")

dec = float(input("Enter a decimal number: ")) 
print("The number ", str(dec), "is a decimal number")

# location input 
location = input("Enter your prefered location: ")

#  printing out ythe personalized message 
print(f"Hello, my name is ",str(name), ". I am ",str(age), "years old and i live in ", str(location), ".")
