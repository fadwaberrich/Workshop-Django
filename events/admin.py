from django.contrib import admin , messages
from django.utils import timezone
from .models import Event,Participation 
# Register your models here.
###################################### HOMEWORK DATE FILTER ######################################################
class DatesEventFilter(admin.DateFieldListFilter):
    title = 'DateEvent'
    parameter_name = 'DateEvent'
    def lookups(self, request, model_admin):
        return (
            ('Today', ('Today')),
            ('This Week', ('This_Week')),
            ('This Month', ('This_Month')),
            ('This Year', ('This_Year')),
        )

    def queryset(self, request, queryset):
        today = timezone.now.today()
        #or simply we can use today = date.today() 
        if self.value() == 'Today':
            return queryset.filter(DateEvent__exact=today)
        elif self.value() == 'This Week':
            return queryset.filter(DateEvent__week=today.isocalendar()[1])
        elif self.value() == 'This Month':
            return queryset.filter(DateEvent__month=today.month)
        elif self.value() == 'This Year':
            return queryset.filter(DateEvent__year=today.year)
        else:
            return queryset
###############################################################################################################
class ParticipantFilter(admin.SimpleListFilter):
    title = 'Number of Participants'
    parameter_name = 'NombreParticipants'

    def lookups(self, request, model_admin):
        return (
            ('0', ('No Participants')),
            ('more', ('There are Participants'))
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(NombreParticipants__exact=0)
        if self.value() == 'more':
            return queryset.filter(NombreParticipants__gt=0)

class ParticipationInline(admin.TabularInline): #we can use TabularInline (tableau ) ou stackInline
        model = Participation
        extra = 1 #  est un paramètre qui définit le nombre de formulaires supplémentaires à afficher 
        classes = ['collapse']
        can_delete = True #champs delete 
        readonly_fields = ('datePart',) #affiche ken date participation

def set_state(ModelAdmin,request,queryset):
    rows = queryset.update(State= True)
    if(rows ==1):
        msg ="One event was"
    else:
        msg = f"{rows} events were" #if more than 2 events are selected
    messages.success(request, message='%s successfully accepted' % msg)

set_state.short_description = "Accept" # elle sera afficher fel liste state sinon state sera affiché par defaut

class EventAdmin(admin.ModelAdmin):
    def unset_state(self, request ,queryset):
        rows_filter = queryset.filter(State= False)
        if rows_filter.count() > 0:
            messages.error(request,message=f"{rows_filter.count()} are already refused")
        else:
            rows =queryset.update(State=False)
            if(rows==1):
                msg = "One event was "
            else:
                msg = f"{rows} events were" #if more than 2 events are selected 
            messages.success(request, message='%s successfully refused' % msg)
    unset_state.short_description = "Refuse"
    actions = [set_state,"unset_state","queryset"]
    actions_on_bottom = True
    actions_on_top = True
    inlines=[
        ParticipationInline
    ]
    
    list_per_page = 20

    list_display =(
        'Title',
        'Category',
        'State', #liste affiché dans la table evnt
        'DateEvent'
    )
    list_filter=(
        
        ParticipantFilter,
        'Category',
        'State',
        'DateEvent',
    )
    date_hierarchy = 'DateEvent'
    ordering = ('Title','-DateEvent')
    search_fields=[
        'Title',
        'Category'
    ]
    readonly_fields=('CreatedAt','UpdatedAt')
    autocomplete_fields=['Organizer']
    fieldsets = (
        (
            'State',
            {
                'fields': ('State',)
            }
        ),
        (
            'About',
            {
                'classes': ('collapse',),
                'fields': (
                    'Title',
                    'ImageEvent',
                    'Category',
                    'Organizer',   
                    'NombreParticipants',
                    'Description',
                ),
            }
        ),
        (
            'Dates',
            {
                'fields': (
                    (
                        'DateEvent',
                        'CreatedAt',
                    ),
                )
            }
        ),
    )
admin.site.register(Event,EventAdmin)
admin.site.register(Participation)