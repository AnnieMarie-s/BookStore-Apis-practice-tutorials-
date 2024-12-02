
from django.urls import path, include
# from django.conf.urls import url
from django.contrib.auth.views import LoginView,LogoutView
from bookapi.views import bookList, bookDetails, bookoperations, booksort, updatebook, Listbook

urlpatterns = [
    path('book/create', bookList.as_view()),
    path('book/list', bookList.as_view()),
    path('book/delete/<int:pk>', bookDetails.as_view()),
    path('book/<int:pk>', bookDetails.as_view()),
    path('book/update/<int:pk>', bookDetails.as_view()),
    path('book/<int:pk>/update/', updatebook.as_view()),
    path('book/find', bookoperations.as_view()),
    path('book/sort/price', booksort.as_view()),
    path('book/sort/<str:pk>', booksort.as_view()),
    path('book/filter', Listbook.as_view()),
    #  path('login/', LoginView.as_view()),
    #   path('logout/', LogoutView.as_view()),
]
