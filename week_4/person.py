class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello! My name is {self.name}, I am {self.age} years old, and I am {self.gender}.")


# Create an instance of the Person class
person = Person("John Doe", 30, "male")

# Call the introduce method to display the person's information
person.introduce()

class Madee:
    def __init__(self, alc, ban, amount):
        self.alc = alc
        self.ban  = ban
        self.amount = amount

    def calling(self):
        print(f"Welcome to Madee club, You just ordered {self.alc}, and a packet of {self.ban}, the total amout is {self.amount}")
    

# creating the instance of the class madee 
madee = Madee("General",  "Burger", 100)

# calling the calling method 
madee.calling()
