from django.shortcuts import render
from django.views import View

class ViewGaleria(View):
    def get(self, request):
        # Verifica o nome da rota para decidir qual template renderizar
        if request.path == '/imagem/':
            # Renderiza o template para a rota de imagem
            return render(request, 'galeria/imagem.html')
        else:
            # Renderiza o template padrão para a rota inicial
            return render(request, 'galeria/index.html')

