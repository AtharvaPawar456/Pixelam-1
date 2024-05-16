from django.contrib import admin

from .models import UserAccountDetails, ChatsData, MyModel

# # Register your models here.

admin.site.register(UserAccountDetails)
admin.site.register(ChatsData)
admin.site.register(MyModel)