from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

# Create your views here.

# Render de paginas
def home(request):
    context={}
    return render(request,'pages/Home.html',context )

def productos(request):
    context={}
    return render(request,'pages/productos.html',context )

def nosotros(request):
    context={}
    return render(request,'pages/Nosotros.html',context )

# Validaciones
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


# Crud
# Vista para listar usuarios
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'pages/listar_usuarios.html', {'usuarios': usuarios})

# Vista para crear un nuevo usuario
def crear_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        correo_electronico = request.POST['correo_electronico']
        telefono = request.POST['telefono']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('crear_usuario')

        usuario = Usuario(
            nombre=nombre,
            apellido=apellido,
            correo_electronico=correo_electronico,
            telefono=telefono,
            password=make_password(password)  # Asegúrate de cifrar las contraseñas
        )
        usuario.save()
        messages.success(request, 'Usuario creado exitosamente.')
        return redirect('listar_usuarios')

    return render(request, 'pages/crear_usuario.html')

# Vista para actualizar un usuario
def actualizar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        usuario.nombre = request.POST['nombre']
        usuario.apellido = request.POST['apellido']
        usuario.correo_electronico = request.POST['correo_electronico']
        usuario.telefono = request.POST['telefono']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('actualizar_usuario', usuario_id=usuario.id)

        usuario.password = make_password(password)
        usuario.save()
        messages.success(request, 'Usuario actualizado exitosamente.')
        return redirect('listar_usuarios')

    return render(request, 'pages/actualizar_usuario.html', {'usuario': usuario})

# Vista para eliminar un usuario
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    usuario.delete()
    messages.success(request, 'Usuario eliminado exitosamente.')
    return redirect('listar_usuarios')