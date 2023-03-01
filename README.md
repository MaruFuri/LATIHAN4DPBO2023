# LATIHAN4DPBO2023
# Saya Akmal Zulkifli NIM 2101310 mengerjakan Latihan 4 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.


# Deskripsi Tugas
Buatlah program berbasis OOP menggunakan bahasa pemrograman C++ dan Python  yang mengimplementasikan konsep inheritance, composition, dan array of object pada kelas-kelas tersebut:
1. Mahasiswa: NIM, nama, jenis_kelamin, fakultas, prodi
2. Human: NIK, nama, jenis_kelamin
3. SivitasAkademik: asal_universitas, email_edu
4. Dosen: NIP, nama, jenis_kelamin, fakultas, prodi, pend_terakhir, keahlian
5. Course: nama_matakuliah, 
6. Program Studi: nama_prodi, kode, course

# Desain Program
Terdapat file Human.py yang berisi class Human, Sivitas, Mahasiswa, dan Dosen.
Terdapat file Matkul.py yang berisi class Matkul.
Terdapat file Prodi.py yang berisi class Prodi.
Terdapat file Main.py yang berisi kode untuk output.

class Human terdiri dari
- **nik** : string
- **name** : string
- **gender** : string

class Sivitas terdiri dari
- **univ** : string
- **email** : string

class Mahasiswa terdiri dari
- **nim** : string
- **faculty** : string
- **major** : string

class Dosen terdiri dari
- **nip** : string
- **nama** : string
- **fakultas** : string
- **gelar** : string
- **keahlian** : string

class Matkul terdiri dari
- **namaMatkul** : string

class Prodi terdiri dari
- **namaProdi** : string
- **kode** : string

#Program
Output merupakan input manual(hardcode). Output merupakan print dari class 'Prodi' yang kemudian melakukan print data 'mahasiswa', 'dosen', dan 'mata kuliah'
