"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1

April 2023
Codescu Elisabeta Maria, 331AC
"""

from threading import Thread
import time

class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """

        Thread.__init__(self, **kwargs)

        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time
        self.name = kwargs['name']

        """
        Fiecarui client ii este dat un singur cos caruia ii apartine 
        un card_id, in acest cos
        clientul va putea adauga sau scoate produse mai tarziu, in run:
        """
        self.cart_id = self.marketplace.new_cart()


    def run(self):

        for cos in self.carts:
            for operatie in cos:

                tip = operatie["type"]
                prod = operatie["product"]
                cantitate = operatie["quantity"]

                if tip == "add":
                    for i in range(cantitate):
                        while self.marketplace.add_to_cart(self.cart_id, prod) is False:
                            time.sleep(self.retry_wait_time)

                if tip == "remove":
                    for j in range(cantitate):
                        self.marketplace.remove_from_cart(self.cart_id, prod)

        bon = self.marketplace.place_order(self.cart_id)
        for p in bon:
            print(self.name + " bought " + str(p))
