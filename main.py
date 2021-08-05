class Fractie:
    def __init__(self, numarator, numitor):
        self.__numarator = numarator
        self.__numitor = numitor

    def __str__(self):
        return "{}/{}".format(self.__numarator, self.__numitor)

    def __add__(self, other):
        return Fractie.simplify(Fractie(self.__numarator * other.numitor + other.numarator * self.__numitor,
                                        self.__numitor * other.numitor))

    def __sub__(self, other):
        return Fractie.simplify(Fractie(self.__numarator * other.numitor - other.numarator * self.__numitor,
                                        self.__numitor * other.numitor))

    def inverse(self):
        return Fractie.simplify(Fractie(self.__numitor, self.__numarator))

    @staticmethod
    def simplify(fraction):
        if fraction.numarator < fraction.numitor:
            smallest = fraction.numarator
        else:
            smallest = fraction.numitor

        for i in range(1, smallest+1):
            if fraction.numarator % i == 0 and fraction.numitor % i == 0:
                gcd = i
        return Fractie(fraction.numarator / gcd, fraction.numitor / gcd)

    @property
    def numarator(self):
        return self.__numarator

    @numarator.setter
    def numarator(self, numarator):
        self.__numarator = numarator

    @property
    def numitor(self):
        return self.__numitor

    @numitor.setter
    def numitor(self, numitor):
        self.__numitor = numitor


f1 = Fractie(10, 4)
print("inversa fractiei {} este {}".format(f1, f1.inverse()))
f2 = Fractie(6, 4)
print("{} + {} = {}".format(f1, f2, f1.__add__(f2)))
print("{} - {} = {}".format(f1, f2, f1.__sub__(f2)))
