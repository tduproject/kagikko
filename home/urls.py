from django.conf.urls import url
from . import views
#home ページルーティング

urlpatterns = [
    #homeページルーティング
    url(r'^',views.index, name = 'home_index'),
]