from django.urls import path, include
from . import views

# A namespace for the polls app.
app_name = 'polls'

# A list of path() instances. Each path() call takes the following arguments:
urlpatterns = [
    path('', views.index, name='index'),
    path('polls/', views.poll, name='polls'),
    path('<int:poll_id>/', views.detail, name='detail'),
    path('<int:poll_id>/results/', views.results, name='results'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
]


