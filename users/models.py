from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    first_name = models.CharField("el nombre de la persona",max_length=50)
    last_name = models.CharField("el apellido de la persona",max_length=50)
    cars = models.ManyToManyField('Car',verbose_name='los carros del usuario')

STATUS_CHOICES = (
    ('R','Reviewed'),
    ('N','Not Reviwed'),
    ('E','Error'),
    ('A','Accepted')
)

class Website(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(unique=True)
    release_date = models.DateField()
    rating = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) #dueño de la pagina, el dueño es uno de los user

    #aqui hemos creado un metodo nuevo, que controla que website fue creado esta semana
    def was_released_last_week(self):
        if self.release_date < datetime.date(2022,6,14):
            return 'Released before last week'
        else:
            return 'Released this week'
    #Propiedades de django
    @property
    def get_full_name(self):
        return f"Este es el nombre completo del sitio web: {self.name}"

    #Metodo que hara referencia al modelo Website cuando se llame a este
    def __str__(self):
        return self.name
    #metodo que hara referencia a un campo con un ruta absoluta
    def get_absolute_url(self):
        return f"/website/{self.id}"

    #metodo guardar
    def save(self,*args,**kwargs):
        print('Estamos gurdando')
        super().save(self,*args,**kwargs)


    class Meta:
        ordering = ['rating']
        verbose_name = 'La Pagina Web'
        verbose_name_plural = 'Las Paginas Webs'

class Car(models.Model):
    name = models.CharField(max_length=50, primary_key=True)