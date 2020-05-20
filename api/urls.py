from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'service-requirements', views.ServiceRequirementsViewSet)
router.register(r'services', views.ServicesViewSet)
router.register(r'arrangements', views.ArrangementViewSet)
router.register(r'file-requirement', views.FileRequirementViewSet)
router.register(r'detail-requirement', views.DetailRequirementViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.login),
    path('cek-register/', views.check_register),
    path('create-user/', views.create_user),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
