from django.shortcuts import render, redirect
from .models import *
from App1.forms import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,  authenticate


#FUNCIONES#

def login_request(request):
    msg_login = ""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            nombre_usuario = authenticate(username=user, password=clave)
            if user is not None:
                login(request, nombre_usuario)
                return render(request, "App1/index.html")
        msg_login = "Usuario o contraseña incorrectos"    
       
    form = AuthenticationForm()
    
    return render(request, "App1/login.html", {'form':form, 'msg_login': msg_login})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "App1/postRegistro.html", {'username': username})
    else:
        form = UserRegisterForm()
            
    return render(request, "App1/registro.html", {'form':form})   

def inicio(request):
    return render(request, "App1/index.html")

def aboutMe(request):
    return render(request, "App1/aboutMe.html", {})

@login_required
def valoranos(request):
    if request.method == "POST":
       reseñaFormulario = ReseñaFormulario(request.POST)
   
       if reseñaFormulario.is_valid():
            info_ =reseñaFormulario.cleaned_data
            usuario = Reseñas(name=info_['name'], opinion=info_['opinion'], puntaje=info_['puntaje'])
            usuario.save()
            
            return render(request, "App1/postValoracion.html")
    else:
       reseñaFormulario = ReseñaFormulario()
  
    return render(request, "App1/valoranos.html",{"reseñaFormulario":reseñaFormulario})
 
def buscarCafeterias(request):
    if request.method =="POST":
        buscarFormulario = BuscarCafeterias(request.POST)
        if buscarFormulario.is_valid():
           info = buscarFormulario.cleaned_data
           cafeterias = Cafeterias.objects.filter(direccion__icontains=info["direccion"])
           return render(request, "App1/mostrarBusqueda.html", {"cafeterias": cafeterias})
    else:
        buscarFormulario=BuscarCafeterias()
        
       
    return render(request, "App1/buscarCafeterias.html", {"buscarFormulario":buscarFormulario})

@login_required
def postAgregar(request):
    return render(request, "App1/postAgregar.html")   


@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            if informacion["password1"] != informacion["password2"]:
                datos = {
                    'first_name': usuario.first_name,
                    'email': usuario.email
                }
                miFormulario = UserEditForm(initial=datos)
                mensaje = "Las contraseñas deben coincidir"

            else:
                usuario.email = informacion['email']
                if informacion["password1"]:
                    usuario.set_password(informacion["password1"])
                usuario.last_name = informacion['last_name']
                usuario.first_name = informacion['first_name']
                usuario.save()

               

                return render(request, "App1/perfil.html")

    else:
        datos = {
            'first_name': usuario.first_name,
            'email': usuario.email
        }
        miFormulario = UserEditForm(initial=datos)

    return render(request, "App1/editarPerfil.html", {"form": miFormulario, "usuario": usuario})
  
#CBV#


class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'dato'
    template_name = "App1/perfil.html"   

class CafeteriaAgregarView(LoginRequiredMixin, CreateView):
    model = Cafeterias
    form_class = AgregarFormulario
    template_name = 'App1/agregarCafeteria.html'
    success_url = reverse_lazy("PostAgregar")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CafeteriaListView(ListView):
    model = Cafeterias
    template_name = "App1/cafeterias.html" 

class CafeteriaDetailView(View):
    model = Cafeterias
    context_object_name = 'cafeteria'
    template_name = "App1/cafeteriaDetalle.html"   

    def get(self, request, pk):
        cafeteria = Cafeterias.objects.get(pk=pk)
        comentarios = Comentario.objects.filter(cafeteria=cafeteria)
        form = ComentarioForm() 

        context = {'cafeteria': cafeteria, 'comentarios': comentarios, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        cafeteria = Cafeterias.objects.get(pk=pk)
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.cafeteria = cafeteria
            comentario.autor = request.user  
            comentario.save()
            return redirect('DetalleCafeteria', pk=pk)

        comentarios = Comentario.objects.filter(cafeteria=cafeteria)
        context = {'cafeteria': cafeteria, 'comentarios': comentarios, 'form': form}
        return render(request, self.template_name, context)
        
class CafeteriaEditarView(LoginRequiredMixin, UpdateView):
    template_name = 'App1/editarCafeteria.html'  
    
    def get(self, request, pk):
        cafeteria = Cafeterias.objects.get(pk=pk)
        form = UpdateFormulario(instance=cafeteria)  

        context = {'form': form, 'cafeteria': cafeteria}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        cafeteria = Cafeterias.objects.get(pk=pk)
        form = UpdateFormulario(request.POST, request.FILES, instance=cafeteria)  

        if form.is_valid():
            form.save()
            return redirect('DetalleCafeteria', pk=cafeteria.pk)
        else:
            context = {'form': form, 'cafeteria': cafeteria}
            return render(request, self.template_name, context) 

class CafeteriaDeletelView(LoginRequiredMixin, DeleteView):
    model = Cafeterias
    context_object_name = 'cafeteria'
    template_name = "App1/confirEliminar.html" 
    success_url = reverse_lazy("ListaCafeterias")   
    
      



    

