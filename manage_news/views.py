from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
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


class LoginView(FormView):
    form_class = AuthenticationForm
    success_url = '/news/'
    template_name = 'login.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return super(LoginView, self).form_invalid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/news/')
