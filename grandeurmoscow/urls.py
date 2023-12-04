"""grandeurmoscow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from main import views
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView



urlpatterns = [
    url(r'^$', views.MainPageView.as_view()),
<<<<<<< HEAD
    url(r'^news/', views.NewsPageView.as_view()),
    url(r'^sales/', views.SalesPageView.as_view()),
    url(r'^catalog/', views.CatalogPageView.as_view()),
    url(r'^factories/', views.FactoriesPageView.as_view()),
    url(r'^designers/', views.DesignersPageView.as_view()),
    url(r'^contacts/', views.ContactsPageView.as_view()),
    url(r'^controlpanel/', admin.site.urls),
=======
    url(r'^news/$', views.NewsPageView.as_view()),
    url(r'^sales/$', views.SalesPageView.as_view()),
    url(r'^catalog/page/(?P<catalog_page_id>\w+)/$', views.CatalogPageView.as_view()),
    url(r'^catalog/item/(?P<item_id>\w+)/$', views.ItemPageView.as_view()),
    url(r'^catalog/(?P<room_name_url>\w+)/(?P<category_name_url>\w+)/page/(?P<cat_page_id>\w+)/$', views.CatalogPageView.as_view()),
    url(r'^catalog/(?P<room_name_url>\w+)/(?P<category_name_url>\w+)/$', views.CatalogPageView.as_view()),
    url(r'^catalog/(?P<room_name_url>\w+)/page/(?P<room_page_id>\w+)/$', views.CatalogPageView.as_view()),
    url(r'^catalog/(?P<room_name_url>\w+)/$', views.CatalogPageView.as_view()),
    url(r'^catalog/$', views.CatalogPageView.as_view()),
    url(r'^factories/(?P<factory_name_url>\w+)/$', views.FactoriesPageView.as_view()),
    url(r'^factories/$', views.FactoriesPageView.as_view()),
    url(r'^designers/$', views.DesignersPageView.as_view()),
    url(r'^contacts/$', views.ContactsPageView.as_view()),
    url(r'^admin/', admin.site.urls),
>>>>>>> faad947 (Много чего)
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
]

if settings.DEBUG:
    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)