from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class TipoUsuario(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    imagen = models.ImageField(upload_to='usuarios', null=True, blank=True, help_text='Imagen del usuario')
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE)    
    ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    direccion = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.username})"

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    pais_origen = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.nombre

class TipoGuitarra(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class SubModelo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre


class Guitarra(models.Model):
    tipo_guitarra = models.ForeignKey(TipoGuitarra, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo,on_delete=models.CASCADE)
    sub_modelo = models.ForeignKey(SubModelo, verbose_name=("Submodelo"), on_delete=models.CASCADE)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    ano_fabricacion = models.IntegerField(null=True, blank=True, help_text='Año de fabricación de la guitarra')
    tipo_cuerpo = models.CharField(max_length=50, null=True, blank=True, help_text='Tipo de cuerpo de la guitarra')
    material_diapason = models.CharField(max_length=50, null=True, blank=True, help_text='Material del diapasón de la guitarra')
    numero_trastes = models.IntegerField(null=True, blank=True, help_text='Número de trastes de la guitarra')
    color = models.CharField(max_length=50, null=True, blank=True, help_text='Color de la guitarra')
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, help_text='Peso de la guitarra')
    imagen = models.ImageField(upload_to='guitarras', null=True, blank=True, help_text='Imagen de la guitarra')
    
    def __str__(self):
        return self.modelo

