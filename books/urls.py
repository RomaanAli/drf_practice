from django.urls import path
from  . import views

urlpatterns=[

    path('books/',views.book_list,name='book_list'),
    path('books/<int:pk>/',views.book_detail,name='book_detail'),


    path('cbv/books/', views.BookListAPI.as_view(), name='cbv_book_list'),
    path('cbv/books/<int:pk>/', views.BookDetailAPI.as_view(), name='cbv_book_detail'),


    path('generic/books/', views.BookListCreateView.as_view(), name='generic_book_list'),
    path('generic/books/<int:pk>/', views.BookDetailView.as_view(), name='generic_book_detail'),
]
