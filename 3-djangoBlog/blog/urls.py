from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('archive/', views.archive, name='archive'),
    path('<>/', views.blog_post, name='blog_post'), # TODO: what is start of path

    # IMPORT VIEWS

]