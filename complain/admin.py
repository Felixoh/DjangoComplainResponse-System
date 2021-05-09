from django.contrib import admin
from .models import Complain,Response

class ComplainAdmin(admin.ModelAdmin):
    list_display = ("location","complains","comment","Comment_rating")
    list_filter = ("date_created",)
    search_fields = ("location__startswith","Comment_rating",)
    
class ResponseAdmin(admin.ModelAdmin):
    list_display = ("comment","reply","status")
    list_filter = ("date_created",)
    search_fields = ("reply",)
# Register your models here 
#admin.site.unregister(Response)
#admin.site.unregister(Complain)

admin.site.register(Complain,ComplainAdmin)
admin.site.register(Response,ResponseAdmin)

admin.site.site_title = 'Admin Page'
admin.site.site_header = 'CMS AdminPage'