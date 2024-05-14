from django.contrib import admin
from core.models import rol
from core.models import usuario
from core.models import lugar
from core.models import categoria
from core.models import local
from core.models import comida
from core.models import reseña

# Register your models here.
admin.site.register(rol)
admin.site.register(usuario)
admin.site.register(lugar)
admin.site.register(categoria)
admin.site.register(local)
admin.site.register(comida)
admin.site.register(reseña)
