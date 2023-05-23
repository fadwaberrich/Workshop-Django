from django.contrib import admin
from .models import Person
from django.utils import timezone
# Register your models here.

# admin.site.register(Person)

####################################### FILTER OF STAFF STATUS ( staff = False/no | superuser = True/yes ######################################
class StaffFilter(admin.SimpleListFilter):
    title = 'Staff status'
    parameter_name = 'is_staff'

    def lookups(self, request, model_admin):
        return (
            ('Yes', ('Yes, in staff !')),
            ('No', ('No, not in staff !')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'Yes':
            return queryset.filter(is_staff=True)
        if self.value() == 'No':
            return queryset.filter(is_staff=False)

###############################################################################################################################################


###################################################### FILTER By Date of joining of the user ###################################################

class JoinDateFilter(admin.SimpleListFilter):
    title = 'Join date'
    parameter_name = 'date_joined'

    def lookups(self, request, model_admin):
        return (
            ('Today', ('Today')),
            ('Last 7 days', ('Last 7 days')),
            ('Last 30 days', ('Last 30 days')),
        )

    def queryset(self, request, queryset):
        today = timezone.now().date()
        if self.value() == 'Today':
            return queryset.filter(date_joined__day=today.day, date_joined__month=today.month, date_joined__year=today.year)
        if self.value() == 'Last 7 days':
            return queryset.filter(date_joined__gte=today-timezone.timedelta(days=7), date_joined__lt=today)
        if self.value() == 'Last 30 days':
            return queryset.filter(date_joined__gte=today-timezone.timedelta(days=30), date_joined__lt=today)

            
###############################################################################################################################################

class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'date_joined',
    )
    ordering = ('email',)
    search_fields = [
        'CIN',
        'email',
    ]
    fieldsets = (
        (
            'Personal Info',
            {
                'fields': (
                    'CIN',
                    'email',
                    'username',
                    'first_name',
                    'last_name',
                    'is_staff'
                ),
            }
        ),
    )
    list_filter = (
        StaffFilter,
        'date_joined'
    )


admin.site.register(Person, PersonAdmin)
