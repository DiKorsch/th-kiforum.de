from django.contrib import admin

from api.models import Organisation, ContactPerson, Demonstrator, Content

class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'website')

class ContactPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')

class DemonstratorAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'key', 'organisation', 'contact_person')

class ContentAdmin(admin.ModelAdmin):
    list_display = ("name", "content_preview")

    def content_preview(self, obj: Content):
        if len(obj.content) < 100:
            return obj.content
        return f"{obj.content[:100]}..."

admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(ContactPerson, ContactPersonAdmin)
admin.site.register(Demonstrator, DemonstratorAdmin)
admin.site.register(Content, ContentAdmin)

# Register your models here.
