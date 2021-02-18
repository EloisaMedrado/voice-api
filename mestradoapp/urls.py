from django.conf.urls import url
from mestradoapp import views

urlpatterns = [
    url(r'^musics/$', views.MusicList.as_view(), name='music-list'),
    url(r'^api/metodo-post$', views.metodo_post, name='metodo-post'),
    url(r'^api/upload-file$', views.upload_file, name='upload-file'),
    url(r'^api/send-links$', views.send_links, name='send-links'),
]
