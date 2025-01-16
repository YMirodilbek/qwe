from django.views.generic import DetailView
from .models import Certificate

class CertificateDetailView(DetailView):
    model = Certificate
    template_name = 'index.html' 
    context_object_name = 'certificate'

