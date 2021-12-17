from django.urls import path
from . import views, api
app_name = 'job'

urlpatterns = [
    path('', views.job_list, name='jobs'),
    path('post', views.job_post, name='job_post'),
    path('<int:id>', views.job_detail, name='job_detail'),
    path('candidates', views.view_candidates, name='candidates'),

    # api function based view
    path('api/list', api.job_list_api, name='api_list'),

    # api class based view
    path('api/v2/list', views.JobList.as_view(), name='api_list_v2')

]
