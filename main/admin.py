#! coding: utf-8

from django.contrib import admin
from main.models import Photo, Settings, Items, TypesRooms, Categories

class PhotoInline(admin.TabularInline):
    model = Photo

class CategoriesInline(admin.TabularInline):
    model = Categories


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('name', 'about_descript', 'primary_number', 'additional_number', 'address', 'email', 'vk_url', 'instagram_url', 'twitter_url', 'fb_url', 'active')
    fieldsets = [
        ('Общая информация', {'fields': ['name', 'about_descript']}),
<<<<<<< HEAD
<<<<<<< HEAD
=======
        ('Настройка главной страницы', {'fields': ['random_discount']}),
=======
        ('Настройка главной страницы', {'fields': ['random_discount', 'hit_count']}),
>>>>>>> ba49513 (Добавил отображение хитов продаж на главной странице)
        ('Настройка каталога', {'fields': ['items_page']}),
>>>>>>> 68f6df1 (Добавил отображение поля random_discount в админке)
        ('Контакты', {'fields': ['primary_number', 'additional_number', 'email', 'address']}),
        ('Ссылки на социальные сети', {'fields': ['vk_url', 'instagram_url', 'twitter_url', 'fb_url']}),
        ('Техническая информация', {'fields': ['active']}),
    ]

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost_of', 'discount', 'main_photo', 'room', 'category',)
    inlines = [
        PhotoInline,
    ]
    fieldsets = [
<<<<<<< HEAD
        ('Основное', {'fields': ['name', 'main_photo',]}),
        ('Склад', {'fields': ['cost_of', 'discount',]}),
=======
        ('Основное', {'fields': ['name', 'description', 'factory', 'main_photo',]}),
        ('Склад', {'fields': ['cost_of', 'discount', 'sales',]}),
>>>>>>> ba49513 (Добавил отображение хитов продаж на главной странице)
        ('Номенклатура', {'fields': ['room', 'category',]})
    ]

    def get_categories(self, obj):
        return obj.room.get_categories(self)

@admin.register(TypesRooms)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_categories')
    inlines = [
        CategoriesInline,
<<<<<<< HEAD
=======
    ]

@admin.register(Factories)
class FactoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_url', 'short_description',)
    inlines = [
        ItemsInline,
>>>>>>> ba49513 (Добавил отображение хитов продаж на главной странице)
    ]