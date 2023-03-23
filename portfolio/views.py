from django.views.generic import TemplateView

from utsab.models import Home
from about.models import About


class IndexPage(TemplateView):
     template_name = 'index.html'
     
     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context["home"] = Home.objects.all()
          context["about"] = About.objects.last()
          
          return context