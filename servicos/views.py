# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Servico, CategoryServico, ImageServico


class ListarListView(generic.ListView):
    model = CategoryServico
    template_name = 'servicos/lista.html'
    context_object_name = 'object_list'


    def get_context_data(self, **kwargs):
        context = super(ListarListView, self).get_context_data(**kwargs)
        context['capa'] = ImageServico.objects.all()
        return context


listar = ListarListView.as_view()


class CategoryListView(generic.ListView):
    template_name = 'servicos/descricao.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Servico.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(CategoryServico, slug=self.kwargs['slug'])
        context['capa'] = ImageServico.objects.all()
        return context

category = CategoryListView.as_view()


def servico(request, slug):
    servico = Servico.objects.get(slug=slug)
    context = {
        'servico': servico
    }
    return render(request, 'servicos/slide-servicos.html', context)



