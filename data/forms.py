from django import forms

class PostPeminjaman(forms.Form):
    NIM = forms.CharField(max_length=10)
    Buku = forms.CharField(max_length=255)
    Tanggal_Pinjam = forms.DateField()
    Petugas = forms.CharField(max_length=50)