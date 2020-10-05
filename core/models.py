from django.db import models


class Curso(models.Model):
    nivel=models.CharField(max_length=2)
    paralelo = models.CharField(max_length=2)

    def __str__(self):
        return '%s %s' % (self.nivel, self.paralelo)

class Estudiante(models.Model):
    Nombre = models.CharField(max_length=200)
    Apellido = models.CharField(max_length=200)
    Edad = models.IntegerField(default=10)
    Email = models.EmailField(default="@gmail.com")
    Sexo = models.CharField(max_length=1)
    Curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    Cedula=models.CharField(max_length=200)
    Fecha_Nacimiento=models.CharField(max_length=200)
    Direccion=models.CharField(max_length=200)
    N_de_Telefono=models.CharField(max_length=200)
    Codigo_Matricula=models.CharField(max_length=200)
    user = models.CharField(max_length=15)
    user_mod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table="core_estudiante"
        verbose_name="estudiante"
        verbose_name_plural="estudiantes"
        ordering = ["Nombre"]

    def __str__(self):
        return self.Apellido + '' + self.Nombre

class Enfermedad(models.Model):
    Tipo= models.CharField(max_length=300)
    Explique= models.CharField(max_length=200)
    Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default=None)

    class Meta:
         db_table = "core_Enfermedad"
         verbose_name = "Enfermedad"
         verbose_name_plural = "Enfermedades"
         ordering = ["Tipo"]

    def _str_(self):
        return self.Tipo

class Familia(models.Model):
    Nombre_Madre = models.CharField(max_length=200)
    Nombre_Padre = models.CharField(max_length=200)
    Apellido_Padre = models.CharField(max_length=200)
    Apellido_Madre = models.CharField(max_length=200)
    Ocupacion_Padre= models.CharField(max_length=200)
    Ocupacion_Madre = models.CharField(max_length=200)
    Trabaja_Donde_Madre= models.CharField(max_length=200)
    Trabaja_Donde_Padre = models.CharField(max_length=200)
    Estado_Civil_Madre = models.CharField(max_length=200)
    Estado_Civil_Padre = models.CharField(max_length=200)
    Vive_con_el_Niño_Madre=models.CharField(max_length=200)
    Vive_con_el_Niño_Padre = models.CharField(max_length=200)
    Telefonos_Madre=models.CharField(max_length=200)
    Telefonos_Padre = models.CharField(max_length=200)
    Direccion_Madre= models.CharField(max_length=200)
    Direccion_Padre= models.CharField(max_length=200)
    Instruccion_Madre= models.CharField(max_length=200)
    Instruccion_Padre= models.CharField(max_length=200)
    Tutor= models.CharField(max_length=200)
    user = models.CharField(max_length=15)
    user_mod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE,default=None)

    class Meta:
        db_table = "core_Familia"
        verbose_name = "Familia"
        verbose_name_plural = "Familias"
        ordering = ["Nombre_Madre"]

    def __str__(self):
        return self.Nombre_Madre

class Formulario(models.Model):
    EDUCACION_CHOICES = (
        ('A', 'Agregar'),
        ('SP', 'Solo Padres'),
        ('PM', 'Mi Padre y Mi Madre'),
        ('SM', 'Solo Madre'),
        ('SP', 'Solo Padre'),
        ('OTRO', 'Otra Persona'),
    )
    Educacion_Formulario = models.CharField(max_length=100, choices=EDUCACION_CHOICES, default="A")

    RELACION_CHOICES = (
        ('A', 'Agregar'),
        ('MCD', 'Mayormente Conversan y Deciden en Conjunto'),
        ('NHC', 'No hay comunicacion'),
        ('NHC', 'Solo habla lo necesario'),
        ('CCT', 'Cuando conversan terminan discutiendo'),
    )
    Relacion_Formulario= models.CharField(max_length=100, choices=RELACION_CHOICES, default="A")

    CONDUCTA_CHOICES = (
        ('A', 'Agregar'),
        ('G', 'Gritan'),
        ('G', 'Golpean'),
        ('LQLM', 'Le quitan lo que mas le gusta'),
        ('LA', 'Le llaman la atencion'),
        ('NLD', 'No le dicen'),
    )
    Conducta_Formulario = models.CharField(max_length=100, choices=CONDUCTA_CHOICES, default="A")

    INTERNET_CHOICES = (
        ('A', 'Agregar'),
        ('G', 'Para Chatiar'),
        ('G', 'Para Jugar'),
        ('LQLM', 'Le quitan lo que mas le gusta'),
        ('LA', 'Para hacer tarea'),
        ('NLD', 'No uso Internet'),
    )
    Internet_Formulario = models.CharField(max_length=100, choices=INTERNET_CHOICES, default="A")

    TRANSPORTE_CHOICES = (
        ('A', 'Agregar'),
        ('TP', 'Transporte Publico'),
        ('TP', 'Transporte Privado'),
        ('TE', 'Transporte Escolar'),
        ('ST', 'Sin Transporte'),
    )
    Transporte_Formulario = models.CharField(max_length=100, choices=TRANSPORTE_CHOICES, default="A")
    Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE,default=None)

    class Meta:
        db_table = "core_Formulario"
        verbose_name = "Formulario"
        verbose_name_plural = "Formularios"
        ordering = ["Educacion_Formulario"]

    def __str__(self):
        return self.Educacion_Formulario

class Retiro(models.Model):
    Nombre = models.CharField(max_length=200)
    Apellido = models.CharField(max_length=200)
    Edad = models.IntegerField(default=10)
    Cedula=models.CharField(max_length=200)
    Direccion=models.CharField(max_length=200)
    N_de_Telefono=models.CharField(max_length=200)
    user = models.CharField(max_length=15)
    user_mod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    Estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE,default=None)

    class Meta:
        db_table = "core_Retiro"
        verbose_name = "Retiro"
        verbose_name_plural = "Retiros"
        ordering = ["Nombre"]

    def __str__(self):
        return self.Nombre

class Estudiante_Familia_Enfermedad_Formulario_Retiro(models.Model):
        estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default=None)
        familia = models.ForeignKey(Familia, on_delete=models.CASCADE, default=None)
        enfermedad = models.ForeignKey(Enfermedad, on_delete=models.CASCADE, default=None)
        formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, default=None)
        retiro = models.ForeignKey(Retiro, on_delete=models.CASCADE, default=None)

        class Meta:
            db_table = "core_Es_Fa_En_Fo_Re"
            verbose_name = "Estudiante_Familia_Enfermedad_Formulario_Retiro"
            verbose_name_plural = "Estudiantes_Familias_Enfermedades_Formularios_Retiros"
            ordering = ["estudiante"]

        def str(self):
            return self.estudiante