# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import OndeComer, CategoryOndeComer, ImageOndecomer


class ListarListView(generic.ListView):
    model = OndeComer
    template_name = 'ondecomer/lista.html'
    context_object_name = 'object_list'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(ListarListView, self).get_context_data(**kwargs)
        context['capa'] = ImageOndecomer.objects.all()
        return context

listar = ListarListView.as_view()

class CategoryListView(generic.ListView):
    template_name = 'ondecomer/descricao.html'
    context_object_name = 'object_list'
    paginate_by = 8

    def get_queryset(self):
        return OndeComer.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(CategoryOndeComer, slug=self.kwargs['slug'])
        context['capa'] = ImageOndecomer.objects.all()
        return context

category = CategoryListView.as_view()

def ondecomer(request, slug):
    ondecomer = OndeComer.objects.get(slug=slug)
    context = {
        'ondecomer': ondecomer
    }
    return render(request, 'ondecomer/slide.html', context)






