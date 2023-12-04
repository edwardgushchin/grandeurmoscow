#! coding: utf-8
from __future__ import unicode_literals

import os
from uuid import uuid1
from django.db import models
from django.conf import settings
from django.template.defaultfilters import truncatechars

def get_file_path(instance, filename):
    result = os.path.join('photos', uuid1().hex)
    if '.' in filename:
        result = '%s.%s' % (result, filename.split('.')[-1])
        return result

#Основные настройки сайта
class Settings(models.Model):
    primary_number = models.CharField(max_length=17, verbose_name='Основной телефон')
    additional_number = models.CharField(max_length=17, verbose_name='Дополнительный телефон')
    name = models.CharField(max_length=50, verbose_name='Название магазина')
    about_descript = models.TextField(verbose_name='Описание')
    address = models.CharField(max_length=500, verbose_name='Адресс офиса')
    email = models.EmailField(verbose_name='Адресс электронной почты')
    vk_url = models.URLField(max_length=500, verbose_name='Ссылка на группу VK')
    instagram_url = models.URLField(max_length=500, verbose_name='Ссылка на Instagram')
    twitter_url = models.URLField(max_length=500, verbose_name='Ссылка на Twitter')
    fb_url = models.URLField(max_length=500, verbose_name='Ссылка на группу Facebook')
    active = models.BooleanField(default=False, verbose_name='Активность профиля')
<<<<<<< HEAD
=======
    items_page = models.IntegerField(default=24, verbose_name='Товаров на странице')
    random_discount = models.IntegerField(default=5, verbose_name='Случайных объектов со скидкой')
<<<<<<< HEAD
>>>>>>> e95cd93 (Добавил поле random_discount для настроек, добавил метод выдающий заданное число случайных товаров со скидкой)
=======
    hit_count = models.IntegerField(default=5, verbose_name='Хитов продаж')
>>>>>>> ba49513 (Добавил отображение хитов продаж на главной странице)

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'Основные настройки'

#Номенклатура товаров
class Items(models.Model):
    name = models.CharField(max_length=25, verbose_name='Наименование товара')
    cost_of = models.IntegerField(default=0, verbose_name='Стоимость товара (руб)')
    discount = models.IntegerField(default=0, verbose_name='Скидка (0 - без скидки)')
    main_photo = models.ImageField(verbose_name=u"Главное фото", upload_to=get_file_path)
    room = models.ForeignKey('TypesRooms', verbose_name='Тип товара')
    category = models.ForeignKey('Categories', verbose_name='Категория товара', blank=True, null=True)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Номенклатура товаров'

    def get_discount(self):
        return self.cost_of - self.cost_of / 100 * self.discount

<<<<<<< HEAD
=======
    def photo_list(self):
        return Photo.objects.filter(item=self)

<<<<<<< HEAD
    def get_discount_random_items(count):
        items = Items.objects.filter(discount > 0).order_by('?')[:count]


>>>>>>> e95cd93 (Добавил поле random_discount для настроек, добавил метод выдающий заданное число случайных товаров со скидкой)
=======
>>>>>>> e990f9c (Удалил метод выдачи рандомных товаров со скидкой.)
    def delete(self, *args, **kwargs):
        storage, path = self.main_photo.storage, self.main_photo.path
        super(Items, self).delete(*args, **kwargs)
        storage.delete(path)

    def __unicode__(self):
        return self.name

#Фотографии товара
class Photo(models.Model):
    image = models.ImageField(verbose_name=u"Фотографии товара", upload_to=get_file_path)
    item = models.ForeignKey(Items)

    class Meta:
        verbose_name = 'фотографию'
        verbose_name_plural = 'Фотографии товара'

    def delete(self, *args, **kwargs):
        storage, path = self.image.storage, self.image.path
        super(Photo, self).delete(*args, **kwargs)
        storage.delete(path)

#Список помещений
class TypesRooms(models.Model):
    name = models.CharField(max_length=25, verbose_name='Наименование категории')
    data_id = models.IntegerField(default=0, verbose_name='Аттрибут data_id в html')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Список категорий'

    def get_categories(self):
        return Categories.objects.filter(room=self)

    def __unicode__(self):
        return self.name

#Список категорий
class Categories(models.Model):
    name = models.CharField(max_length=25, verbose_name='Наименование подкатегории')
    room = models.ForeignKey(TypesRooms, verbose_name='Категория')
    data_id = models.IntegerField(default=0, verbose_name='Аттрибут data_id в html')

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'Список подкатегорий'

    def __unicode__(self):
<<<<<<< HEAD
        return self.name
=======
        return self.room.name + ' | ' + self.name

class Factories(models.Model):
    name = models.CharField(max_length=25, verbose_name='Наименование фабрики')
    name_url = models.SlugField(max_length=20, verbose_name='Представление фабрики в виде URL')
    description = models.TextField(verbose_name='Описание фабрики')
    logo = models.ImageField(verbose_name=u"Логотип фабрики", upload_to=get_file_path_factories)
    preview = models.ImageField(verbose_name=u"Превью фабрики", upload_to=get_file_path_factories)

    class Meta:
        verbose_name = 'фабрика'
        verbose_name_plural = 'Список фабрик'

    def get_items(self):
        return Items.objects.filter(factory=self)
    
    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    def __unicode__(self):
        return self.name
>>>>>>> ba49513 (Добавил отображение хитов продаж на главной странице)
