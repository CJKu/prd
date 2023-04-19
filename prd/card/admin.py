from django.contrib import admin

# Register your models here.
from .models import PublicCardInfo, PrivateCardInfo

admin.site.register(PublicCardInfo)
admin.site.register(PrivateCardInfo)
