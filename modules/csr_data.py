class CSRData:
    def __init__(self):
        self.__aa = []
        self.__ia = []
        self.__ja = []

    def register_value(self, val):
        self.__aa.append(val)

    def register_ja(self, j):
        self.__ja.append(j)

    def register_ia(self, i):
        self.__ia.append(i)

    def get_values(self):
        return self.__aa

    def get_ia_values(self):
        return self.__ia

    def get_ja_values(self):
        return self.__ja
