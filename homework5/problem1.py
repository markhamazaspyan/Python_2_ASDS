"""
Create a Person class which will have attributes Name, Last Name, Email and Age.
Use the Decorator pattern and any additional classes of your choice to implement the following logic:
If the Person is a child (age<14), s/he wants the information about them printed as follows:
*** &&& Name - Last Name - Email &&& ***. Otherwise, print the information like this: &&& Name - Last Name - Email &&&.
"""


class Human:
    def __init__(self, name, last_name, email, age):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.age = age


    def speak(self):
        return f"{self.name} - {self.last_name} - {self.email}"


class Child(Human):
    def __init__(self, wrapped: Human):
        self._wrapped = wrapped

    def speak(self):
        print(f"*** &&& {self._wrapped.speak()} &&& ***")

class Adult(Human):
    def __init__(self, wrapped: Human):
        self._wrapped = wrapped

    def speak(self):
        print(f"&&& {self._wrapped.speak()} &&&")


class Person:
    def __init__(self,name, last_name, email, age):
        self.h = Human(name, last_name, email, age)

    def info(self):
        if self.h.age<14:
            Child(self.h).speak()
        else:
            Adult(self.h).speak()


if __name__ == '__main__':
    p = Person("Vazgen","Avagyan", "v@gmail.com", 20)
    p.info()

    p = Person("Vazgen", "Grigoryan", "v98@gmail.com", 10)
    p.info()
