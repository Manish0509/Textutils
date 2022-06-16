from django.contrib import admin
from django.urls import path
from .import views

# Code for Video 6
#urlpatterns = [
#   path('admin/', admin.site.urls),
#   path('', views.index, name='index'),
#   path('about', views.about, name='about'),
#]
# ode for Video 7
urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.index, name='index'),
   path('analyze', views.analyze, name='analyze'),
  # path('capitalizefirst', views.capitalizefirst, name='capitalizefirst'),
  # path('newlineremove', views.newlineremove, name='newlineremove'),
  #  path('spaceremove', views.spaceremove, name='spaceremove'),
  # path('charcount', views.charcount, name='charcount'),
]