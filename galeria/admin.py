from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda','categoria','publicada')
    list_display_links = ('id', 'nome','categoria')
    search_fields = ('nome',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 25   # 25, 50 e 100 item por página

admin.site.register(Fotografia, ListandoFotografias)
