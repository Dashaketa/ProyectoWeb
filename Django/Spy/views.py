from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

# Create your views here.
def home(request):
    context={}
    return render(request,'pages/Home.html',context )

def productos(request):
    context={}
    return render(request,'pages/productos.html',context )

def nosotros(request):
    context={}
    return render(request,'pages/Nosotros.html',context )


def inicioSesion(request):
    if request.method == 'POST':
        correo_electronico = request.POST['correo_electronico']
        password = request.POST['password']

        try:
            usuario = Usuario.objects.get(correo_electronico=correo_electronico)
            if check_password(password, usuario.password):
                # Aquí puedes establecer una sesión de usuario si es necesario
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('home')
            else:
                messages.error(request, 'Contraseña incorrecta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario no encontrado.')

    return render(request, 'pages/InicioSesion.html')



def registro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo_electronico = request.POST['correo_electronico']
        telefono = request.POST['telefono']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('registro')

        usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            correo_electronico=correo_electronico,
            telefono=telefono,
            password=make_password(password)  # Asegúrate de cifrar las contraseñas en una implementación real
        )
        usuario.save()
        messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
        return redirect('inicioSesion')

    return render(request, 'pages/registro.html')


