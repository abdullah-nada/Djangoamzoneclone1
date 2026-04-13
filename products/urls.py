from django.urls import path

from .views import productlist, productdetail
urlpatterns = [
    path('',productlist.as_view() ),
    path('<slug:slug>',productdetail.as_view() ),
]
