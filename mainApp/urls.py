from django.urls import path

from . import views

urlpatterns = [
    path('adminInv', views.adminInv, name='adminInv'),
    path('adminPro', views.adminPro, name='adminPro'),
    path('distribution', views.distribution, name='distribution'),
    path('', views.index, name='index'),
    path('production', views.production, name='production'),
    path('report', views.report, name='report'),
    path('report/db', dbReport.as_view()),
    path('production/db', dbProduction.as_view())
]