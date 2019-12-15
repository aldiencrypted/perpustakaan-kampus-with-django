from django.contrib import admin

# Register your models here.

from .models import Data_Mahasiswa, Data_Peminjaman, Data_Penjaga, Data_Buku

admin.site.register(Data_Mahasiswa)
admin.site.register(Data_Penjaga)
admin.site.register(Data_Buku)
admin.site.register(Data_Peminjaman)

