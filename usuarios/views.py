from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.views.generic import CreateView, TemplateView
from .models import Perfil
from hipertension.models import Hipertension
from diabetes.models import Diabetes
from django.contrib.auth.models import User
from usuarios.forms import SignUpForm, LoginForm

# Create your views here.
class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
   template_name = 'usuarios/bienvenida.html'


from django.contrib.auth.views import LoginView

class SignInView(LoginView):
    form_class=LoginForm
    template_name = 'usuarios/iniciar_sesion.html'


from django.contrib.auth.views import LogoutView 

class SignOutView(LogoutView):
    pass


def historial(request):
    usuariop=User.objects.get(username=request.user)
    consulta=Hipertension.objects.filter(usuario=usuariop).order_by("-id")

    consulta_diabetes = Diabetes.objects.filter(user=usuariop).order_by("-id")

    return render(request, "usuarios/historial.html", {"consultas":consulta, "consultadiabetes":consulta_diabetes})