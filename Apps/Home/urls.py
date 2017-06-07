from django.conf.urls import url
from Apps.Home.views import index, contacto_view, administracion,quienes_somos,informatica,servprofesionales


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', contacto_view, name='contacto_enviar'),
    url(r'^adm-finanzas$', administracion, name='adm-finanza'),
    url(r'^informatica$', informatica, name='informatica'),
    url(r'^quienes_somos$', quienes_somos, name='quienes_somos'),
    url(r'^servprofesionales$', servprofesionales, name='servprofesionales'),
]