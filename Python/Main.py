#import library
# from Human import Human
from Human import Mahasiswa
from Human import Dosen
from Matkul import Matkul
from Prodi import Prodi

# instance object dari class Mahasiswa
mahasiswa1 = Mahasiswa("Simon", "He/Him", "ITB", "simon@itb.edu",
                       "2101310", "FMIPA", "Teknik Informatika")
mahasiswa2 = Mahasiswa("Maria", "She/Her", "Binus",
                       "maria@binus.edu", "2101311", "FMIPA", "Teknik Informatika")
mahasiswa3 = Mahasiswa("Mai", "They/Them", "Binus",
                       "mai@binus.edu", "2101312", "FMIPA", "Teknik Informatika")

# instance object dari class Dosen
dosen1 = Dosen("1111", "Hiro Rio",  "FPMIPA", "S3", "Machine Learning")
dosen2 = Dosen("2222", "Rias Amelia", "FPMIPA", "S3", "Operating System")
dosen3 = Dosen("3333", "Mario Malik", "FPMIPA", "S2", "Big Data")

# instance object dari class Matkul
Matkul1 = Matkul("Machine Learning")
Matkul2 = Matkul("Operating System")
Matkul3 = Matkul("Big Data")

# instance object dari class Prodi
prodi1 = Prodi("Teknik Informatika", "IT")

# output
print("Program Studi " + prodi1.getNamaProdi() "/" prodi1.getKode())
