"""
Suppose that you want to order some food with a delivery.
Use Facade Design Pattern and classes of your choice to simulate a scenario of ordering using an application,
you can have a dispatcher, a restaurant, a delivery guy and other actors of your choice.
The most important thing is that you should have some method which will organize the priority of
the steps that need to be taken when you order the delivery and will "ask" the right parties to do their job.
This should happen without intervention of the client.
"""

import time


class Dispatcher:

    def get_order(self, order):
        print(f"You order is taken. Order: {order}.")
        time.sleep(1)
        return order


class Restaurant:

    def make_order(self, order):
        time.sleep(2)
        print(f"You order is being cooked. Order: {order}.")
        return order


class DeliveryGuy:

    def deliver_order(self, order):
        time.sleep(3)
        print(f"You order is being delivered. Order: {order}.")
        return order


class FoodApp:

    def __init__(self):
        self.dispatcher = Dispatcher()
        self.restaurant = Restaurant()
        self.delivery_guy = DeliveryGuy()


    def make_order(self, order):
        return self.delivery_guy.deliver_order(self.restaurant.make_order(self.dispatcher.get_order(order)))



if __name__ == "__main__":

    ggFood = FoodApp()
    ggFood.make_order("pizza")

