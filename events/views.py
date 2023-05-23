from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .models import Event
from django.views.generic import ListView, DetailView , CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
# tjr on a du requetes


def homePage(Request):  # esm l fonction dima yabda bel miniscule
    # pour renvoyer un HTML on appel HTMLResponse
    return HttpResponse('<h1>Titlr here</h1>')


def homePage1(request):
    return render(
        request,  # 1éer param tjr request
        'events/homePage.html'  # page html à affiché
        # 3éme param .. context ( non obligatoir )
    )


def listEventsStatic(request):
    list = [
        {
            'title': 'Event 1',
            'description': 'description 1',
            'image': 'image.png'
        },
        {
            'title': 'Event 2',
            'description': 'description 2',
            'image': 'image.png'
        },
        {
            'title': 'Event 3',
            'description': 'description 3',
            'image': 'image.png'
        }
    ]
    return render(
        request,
        'events/listEvents.html',
        {
            'events': list
        }
    )

@login_required(login_url="/users/login")
def listEvents(request):
    list = Event.objects.filter(State=True)  # objects.filter search ...
    return render(
        request,
        'events/listEvents.html',
        {
            'events': list
        }
    )


def detailEvent(request, id):
    event = Event.objects.get(id=id)
    return render(
        request,
        'events/event_detail.html',
        {
            'event': event,
        }
    )


class listEventsViews(ListView):
    model = Event
    template_name = 'events/listEvents.html'
    context_object_name = 'events'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(State=True)
    


class EventDtails(DetailView):
    model = Event


def addEvent(request):
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            Event.objects.create(
                **form.cleaned_data
                # Title=form.cleaned_data.get('title'),
                # Description=form.cleaned_data['Description']
            )
            return redirect('Event_ListEvent_V')
    return render(
        request,
        'events/event_add.html',
        {
            'form': form,
        }
    )


def addEventModel(request):
    form = EventModelForm()
    if request.method == 'POST':
        form = EventModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Event_ListEvent_V')
   
    return render(
        request,
        'events/event_add.html',
        {
            'form': form,
        }
    )
class EventCreateView(CreateView):
    model = Event
    form_class = EventModelForm
    success_url = reverse_lazy('Event_ListEvent_C')
    template_name ='events/event_add.html'
    
def updateEvent(request, id):
    event = get_object_or_404(Event, id=id)
    form = EventModelForm(instance=event)
    
    if request.method == 'POST':
        form = EventModelForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('Event_ListEvent_V')
    
    return render(
        request,
        'events/event_update.html',
        {
            'form': form,
            'event': event,
        }
    )


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventModelForm
    success_url = reverse_lazy('Event_ListEvent_C')
    template_name = 'events/event_update.html'

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/event_delete.html'
    success_url = reverse_lazy('Event_ListEvent_V')

def participate(request, id):
    event = Event.objects.get(id=id)
    person= Person.objects.get(CIN= 11223344)
    if Participation.objects.filter(person=person,event=event).count()==0:
        Participation.objects.create(event=event,person=person)     
        event.NombreParticipants += 1
        event.save()
        messages.add_message(request,messages.SUCCESS,f'your participation to the event : {event.Title} was added ')
    else:
        messages.add_message(request, messages.ERROR,"You are already participated to this event")
    # nb = event.NombreParticipants + 1
    # Event.objects.filter(id=id).update(NombreParticipants=nb)
    # ---sol2---

    return redirect('Event_ListEvent_V')

