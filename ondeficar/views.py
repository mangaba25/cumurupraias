# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import OndeFicar, CategoryOndeFicar, ImageOndeficar

# Create your views here.
class ListarListView(generic.ListView):
    model = OndeFicar
    template_name = 'ondeficar/lista.html'
    context_object_name = 'object_list'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(ListarListView, self).get_context_data(**kwargs)
        context['capa'] = ImageOndeficar.objects.all()
        return context


listar = ListarListView.as_view()

class CategoryListView(generic.ListView):
    template_name = 'ondeficar/descricao.html'
    context_object_name = 'object_list'
    paginate_by = 8

    def get_queryset(self):
        return OndeFicar.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(CategoryOndeFicar, slug=self.kwargs['slug'])
        context['capa'] = ImageOndeficar.objects.all()
        return context

category = CategoryListView.as_view()

def ondeficar(request, slug):
    ondeficar = OndeFicar.objects.get(slug=slug)
    context = {
        'ondeficar': ondeficar
    }
    return render(request, 'ondeficar/slide.html', context)

    capa = ImageOndecomer.objects.all()
