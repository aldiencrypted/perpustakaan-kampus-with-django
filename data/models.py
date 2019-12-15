from django.db import models

# Create your models here.

class Data_Mahasiswa(models.Model):
    nim = models.CharField(max_length=10, primary_key=True)
    nama = models.CharField(max_length=255)
    email = models.EmailField()
    prodi = models.CharField(max_length=30)
    fakultas = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.nama)

class Data_Penjaga(models.Model):
    nip = models.CharField(max_length=18, primary_key=True)
    nama = models.CharField(max_length=50)
    jabatan = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.nama)

class Data_Buku(models.Model):
    kode_buku = models.CharField(max_length=5, primary_key=True)
    judul = models.CharField(max_length=255)
    pengarang = models.CharField(max_length=255)
    penerbit = models.CharField(max_length=255)

    def __str__(self):
        return "{}".format(self.judul)

class Data_Peminjaman(models.Model):
    Peminjam = models.ForeignKey(Data_Mahasiswa, on_delete=models.CASCADE )
    Nama_Buku = models.ForeignKey(Data_Buku, on_delete=models.CASCADE)
    Penanggung_Jawab=models.ForeignKey(Data_Penjaga, on_delete=models.CASCADE)
    Tanggal = models.DateField()

    def __str__(self):
        return "{}".format(self.id)