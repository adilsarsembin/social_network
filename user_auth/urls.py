from django.urls import path
from .views import CreateUserView, LoginUserView

urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login')
]
