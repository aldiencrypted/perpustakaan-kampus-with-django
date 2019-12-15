from django.shortcuts import render
from .forms import PostPeminjaman
from .models import Data_Peminjaman, Data_Mahasiswa, Data_Buku, Data_Penjaga
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    buku = Data_Buku.objects.all()

    context = {
        'page_title':'Data Mahasiswa',

    }
    return render(request,'index.html',context)

def pinjam(request):
    post_pinjam = PostPeminjaman()
    #maha = Data_Mahasiswa.objects.only('nim').get(nim=da)
    if request.method == 'POST':
        #mengambil data yang telah diinputkan
        nim = request.POST['NIM']
        nbuku = request.POST['Buku']
        pj = request.POST['Petugas']
        # karena jenis yang digunakan foreignkey maka kita harus menyamakan dengan database lainnya dengan cara
        mahasiswa = Data_Mahasiswa.objects.get(nim=nim)
        buku = Data_Buku.objects.get(judul=nbuku)
        penanggung = Data_Penjaga.objects.get(nama=pj)
        #memasukan data yang telah diinputkan
        Data_Peminjaman.objects.create(
            Peminjam = mahasiswa,
            Nama_Buku = buku,
            Penanggung_Jawab = penanggung,
            Tanggal = request.POST['Tanggal_Pinjam'],
        )


        return HttpResponseRedirect('/data/pinjam')
    context = {
        'page_title':'Pinjam Buku',
        'isi':'Pinjam Buku',
        'datapinjam':post_pinjam
    }

    return render(request,'pinjam.html',context)
