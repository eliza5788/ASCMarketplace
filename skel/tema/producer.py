"""
This module represents the Producer.

Computer Systems Architecture Course
Assignment 1
April 2023
Codescu Elisabeta Maria, 331AC
"""

from threading import Thread
import time


class Producer(Thread):
    """
    Class that represents a producer.
    """

    def __init__(self, products, marketplace, republish_wait_time, **kwargs):
        """
        Constructor.

        @type products: List()
        @param products: a list of products that the producer will produce

        @type marketplace: Marketplace
        @param marketplace: a reference to the marketplace

        @type republish_wait_time: Time
        @param republish_wait_time: the number of seconds that a producer must
        wait until the marketplace becomes available

        @type kwargs:
        @param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.products = products
        self.marketplace = marketplace
        self.republish_wait_time = republish_wait_time

        """
        Tot in acest constructor se initializeaza si id-ul unic asociat fiecarui producator,
        cu ajutorul metodei register_producer din marketplace.py
        """
        self.producer_id = self.marketplace.register_producer()

    def run(self):
        """
        Se parcurge lista products: fiecarui element din aceasta lista ii corespunde:
         [produs, cantitate, timp_asteptare] , asa cum se specifica in enuntul de pe ocw al temei.

        """
        while True:
            for product in self.products:

                produs = product[0]
                cantitate = product[1]
                timp_asteptare = product[2]

                """
                Se itereaza prin fiecare cantitate aleasa pentru fiecare dintre 
                produsele din lista products, cu ajutorul unui for in interiorul
                altui for. Atata timp cat un anumit produs nu poate fi inca
                publicat in Marketplace, se asteapta pentru o anumita perioada
                de timp pana cand se reincearca din nou, adica republish_wait_time. 
                Atunci cand in sfarsit se poate publica produsul respectiv,
                se asteapta perioada de timp specificata in timp_asteptare pentru 
                produsul respectiv, care este necesara pentru fabricarea/
                pregatirea efectiva a produsului. Pentru aceste asteptari,
                utilizam functia sleep din biblioteca time.
                """
                for i in range(cantitate):
                    while self.marketplace.publish(self.producer_id, produs) is False:
                        time.sleep(self.republish_wait_time)
                    time.sleep(timp_asteptare)
