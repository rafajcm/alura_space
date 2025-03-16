from gc import get_objects

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from galeria.models import Fotografia
# from django.views import View

def index(request):
    # fotografias = Fotografia.objects.all()
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    return render(request, template_name='galeria/index.html', context={"cards":fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, template_name='galeria/imagem.html', context={"fotografia":fotografia})

# class ViewGaleria(View):
#     def get(self, request):
#         # Verifica o nome da rota para decidir qual template renderizar
#         if request.path == '/imagem/':
#             # Renderiza o template para a rota de imagem
#             return render(request, 'galeria/imagem.html')
#         else:
#             # Renderiza o template padrão para a rota inicial
#             return render(request, 'galeria/index.html')

