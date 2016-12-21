# coding=utf-8


from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Artesanato, CategoryArtesanato, ImageArtesanato


class ListarListView(generic.ListView):
    model = Artesanato
    template_name = 'artesanatos/lista.html'
    context_object_name = 'object_list'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super(ListarListView, self).get_context_data(**kwargs)
        context['capa'] = ImageArtesanato.objects.all()
        return context


listar = ListarListView.as_view()

class CategoryListView(generic.ListView):
    template_name = 'artesanatos/descricao.html'
    context_object_name = 'object_list'
    paginate_by = 8

    def get_queryset(self):
        return Artesanato.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(CategoryArtesanato, slug=self.kwargs['slug'])
        return context

category = CategoryListView.as_view()

def artesanato(request, slug):
    artesanato = Artesanato.objects.get(slug=slug)
    context = {
        'artesanato': artesanato
    }
    return render(request, 'artesanatos/slide.html', context)



