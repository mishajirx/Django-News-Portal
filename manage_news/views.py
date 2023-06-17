from django.shortcuts import render
from django.views.generic import TemplateView
from .models import News

# Create your views here.


class MainView(TemplateView):
    template_name = 'base.html'

    def get(self, request):
        if request.user.is_authenticated:
            news = News.objects.filter(author=request.user)
            ctx = {'news': news}
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})
