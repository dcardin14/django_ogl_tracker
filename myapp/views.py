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
        form = OGLForm(request.POST, instance=ogl)
        formset = MineralTractFormset(request.POST, instance=ogl)

        if formset.is_valid():
            print("Formset is valid")
        else:
            print("Formset errors:", formset.errors)
            for form in formset:
                print("Form cleaned_data:", form.cleaned_data)

        if form.is_valid() and formset.is_valid():
            ogl = form.save()
            formset.instance = ogl  # Bind formset to the OGL instance
            formset.save()  # Save formset and handle deletions correctly
            messages.success(request, 'Lease updated successfully!')
            return redirect('home')
        else:
            # Debugging: Print errors and cleaned data
            print("Form errors:", form.errors)
            print("Formset errors:", formset.errors)
            for i, form in enumerate(formset):
                print(f"Form {i} cleaned_data:", form.cleaned_data)  # Debug each form
                print(f"Form {i} errors:", form.errors)  # Debug individual form errors
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
