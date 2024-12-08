from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipo  # Asegúrate de importar el modelo Equipo
from .forms import EquipoForm  
from django.contrib import messages
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from io import BytesIO
from django.template.loader import render_to_string
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Vista principal - Cargar todos los equipos para mostrar en la tabla
def index(request):
    equipos = Equipo.objects.all()  # Obtén todos los equipos de la base de datos
    return render(request, 'inventario/index.html', {'equipos': equipos})

# Vista para mostrar todos los equipos
def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'inventario/equipos.html', {'equipos': equipos})

# Vista para ver los detalles de un equipo
def detalle_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)  
    return render(request, 'inventario/detalle_equipo.html', {'equipo': equipo})

# Vista para exportar los detalles del equipo a PDF
def exportar_equipo_pdf(request, equipo_id):
    # Obtener el equipo por ID
    equipo = Equipo.objects.get(id=equipo_id)
    
    # Renderizar el template a un string
    html_content = render_to_string('inventario/detalle_equipo.html', {'equipo': equipo})
    
    # Crear el archivo PDF
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Aquí, en vez de agregar solo texto simple, podrías renderizar contenido HTML,
    # pero para simplificar, agregaré solo el texto básico del equipo.
    p.drawString(100, 750, f"Número de Placa: {equipo.numero_placa}")
    p.drawString(100, 735, f"Tipo de Equipo: {equipo.tipo_equipo}")
    p.drawString(100, 720, f"Marca: {equipo.marca}")
    p.drawString(100, 705, f"Modelo: {equipo.modelo}")
    p.drawString(100, 690, f"Fecha de ingreso: {equipo.fecha_ingreso}")
    
    # Guardar el PDF en el buffer
    p.showPage()
    p.save()
    
    # Obtener el PDF generado
    pdf = buffer.getvalue()
    buffer.close()

    # Devolver el PDF como una respuesta HTTP
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="equipo_{equipo_id}.pdf"'
    return response

# Vista para crear un nuevo equipo
def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('equipos')  
    else:
        form = EquipoForm()  
    return render(request, 'inventario/crear_equipo.html', {'form': form})

# Vista para editar un equipo existente
def editar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)

    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'El equipo se ha editado correctamente.')
                return redirect('equipos')
            except Exception as e:
                messages.error(request, f'Error al guardar el equipo: {str(e)}')
        else:
            messages.error(request, 'Por favor, corrija los errores del formulario.')
    else:
        form = EquipoForm(instance=equipo)

    return render(request, 'inventario/editar_equipo.html', {'form': form, 'equipo': equipo})

# Vista para eliminar un equipo
def eliminar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)  
    if request.method == 'POST':
        equipo.delete()  
        return redirect('equipos') 
    return render(request, 'inventario/eliminar_equipo.html', {'equipo': equipo})
