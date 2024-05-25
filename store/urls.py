from django.urls import path
from .views import *

urlpatterns = [
path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category-list/', CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/<slug:slug>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<slug:slug>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]

