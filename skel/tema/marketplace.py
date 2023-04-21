"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1

April 2023
Codescu Elisabeta Maria, grupa 331AC

"""
import threading

class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """
    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        self.queue_size_per_producer = queue_size_per_producer

        """Pe masura ce mai apare un producator sau un client, le va fi atribuit 
        un producer_id sau un cart_id
        #in functie de valoarea curenta a atributelor producer_ids si cart_ids, 
        in metodele register_producer
        #si new_cart, definite mai jos. Initial, acestea sunt 0 pentru ca marketplace-ul 
        nu a fost inca populat:
        """
        self.producer_ids =  0
        self.cart_ids = 0

        """Fiecare producator "producer_id" va avea anumite produse asociate. Folosim un 
        dictionar pentru a pastra evidenta producatorilor si a produselor lor
        """

        self.dictionary_of_producers = {}

        """Fiecare cos de cumparaturi cart_id contine diverse produse de la 
        diversi producatori. Din nou folosim un dictionar care va avea cheie 
        fiecare cart_id si valoarea cheii va fi lista de produse
        si producatorul corespunzator
        """

        self.dictionary_of_carts = {}

        self.lock = threading.Lock()


    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        with self.lock:

            self.producer_ids = self.producer_ids + 1
            self.dictionary_of_producers.update({self.producer_ids: []})

            return self.producer_ids

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        product_queue = self.dictionary_of_producers[producer_id]
        product_queue_size = len(product_queue)

        if product_queue_size >= self.queue_size_per_producer:
            return False
        else:
            self.dictionary_of_producers[producer_id].append(product)
            return True


    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        with self.lock:

            self.cart_ids = self.cart_ids + 1
            self.dictionary_of_carts.update({self.cart_ids: []})

            return self.cart_ids

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        for i in self.dictionary_of_producers:

            """
            Se itereaza prin produsele fiecarui producator pentru a se putea gasi 
            obiectul dorit si pentru a se adauga in cos:
            """

            if product in self.dictionary_of_producers[i]:

                item = (product, i)
                self.dictionary_of_carts[cart_id].append(item)

                """
                Produsul a fost gasit si adaugat in cos, deci devine 
                indisponibil pentru ceilalti clienti
                """
                self.dictionary_of_producers[i].remove(product)

                return True
        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        """Se itereaza prin toate produsele din cosul cart_id pentru a se putea identifica care
        #este produsul care trebuie scos din cos
        """

        for product_to_return in self.dictionary_of_carts[cart_id]:

            product_to_return_name = product_to_return[0]

            if product == product_to_return_name:
                """
                #Produsul redevine disponibil pentru ceilalti clienti
                #Valoarea cheii cart_id este o lista care are 2 elemente, 
                mereu al doilea element fiind id-ul producatorului caruia ii 
                apartine produsul. Astfel, ne folosim de product_to_return[1]
                pentru a putea afla idul producatorlui in lista caruia 
                trebuie sa readaugam produsul
                """
                product_to_return_producer = product_to_return[1]
                self.dictionary_of_producers[product_to_return_producer].append(product)

                """
                Produsul este abia acum scos din cos, deoarece daca 
                l-am fi scos inainte, am fi pierdut idul producatorului sau 
                si nu am fi stiut in lista carui producator sa il readaugam
                """

                self.dictionary_of_carts[cart_id].remove(product_to_return)
                return

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        """
        Se parcurge cosul corespunzator idului primit la apelarea functiei,
        adaugandu-se fiecare produs pe bon. La final, clientul si-a finalizat
        cumparaturile si bonul a fost inchis, deci nu mai e nevoie de cosul
        de cumparaturi cart_id. Acesta este sters din dictionarul cu 
        cosuri de cumparaturi in uz
        """
        bon = []

        for product_to_buy in self.dictionary_of_carts[cart_id]:
            bon.append(product_to_buy[0])

        self.dictionary_of_carts.pop(cart_id)

        return bon
