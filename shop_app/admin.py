from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(shop_admin)
class shopadminAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email',)

@admin.register(shop_user)
class shopuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'sex', 'email', 'face', 'regTime',)

@admin.register(shop_pro)
class shopproAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'old_price', 'is_bestseller', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'desc', 'meta_keywords', 'meta_desc']
    exclude = ('created_at', 'updated_at',)
    prepopulated_fields = {'slug':('name',)}

@admin.register(shop_cat)
class shopcatAdmin(admin.ModelAdmin):
    list_display = ('name', 'proname', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'desc', 'meta_keywords', 'meta_desc']
    exclude = ('created_at', 'updated_at',)
    prepopulated_fields = {'slug':('name',)}

@admin.register(CarItem)
class CarItemAdmin(admin.ModelAdmin):
    list_display = ('car_id','name', 'quantity','total','date_added',)
    list_display_links = ('car_id',)
    # list_per_page每页显示的数据条数
    list_per_page = 20


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_url', 'date_publish','index',)
    list_display_links = ('image_url',)
    list_editable = ('index',)
