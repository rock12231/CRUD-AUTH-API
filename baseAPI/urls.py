from django.urls import path
from baseAPI.views import DesignList , RegistrationView , LogoutView , DesignDetail
urlpatterns = [
    path('alldesigns', DesignList.as_view()),
    path('designs', DesignDetail.as_view()),
    path('designs/<int:id>', DesignDetail.as_view()),
    path('register', RegistrationView.as_view()),
    path('logout', LogoutView.as_view()),
]