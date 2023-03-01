class Prodi:
    # atribut
    __namaProdi = ""
    __kode = ""
    __course = ""

    # constructor
    def __init__(self, namaProdi="", kode=""):
        self.__namaProdi = namaProdi
        self.__kode = kode
        # self.__course = course

    # kumpulan method setter dan getter untuk tiap atribut
    def setProdi(self, namaProdi):
        self.__namaProdi = namaProdi

    def getProdi(self):
        return self.__namaProdi

    def setKode(self, kode):
        self.__kode = kode

    def getKode(self):
        return self.__kode

    # def setCourse(self, course):
    #     self.__course = course

    # def getCourse(self):
    #     return self.__course
