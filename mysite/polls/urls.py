from django.urls import path
from django.conf.urls import url

from polls.views import RequesterView,RiderView

app_name = 'polls'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    url(r"^requester$",RequesterView.as_view({
        'get': 'retrieve',
        'post': 'create',
        }),name="requester"),
    url(r"^requester/match",RequesterView.as_view({
        'get': 'matching_riders',
        }),name="matching_riders"),
    url(r"^rider",RiderView.as_view({
        'get': 'retrieve',
        'post': 'create',
        }),name="requester"),
]
