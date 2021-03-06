from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/image$', views.new_image, name='new_image'),
    url(r'^edit/profile',views.edit_profile, name='edit-profile'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^look/',views.look, name='look'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)