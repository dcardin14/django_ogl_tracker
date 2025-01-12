from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from .models import TodoItem, OGL
from .forms import OGLForm, MineralTractForm, MineralTractFormset

# Create your views here.
def home(request):
    ogl_list = OGL.objects.all()  # Fetch all OGL records
    return render(request, "home.html", {'ogl_list': ogl_list})

def update_ogl(request, pk):
    ogl = get_object_or_404(OGL, pk=pk)  # Retrieve the OGL instance
    prev_ogl = OGL.objects.filter(id__lt=pk).order_by('-id').first() # Left arrow
    next_ogl = OGL.objects.filter(id__gt=pk).order_by('id').first() # Right arrow
    if request.method == 'POST':
        form = OGLForm(request.POST, instance=ogl)  # Bind to the existing instance
        formset = MineralTractFormset(request.POST, instance=ogl)  # Bind to related mineral tracts
        if form.is_valid() and formset.is_valid():
            ogl = form.save()  # Save the updated OGL
            formset.save()  # Save the related MineralTracts
            messages.success(request, 'Lease updated successfully!')  # Success message
            return redirect('home')  # Redirect to a success page (update this as needed)
    else:
        form = OGLForm(instance=ogl)  # Populate form with existing data
        formset = MineralTractFormset(instance=ogl)  # Populate formset with existing data

    return render(request, 'update_ogl.html', {
        'form': form,
        'formset': formset,
        'prev_ogl': prev_ogl,
        'next_ogl': next_ogl,
    })

def add_ogl(request):
    if request.method == 'POST':
        form = OGLForm(request.POST)
        formset = MineralTractFormset(request.POST)
        if form.is_valid() and formset.is_valid():
            ogl = form.save()  # Save the OGL instance
            formset.instance = ogl  # Link the formset to the saved OGL
            formset.save()  # Save all related MineralTracts
            return redirect('home')  # Redirect to a success page
    else:
        form = OGLForm()
        formset = MineralTractFormset()

    # Always render the form, whether it’s a GET or invalid POST
    return render(request, 'add_ogl.html', {'form': form, 'formset': formset})
