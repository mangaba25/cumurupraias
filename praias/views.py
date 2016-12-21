# coding=utf-8


from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Praia, CategoryPraia, ImagePraia


class ListarListView(generic.ListView):
    model = Praia
    template_name = 'praias/lista.html'
    context_object_name = 'object_list'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(ListarListView, self).get_context_data(**kwargs)
        context['capa'] = ImagePraia.objects.all()
        return context


listar = ListarListView.as_view()

class CategoryListView(generic.ListView):
    template_name = 'praias/descricao.html'
    context_object_name = 'object_list'
    paginate_by = 8

    def get_queryset(self):
        return Praia.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(CategoryPraia, slug=self.kwargs['slug'])
        return context

category = CategoryListView.as_view()

def praia(request, slug):
    praia = Praia.objects.get(slug=slug)
    context = {
        'praia': praia
    }
    return render(request, 'praias/slide.html', context)
