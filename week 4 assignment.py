class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, I am {self.name}, {self.age} years old, and my gender is {self.gender}.")

        
person = Person("Mark Kintu", 26, "Male")
person.introduce()