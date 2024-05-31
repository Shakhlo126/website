from django.contrib import admin
from .models import (Users,
                     Vd_lessons,
                     Client,
                     Payment,
                     About,
                     Team,
                     Web_sites,
                     Web_images)
# Register your models here.

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email')
    search_fields = ('id', 'username', 'email')
    list_filter = ('username', 'email')


admin.site.register(Vd_lessons)
admin.site.register(Client)
admin.site.register(Payment)
admin.site.register(About)
admin.site.register(Team)
admin.site.register(Web_sites)
admin.site.register(Web_images)