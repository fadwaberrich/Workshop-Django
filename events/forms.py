from django import forms
from users.models import Person
from .models import *

CATEGORY_CHOICES = ( ('Music','Music'),('Sport','Sport'),('Cinema','Cinema'))
class EventForm(forms.Form):
    Title = forms.CharField(label='titre',max_length=150,widget=forms.TextInput(attrs={'class':'form-control','id':"title",'placeholder':"Enter your title here"}))
    Description = forms.CharField(widget=forms.Textarea, max_length=150, required=True)
    ImageEvent = forms.ImageField(label='Image')
    NombreParticipants = forms.IntegerField(label="Number",min_value=0,step_size=1)
    Category=forms.ChoiceField(widget=forms.RadioSelect,choices=CATEGORY_CHOICES)
    DateEvent=forms.DateField(widget=forms.DateInput(attrs={'type':'date','class':'form-control date-input'}))
    Organizer=forms.ModelChoiceField(queryset=Person.objects.all())

class EventModelForm(forms.ModelForm):
    class Meta:
        model=Event
        fields="__all__"
        exclude=['state']
        help_texts={
            'title':'YOUR EVENT TITLE HERE',
            'Description':'WRITE YOUR DESCRIPTION HERE !'
        }
    DateEvent = forms.DateField(
        initial=date.today,
        widget=forms.DateInput(
        attrs={
        'type':'date',
        'class':'form-control date-input'
        }
        )
    )