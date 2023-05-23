from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.core.exceptions import ValidationError
from datetime import date
from users.models import Person
# Create your models here.


def less_date(dateEvent):
    today = date.today()
    if dateEvent < today :
         raise ValidationError('Please check your "Date event" it shouldn t be less than today') 


class Event(models.Model):

    Title =models.CharField("Title", default="",max_length=250)

    Description =models.TextField("Description", default="",max_length=250)

    State =models.BooleanField(default=False)

    ImageEvent =models.ImageField(upload_to='images/',blank=True)

    NombreParticipants =models.IntegerField(default=0)

    CATEGORY_CHOICES = ( ('Music','Music'),('Sport','Sport'),('Cinema','Cinema'))
    Category =models.CharField("Category",choices=CATEGORY_CHOICES,max_length=10)

    DateEvent =models.DateField(validators=[less_date])

    CreatedAt =models.DateField(auto_now_add=True)

    UpdatedAt =models.DateField(auto_now=True)
    # controle : donne commmentaire
    Organizer = models.ForeignKey(Person,on_delete=models.CASCADE)

    participants = models.ManyToManyField (
        Person, #esm l table li m3a l relation

        related_name="participations", #esm l attribut fel event

        through="Participation" #nom de la table intermediaire
    )

def __str__(self):
    return self.title #to string __XX__ : fonction magic ( str to define string ) 

class Participation(models.Model):
    person =models.ForeignKey(Person,on_delete=models.CASCADE) # fk 
    event =models.ForeignKey(Event,on_delete=models.CASCADE) # fk
    datePart =models.DateField(auto_now=True) # attribut partagé
    # les deux id mte3 les deux tables 
    class Meta:
        unique_together = ('person','event') # une personne ne peut pas participer a pluseirs events a la fois
        verbose_name_plural='Participations' # pas obligatoire ( ya3ti esm fel cas plural )
    #class meta : meta donnee 
