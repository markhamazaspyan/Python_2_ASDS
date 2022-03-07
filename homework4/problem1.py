from abc import ABC, abstractmethod


"""
Let say you want to send a message to someone. You have 2 options - you can Email the message or 
SMS the message to the corresponding person. So, you have two options to send the message and the 
client side code will use one of the implementations to send the message to the corresponding person. 
Use Bridge Design Pattern to implement the logic with classes of your choice and make sure to test the implementation with some concrete objects.
"""


class SendMessage(ABC):

    @abstractmethod
    def send_message(self, message, person):
        pass


class TypeEmail(SendMessage):

    def send_message(self, message, person):
        print(f"Email is for {person} and states the following: {message}.")



class TypeSMS(SendMessage):

    def send_message(self, message, person):
        print(f"SMS is for {person} and states the following: {message}.")


class Messenger:

    def __init__(self, type):
        self.type = type


    def send(self, message, person):
        self.type.send_message(message, person)



if __name__=="__main__":
    email = Messenger(TypeEmail())
    email.send("Hello", "Bob")

    email = Messenger(TypeSMS())
    email.send("I said hello via email", "Bob!!!")