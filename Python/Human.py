# inisialisasi class Human (sebagai base class / parent class utama)
class Human:
    # atribut
    __nik = ""
    __name = ""
    __gender = ""

    # constructor
    def __init__(self, nik="", name="", gender=""):
        self.__nik = nik
        self.__name = name
        self.__gender = gender

    # kumpulan method setter dan getter untuk tiap atribut
    def setNik(self, nik):
        self.__nik = nik

    def getNik(self):
        return self.__nik

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender


# inisialisasi class Sivitas sebagai child dari class Human
class Sivitas(Human):
    # atribut
    __univ = ""
    __email = ""

    # constructor
    def __init__(self, university="", email=""):
        self.__univ = university
        self.__email = email

    # kumpulan method setter dan getter untuk tiap atribut
    def setUniv(self, university):
        self.__univ = university

    def getUniv(self):
        return self.__univ

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

# inisialisasi class Mahasiswa sebagai child dari class Sivitas (juga "cucu" dari class Human)


class Mahasiswa(Sivitas):
    # atribut
    __nim = ""
    __faculty = ""
    __major = ""

    # constructor
    def __init__(self, name="", gender="", university="", email="", nim="", faculty="", major=""):
        super().__init__(name, gender, university, email)
        self.__nim = nim
        self.__faculty = faculty
        self.__major = major

    # kumpulan method setter dan getter untuk tiap atribut
    def setNim(self, nim):
        self.__nim = nim

    def getNim(self):
        return self.__nim

    def setFaculty(self, faculty):
        self.__faculty = faculty

    def getFaculty(self):
        return self.__faculty

    def setMajor(self, major):
        self.__major = major

    def getMajor(self):
        return self.__major

# inisialisasi class Mahasiswa sebagai child dari class Sivitas (juga "cucu" dari class Human)


class Dosen(Sivitas):
    # atribut
    __nip = ""
    __nama = ""
    __fakultas = ""
    __gelar = ""
    __keahlian = ""

    # constructor
    def __init__(self, nip="", nama="", fakultas="", gelar="", keahlian=""):
        self.__nip = nip
        self.__nama = nama
        self.__fakultas = fakultas
        self.__gelar = gelar
        self.__keahlian = keahlian

    # kumpulan method setter dan getter untuk tiap atribut
    def setNIP(self, nip):
        self.__nip = nip

    def getNIP(self):
        return self.__nip

    def setNama(self, nama):
        self.__nama = nama

    def getNama(self):
        return self.__nama

    def setFakultas(self, fakultas):
        self.__fakultas = fakultas

    def getFakutas(self):
        return self.__fakultas

    def setGelar(self, gelar):
        self.__gelar = gelar

    def getGelar(self):
        return self.__gelar

    def setKeahlian(self, keahlian):
        self.__keahlian = keahlian

    def getKeahlian(self):
        return self.__keahlian
