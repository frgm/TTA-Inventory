from django.urls import path
from mainApp.views import *
from . import views

urlpatterns = [
    path('adminInv', views.adminInv, name='adminInv'),
    path('adminPro', views.adminPro, name='adminPro'),
    path('distribution', views.distribution, name='distribution'),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('login', views.index, name='index'),
    path('production', views.production, name='production'),
    path('report', views.report, name='report'),
    path('report/db', dbReport.as_view()),
    path('production/db', dbProduction.as_view()),
    path('distribution/db', dbDistribution.as_view()),
    path('adminPro/db', dbAdminPro.as_view()),
    path('adminInv/db', dbAdminInv.as_view()),
    path('index/login', login.as_view())
    path('menu', views.menu, name='menu')
]