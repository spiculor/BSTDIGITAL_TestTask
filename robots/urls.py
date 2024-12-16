from django.urls import path
from .views import RobotCreateView
from .views import WeeklyReportView


urlpatterns = [
    path('api/robots/create/', RobotCreateView.as_view(), name='robot-create'),
    path('api/robots/weekly-report/', WeeklyReportView.as_view(), name='weekly-report'),
]
