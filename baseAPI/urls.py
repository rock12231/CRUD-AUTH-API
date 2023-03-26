from django.urls import path
from baseAPI.views import DesignList , RegistrationView , LogoutView , DesignDetail
urlpatterns = [
    # Get all designs
    path('alldesigns', DesignList.as_view()),
    # Get design by id
    path('designs', DesignDetail.as_view()),
    # Put and Delete design by id
    path('designs/<int:id>', DesignDetail.as_view()),
    # register a new user
    path('register', RegistrationView.as_view()),
    # User logout
    path('logout', LogoutView.as_view()),
]