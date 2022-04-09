from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import GeeksModel


class IndexView(ListView):
    model = GeeksModel
    template_name = 'index.html'
    queryset = GeeksModel.objects.all()
    context_object_name = 'dataset'


class DetailItemView(DetailView):
    model = GeeksModel
    template_name = 'detail_view.html'
    context_object_name = 'dataset'


class CreateItemView(CreateView):
    model = GeeksModel
    template_name = 'create_view.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('index')


class UpdateItemView(UpdateView):
    model = GeeksModel
    template_name = 'update_view.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('index')


class DeleteItemView(DeleteView):
    model = GeeksModel
    template_name = 'delete_view.html'
    success_url = reverse_lazy('index')
