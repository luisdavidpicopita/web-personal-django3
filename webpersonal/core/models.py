from django.db import models

# Create your models here.
class rol (models.Model):
    tipo = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=300, null=False, blank=False)

class usuario (models.Model):
    nc = models.PositiveBigIntegerField(null=False, blank=False)
    p_nombre = models.CharField(max_length=50, null=False, blank=False)
    s_nombre = models.CharField(max_length=50, null=False, blank=True)
    p_apellido = models.CharField(max_length=50, null=False, blank=True)
    m_apellido = models.CharField(max_length=50, null=False, blank=True)
    correo = models.EmailField(null=False, blank=False)
    tipo = models.ForeignKey(rol, on_delete=models.CASCADE)

class lugar (models.Model):
    referencia = models.CharField(max_length=100, null=False, blank=False)

class categoria (models.Model):
    tipo = models.CharField(max_length=30, null=False, blank=False)
    descripcion = descripcion = models.CharField(max_length=300, null=False, blank=False)

class local (models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=300, null=False, blank=False)
    foto = models.ImageField(null=False, blank=False)
    hora_aper = models.TimeField(null=False, blank=False)
    hora_cier = models.TimeField(null=False, blank=False)
    dueño = models.ForeignKey(usuario, on_delete=models.CASCADE, null=False, blank=False)
    lugar = models.ForeignKey(lugar, on_delete=models.CASCADE, null=False, blank=False)
    categoria = models.ManyToManyField(categoria)

class comida (models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    descripcion = models.CharField(max_length=300, null=False, blank=False)
    foto = models.ImageField(null=False, blank=False)
    precio = models.DecimalField(null=False, blank=False, max_digits=4, decimal_places=2)
    local = models.ForeignKey(lugar, on_delete=models.CASCADE)

class reseña (models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE, null=False, blank=False)
    comida = models.ForeignKey(comida, on_delete=models.CASCADE, null=False, blank=False)
    comentaio = models.CharField(max_length=300, null=False, blank=False)
    calificacion = models.PositiveSmallIntegerField(null=False, blank=False)

