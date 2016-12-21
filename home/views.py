from django.shortcuts import render
from home.models import Home, Aviso, Dica


# Create your views here.
def index(request):
    home = Home.objects.all()
    dica = Dica.objects.all()
    aviso = Aviso.objects.all()
    context = {
        "home": home,
        "dica": dica,
        "aviso": aviso
    }
    return render(request, 'index.html', context)

def comochegar(request):
    return render(request, 'comochegar.html')

