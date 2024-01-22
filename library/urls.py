from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView



app_name = 'library'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('info-register/', InformationView.as_view(), name='info-register'),


    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='library:login'), name='logout'),

    path('books/', BookView.as_view(), name='book-list'),
    path('book/create/', BookCreate.as_view(), name='book-create'),
    path('book/<slug:pk>/', BookDetail.as_view(), name= 'book'),
    path('book/<slug:pk>/update/', BookUpdate.as_view(), name='book-update'),
    path('book/<slug:pk>/delete/', BookDelete.as_view(), name='book-delete'),



    path('members/', MemberView.as_view(), name='member-list'),
    path('member/create/', MemberCreate.as_view(), name='member-create'),
    path('member/<slug:pk>/', MemberDetail.as_view(), name='member-detail'),
    path('member/<slug:pk>/update/', MemberUpdate.as_view(), name='member-update'),
    path('member/<slug:pk>/delete/', MemberDelete.as_view(), name='member-delete'),

    path('users/', UsersView.as_view(), name='users-list'),
    path('users/create/', UsersCreate.as_view(), name='users-create'),
    path('user/<slug:pk>/', UsersDetail.as_view(), name='users-detail'),


    path('borrowers/', BorrowerView.as_view(), name='borrower-list'),
    path('borrower/create/', BorrowerCreate.as_view(), name='borrower-create'),
    path('borrower/<slug:pk>/', BorrowerDetail.as_view(), name= 'borrower'),
    path('borrower/<slug:pk>/update/', BorrowerUpdate.as_view(), name='borrower-update'),
    path('borrower/<slug:pk>/delete/', BorrowerDelete.as_view(), name='borrower-delete'),



]
