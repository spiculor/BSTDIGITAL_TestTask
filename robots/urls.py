from django.urls import path
from .views import RobotCreateView

urlpatterns = [
    path('api/robots/create/', RobotCreateView.as_view(), name='robot-create'),
]
