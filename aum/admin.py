from django.contrib import admin
from .models import *

class ProgramDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'program_group')

    def program_group (self, obj):
        return obj.groupBachelor



# Register your models here.
admin.site.register(HeroBanner)
admin.site.register(ApplyBanner)
admin.site.register(ProgramData,ProgramDataAdmin)
admin.site.register(HeroGlobalData)
admin.site.register(GlobalTextAndTitle)
admin.site.register(BlogGeneral)
admin.site.register(ProgramsGeneral)
admin.site.register(ButtonsGeneral)
admin.site.register(PageGeneral)
admin.site.register(Professor)
admin.site.register(PageBasic)
admin.site.register(NavSetting)
admin.site.register(ContactWebpage)
admin.site.register(NewsletterContact)

admin.site.site_header = "AUM Admin"
admin.site.site_title = "AUM Admin Portal"
admin.site.index_title = "Welcome to AUM Content Manager"

