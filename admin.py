from django.contrib import admin
from goods.models import Goods


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name','price','picture','desc']

admin.site.register(Goods,GoodsAdmin)


