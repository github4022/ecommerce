from django.views.generic import *
from django.urls import reverse_lazy
from .models import Category
from django.contrib.messages.views import SuccessMessageMixin


class CategoryListView(ListView):
    model = Category
    template_name = 'store/category_list.html'
    context_object_name = 'category_list'


class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    # fields = '__all__'
    fields = ['name', 'description', 'image',]
    template_name = 'store/category_create.html'
    success_message = 'Category added successfully!'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'store/category_detail.html'
    context_object_name = 'category'


class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'store/category_update.html'


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category_list')
    context_object_name = 'category'
