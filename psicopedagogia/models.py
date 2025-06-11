from django.db import models


class CicloAcademico(models.Model):
    ESTADO_CHOICES = (
        ('activo', 'Activo'),
        ('archivado', 'Archivado'),
    )
    nombre = models.CharField(max_length=10, unique=True)  # Ejemplo: 2025-1
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activo')

    def __str__(self):
        return self.nombre


class Evento(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='eventos/', blank=True, null=True)  # Opcional
    es_destacado = models.BooleanField(default=False)  # 🔹 Nuevo campo
    link_formulario = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class InstanciaEventoCiclo(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='instancias')
    ciclo_academico = models.ForeignKey(CicloAcademico, on_delete=models.CASCADE, related_name='instancias_evento')

    def __str__(self):
        return f"{self.evento.nombre} ({self.ciclo_academico.nombre})"


class MiembroPsicopedagogia(models.Model):
    nombre = models.CharField(max_length=255)
    frase = models.TextField()
    foto = models.ImageField(upload_to='psicopedagogia/')

    def __str__(self):
        return self.nombre

class ImagenGeneralNosotros(models.Model):
    imagen = models.ImageField(upload_to='nosotros/')
    actualizado_en = models.DateTimeField(auto_now=True)  # Para saber cuándo se actualizó

    def __str__(self):
        return f"Imagen actualizada en {self.actualizado_en}"

class FotoEvento(models.Model):
    instancia = models.ForeignKey(InstanciaEventoCiclo, on_delete=models.CASCADE, related_name='fotos')
    imagen = models.ImageField(upload_to='galeria_eventos/')

    def __str__(self):
        return f"Foto de {self.instancia}"

class ArchivoInscritos(models.Model):
    instancia = models.ForeignKey(InstanciaEventoCiclo, on_delete=models.CASCADE, related_name='archivos_inscritos')
    archivo = models.FileField(upload_to='archivos_inscritos/')

    def __str__(self):
        return f"Archivo de {self.instancia}"

class CategoriaDeporte(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class EquipoCopaTecsup(models.Model):
    nombre_equipo = models.CharField(max_length=255)
    foto_equipo = models.ImageField(upload_to='equipos/', blank=True, null=True)
    instancia = models.ForeignKey(InstanciaEventoCiclo, on_delete=models.CASCADE, related_name='equipos')
    categoria = models.ForeignKey(CategoriaDeporte, on_delete=models.SET_NULL, null=True, related_name='equipos')

    def __str__(self):
        return self.nombre_equipo



