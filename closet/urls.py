from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
    path('logout', logout_view, name='logout'),
    path('closet/', closet, name='closet'),
    path('closet/create/item', createItem, name='createItem'),
    path('closet/edit/item/<int:id>', editItem, name='editItem'),
    path('closet/create/category', createCategory, name='createCategory'),
    path('closet/delete/<int:id>', deleteClothingItem, name='deleteClothingItem'),
    path('looks', looks, name='looks'),
    path('looks/create', createLook, name='createLook'),
    path('looks/<int:id>', look, name='look'),
    path('looks/delete/<int:id>', deleteLook, name='deleteLook'),
    path('looks/edit/<int:id>', editLook, name='editLook'),
]