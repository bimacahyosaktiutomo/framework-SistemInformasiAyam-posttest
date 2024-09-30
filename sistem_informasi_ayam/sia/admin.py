from django.contrib import admin
from django.contrib.auth.hashers import make_password

# Register your models here.
from .models.overseer import Overseer
from .models.member import Members
from .models.produks import Produks
from .models.hewan_ternak import HewanTernak
from .models.users import Users

class OverseerAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username', 'password', 'priviliege')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        user, created = Users.objects.get_or_create(username=obj.username, defaults= {
            'password': make_password('default_password'),
            'role':Users.OVERSEER
        })
        
        if not created:
            user.role = Users.OVERSEER
            user.save()

admin.site.register(Overseer, OverseerAdmin)

admin.site.register(Members)
admin.site.register(Users)
admin.site.register(Produks)
admin.site.register(HewanTernak)