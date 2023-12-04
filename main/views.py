#! coding: utf-8

from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Max, Min
from main import models 
from main import forms 

class MainTemplate(TemplateView):
    template_name = 'main_template.html'
    def get_context_data(self, **kwards):
        context = super(MainTemplate, self).get_context_data(**kwards)
        context['title'] = "GrandEurMoscow.ru - Мебель вашей мечты"
        context['settings'] = models.Settings.objects.filter(active=True).last()
        return context

class MainPageView(MainTemplate):
    template_name = 'main_page.html'
    def get_context_data(self, **kwards):
        context = super(MainPageView, self).get_context_data(**kwards) 
        context['current'] = 1
        hit_items = models.Items.objects.all().order_by('-sales')[:context['settings'].hit_count]
        discount_items = models.Items.objects.filter(discount__gt=0).order_by('?')[:context['settings'].random_discount]
        context['hit_items'] = hit_items
        context['discount_items'] = discount_items
        return context

class NewsPageView(MainTemplate):
    template_name = 'news_page.html'
    def get_context_data(self, **kwards):
        context = super(NewsPageView, self).get_context_data(**kwards) 
        context['current'] = 2
        return context

class SalesPageView(MainTemplate):
    template_name = 'sales_page.html'
    def get_context_data(self, **kwards):
        context = super(SalesPageView, self).get_context_data(**kwards) 
        context['current'] = 3
        return context

class CatalogPageView(MainTemplate):
    template_name = 'catalog_page.html'
    def get_context_data(self, **kwards):
        context = super(CatalogPageView, self).get_context_data(**kwards)
        context['title'] = 'GrandEurMoscow.ru - Каталог' 
        context['current'] = 4
        context['nomenclature'] = models.TypesRooms.objects.all()
        context['items'] = models.Items.objects.all()
        context['cost_data'] = models.Items.objects.all().aggregate(Max('cost_of'), Min('cost_of'))
        return context

class FactoriesPageView(MainTemplate):
    template_name = 'factories_page.html'
    def get_context_data(self, **kwards):
        context = super(FactoriesPageView, self).get_context_data(**kwards) 
        context['current'] = 5
        context['factories'] = models.Factories.objects.all()
        return context

class DesignersPageView(MainTemplate):
    template_name = 'designers_page.html'
    def get_context_data(self, **kwards):
        context = super(DesignersPageView, self).get_context_data(**kwards) 
        context['current'] = 6
        return context

class ContactsPageView(MainTemplate):
    template_name = 'contacts_page.html'
    def get_context_data(self, **kwards):
        context = super(ContactsPageView, self).get_context_data(**kwards) 
        context['current'] = 7
        return context 