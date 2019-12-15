from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
app_name = 'data'
urlpatterns = [
    url(r'^pinjam/$',views.pinjam,name='pinjam'),
    url(r'^$', views.index, name='index'),

]
urlpatterns += staticfiles_urlpatterns()
