# Generated by Django 2.2.7 on 2019-11-21 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_remove_mahasiswa_fakultas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('kode_buku', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('judul', models.CharField(max_length=255)),
                ('pengarang', models.CharField(max_length=255)),
                ('penerbit', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Penjaga',
            fields=[
                ('nip', models.CharField(max_length=18, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=50)),
                ('jabatan', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Peminjaman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tanggal', models.DateField()),
                ('Nama_Buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Buku')),
                ('Peminjam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Mahasiswa')),
            ],
        ),
    ]
