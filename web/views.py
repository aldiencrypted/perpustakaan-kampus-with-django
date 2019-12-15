from django.shortcuts import render

def index(request):
    context = {
        'page_title':'Selamat Datang',
    }
    return render(request,'index.html',context)
