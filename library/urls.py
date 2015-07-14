from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    
    url(r'^books/add/$', views.add_book, name="add"),
    url(r'^books/(?P<book_id>[0-9]+)/delete$', views.delete_book, name="delete"),
    url(r'^books/(?P<book_id>[0-9]+)/detail$', views.show_book_details, name="detail"),
    url(r'^books/(?P<book_id>[0-9]+)/edit$', views.edit_book, name="edit"),
    url(r'^books/search/$', views.search_for_book, name="search"),
    url(r'^books/$', views.list_books, name="list"),
]
