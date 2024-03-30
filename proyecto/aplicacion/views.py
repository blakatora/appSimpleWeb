from django.shortcuts import render
from .models import Moto, Reparacion,Cliente
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
def clientes(request):
    # Obtener todos los clientes de la base de datos
    
    
    clientes = Cliente.objects.all()

    return render(request, 'clientes.html', {'clientes': clientes})
    
    # Pasar los clientes al contexto de la plantilla
def agregar_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')
        dni = request.POST.get('dni')

        # Crear un nuevo cliente en la base de datos
        cliente = Cliente.objects.create(
            nombre_completo=nombre,
            correo=correo,
            telefono=telefono,
            direccion=direccion,
            dni=dni
        )

        return render(request, 'clientes.html', {'clientes': clientes})
    else:
        return JsonResponse({'error': 'Solicitud no válida'}, status=400)


def detalle_moto(request, moto_id):
    try:
        # Obtener la moto específica según el ID proporcionado
        moto = Moto.objects.get(pk=moto_id)
        
        # Obtener todas las reparaciones asociadas a la moto
        reparaciones = Reparacion.objects.filter(moto=moto)
        
        # Renderizar la plantilla HTML con los datos de la moto y las reparaciones
        return render(request, 'detalle_moto.html', {'moto': moto, 'reparaciones': reparaciones})
    except Moto.DoesNotExist:
        # Manejar el caso en el que la moto no exista
        return render(request, 'error.html', {'mensaje': 'La moto especificada no existe'})
    except Exception as e:
        # Manejar cualquier otra excepción
        return render(request, 'error.html', {'mensaje': str(e)})
