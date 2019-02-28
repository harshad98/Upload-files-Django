from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('', views.index,name= 'prax-index'),
   path('upload/', views.upload,name='upload'),
   path('books/', views.book_list, name='book_list'),
   path('books/upload/', views.upload_book, name='upload_book'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),

]
