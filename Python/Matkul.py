class Matkul:
    # atribut
    __namaMatkul = ""

    # constructor
    def __init__(self, namaMatkul=""):
        self.__namaMatkul = namaMatkul

    # kumpulan method setter dan getter untuk tiap atribut
    def setMatkul(self, namaMatkul):
        self.__namaMatkul = namaMatkul

    def getMatkul(self):
        return self.__namaMatkul
