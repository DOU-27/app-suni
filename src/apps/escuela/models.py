from django.db import models
from django.urls import reverse
from django.utils import timezone
from apps.main.models import Municipio, Coordenada
from apps.main.utils import get_telefonica
from apps.mye.models import Cooperante, Proyecto, Solicitud


class EscArea(models.Model):
    area = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'

    def __str__(self):
        return self.area


class EscJornada(models.Model):
    """
    Description: Jornada de la escuela
    """
    jornada = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Jornada'
        verbose_name_plural = 'Jornadas'

    def __str__(self):
        return self.jornada


class EscModalidad(models.Model):
    """
    Description: Modalidad de la escuela
    """
    modalidad = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Modalidad'
        verbose_name_plural = 'Modalidades'

    def __str__(self):
        return self.modalidad


class EscNivel(models.Model):
    """
    Description: Nivel de la escuela
    """
    nivel = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveles'

    def __str__(self):
        return self.nivel


class EscPlan(models.Model):
    """
    Description: Plan de la escuela (diario, fin de semana, etc.)
    """
    plan = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'

    def __str__(self):
        return self.plan


class EscSector(models.Model):
    """
    Description: Sector de la escuela (oficial, privado, etc.)
    """
    sector = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'

    def __str__(self):
        return self.sector


class EscStatus(models.Model):
    """
    Description: Status de la escuela (Abierta, cerrada)
    """
    status = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statues'

    def __str__(self):
        return self.status


class Escuela(models.Model):
    """
    Description: Escuela
    """
    codigo = models.CharField(max_length=15, unique=True)
    distrito = models.CharField(max_length=10, null=True, blank=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=250)
    direccion = models.TextField()
    telefono = models.CharField(max_length=12, null=True, blank=True)
    nivel = models.ForeignKey(EscNivel, on_delete=models.PROTECT)
    sector = models.ForeignKey(EscSector, on_delete=models.PROTECT)
    area = models.ForeignKey(EscArea, on_delete=models.PROTECT)
    status = models.ForeignKey(EscStatus, on_delete=models.PROTECT)
    modalidad = models.ForeignKey(EscModalidad, on_delete=models.PROTECT)
    jornada = models.ForeignKey(EscJornada, on_delete=models.PROTECT)
    plan = models.ForeignKey(EscPlan, on_delete=models.PROTECT)
    mapa = models.ForeignKey(Coordenada, null=True, blank=True)

    cooperante_asignado = models.ManyToManyField(
        Cooperante,
        through='mye.EscuelaCooperante',
        blank=True)
    proyecto_asignado = models.ManyToManyField(
        Proyecto,
        through='mye.EscuelaProyecto',
        blank=True)

    class Meta:
        verbose_name = "Escuela"
        verbose_name_plural = "Escuelas"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('escuela_detail', kwargs={'pk': self.id})

    def get_poblacion(self):
        if self.poblaciones.count() > 0:
            return self.poblaciones.latest('fecha').total_alumno
        else:
            return None
    poblacion = property(get_poblacion)

    def es_equipada(self):
        return True if self.equipamiento.count() > 0 else False
    equipada = property(es_equipada)

    def tiene_solicitud(self):
        return Solicitud.objects.filter(escuela=self).count() > 0

    def get_ficha_escolar(self):
        return 'https://public.tableau.com/views/1-FichaEscolarDatosGenerales/DatosGenerales?CODUDI={}'.format(self.codigo)


class EscContactoRol(models.Model):
    """
    Description: Rol para el contacto de escuela
    """
    rol = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Rol de contacto"
        verbose_name_plural = "Roles de contacto"

    def __str__(self):
        return self.rol


class EscContacto(models.Model):
    escuela = models.ForeignKey(Escuela, related_name="contacto")
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rol = models.ForeignKey(EscContactoRol, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos de escuela"

    def __str__(self):
        return self.nombre + " " + self.apellido


class EscContactoTelefono(models.Model):
    contacto = models.ForeignKey(EscContacto, related_name="telefono", null=True)
    telefono = models.IntegerField()

    def get_empresa(self):
        return get_telefonica(self.telefono)
    empresa = property(get_empresa)

    def __str__(self):
        return str(self.telefono)


class EscContactoMail(models.Model):
    """
    Description: Correo de contacto
    """
    contacto = models.ForeignKey(EscContacto, related_name="mail", null=True)
    mail = models.EmailField(max_length=125)

    def __str__(self):
        return self.mail


class EscPoblacion(models.Model):
    escuela = models.ForeignKey(Escuela, related_name="poblaciones")
    fecha = models.DateField(default=timezone.now)

    alumna = models.IntegerField(default=0)
    alumno = models.IntegerField(default=0)
    maestra = models.IntegerField(default=0)
    maestro = models.IntegerField(default=0)

    total_alumno = models.IntegerField(null=True, blank=True)
    total_maestro = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Población de escuela"
        verbose_name_plural = "Poblaciones de escuela"

    def __str__(self):
        return str(self.escuela)[:15] + " - " + str(self.fecha)

    def save(self, *args, **kwargs):
        if self.total_alumno is None or self.total_alumno == 0:
            self.total_alumno = self.alumna + self.alumno
        if self.total_maestro is None or self.total_maestro == 0:
            self.total_maestro = self.maestra + self.maestro
        super(EscPoblacion, self).save(*args, **kwargs)
