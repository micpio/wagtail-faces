
from django.urls import path
from .views import SearchResultsView
from . import views

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('book_index/',views.book_index,name='book_index'),
    path('show/<int:pk>/',views.show,name='show'),


]
