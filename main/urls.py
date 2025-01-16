from django.urls import path
from .views import CertificateDetailView

urlpatterns = [
    path('certificate/<int:pk>/', CertificateDetailView.as_view(), name='certificate_detail'),
]
