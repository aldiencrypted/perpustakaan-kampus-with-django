from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from data import views as dataViews #mengambil semua yang ada di views data, karena ada views difile ini
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^data/',include('data.urls',namespace='data')),
    url(r'^$',views.index),

]

