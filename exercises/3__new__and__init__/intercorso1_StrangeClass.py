"""
Fornire la classe StrangeClass che funziona in modo tale che la seconda istanza creata sia identica alla prima,
la quarta sia identica alla terza e così via. Istanze vengono considerate identiche se nascono identiche e lo restano
durante la loro intera vita
"""


class StrangeClass:
    counter = 0
    instances = []

    def __init__(self):
        # Incrementa il contatore di istanze
        StrangeClass.counter += 1

        # Se è la prima istanza, inizializza il dizionario
        if StrangeClass.counter == 1:
            self.__dict__ = {}
        else:
            # Se non è la prima, duplica lo stato dall'istanza appropriata
            index_to_copy = (StrangeClass.counter - 2)  # Indice dell'istanza da copiare
            if index_to_copy < len(StrangeClass.instances):
                self.__dict__ = StrangeClass.instances[index_to_copy].__dict__

        # Aggiungi l'istanza corrente alla lista delle istanze
        StrangeClass.instances.append(self)


if __name__ == '__main__':
    obj1 = StrangeClass()
    obj1.value = 10

    obj2 = StrangeClass()  # Dovrebbe essere identico a obj1
    obj3 = StrangeClass()
    obj3.value = 20

    obj4 = StrangeClass()  # Dovrebbe essere identico a obj3

    print(f"obj1_dict: {obj1.__dict__}")  # Output: {'value': 10}
    print(f"obj2_dict: {obj2.__dict__}")  # Output: {'value': 10} (identico a obj1)
    print(f"obj3_dict: {obj3.__dict__}")  # Output: {'value': 20}
    print(f"obj4_dict: {obj4.__dict__}")  # Output: {'value': 20} (identico a obj3)

    obj3.v2 = 3

    print(f"obj4_dict: {obj4.__dict__}")
