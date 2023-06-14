from django.urls import re_path, include,path
 
from . import views 
 
app_name = 'artisr'
urlpatterns = [
    re_path(r'^Trang_chu', views.IndexView.as_view(), name='index'),
    re_path(r'^(?P<pk>[0-9]+)/details/$', views.DetailView.as_view(), name='detail'),
    re_path(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    re_path(r'^(?P<musician_id>[0-9]+)/numstar/$', views.num_stars_function, name='numstar'),
    re_path(r'^(?P<musician_id>[0-9]+)/delete/$', views.delete_song, name='delete_song'),
    re_path(r'^(?P<musician_id>[0-9]+)/add_song/$', views.add_song, name='add_song'),
    re_path(r'^add_singer/$', views.add_singer, name='add_singer'),
    re_path(r'^(?P<musician_id>[0-9]+)/detail_infor/$', views.detail_infor, name='detail_infor'), 
    re_path(r'^(?P<musician_id>[0-9]+)/update_infor/$', views.update_infor, name='update_infor'), 
    re_path(r'^(?P<musician_id>[0-9]+)/delete_singer/$', views.delete_singer, name='delete_singer'),
    re_path(r'^search/$', views.search_singer, name='search_singer'),
    re_path(r'^user_signup/', views.user_signup, name='user_signup'),
    re_path(r'^user_login/', views.user_login, name='user_login'),
    re_path(r'^user_logout/', views.user_logout, name='user_logout'),
]
