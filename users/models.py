from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator,MaxLengthValidator
from django.core.exceptions import ValidationError
# Create your models here.

def is_email_esprit(mail):
    if str(mail).endswith('@esprit.tn')==False:
        raise ValidationError('Please check your email')
        
class Person(AbstractUser):

    CIN =models.CharField("CIN",max_length=250,validators= [RegexValidator(regex='^[0-9]{8}$',message="Numbers Only !")])

    email =models.EmailField("Email",help_text='xx@yy.tn',unique=True,validators=[is_email_esprit])
