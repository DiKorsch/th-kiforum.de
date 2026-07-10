from django.contrib import admin

from api.models import Organisation, ContactPerson, Demonstrator

class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'website')

class ContactPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')

class DemonstratorAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'key', 'organisation', 'contact_person')

admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(ContactPerson, ContactPersonAdmin)
admin.site.register(Demonstrator, DemonstratorAdmin)

# Register your models here.
