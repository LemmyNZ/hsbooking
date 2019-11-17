from django.shortcuts import render, redirect, get_object_or_404


from .forms import PetRegistrationForm, PetUpdateForm
from .models import Pet

def pet_register_view(request):
    conetext = {}

    if request.POST:
        form = PetRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context = {"form": form}

    else:
        form = PetRegistrationForm()
        context = {"form": form}
    return render(request, 'pets/registration.html', context)


def pet_list_view(request):
    qs = Pet.objects.all()
    if request.user_is_authenticated:
        my_qs = Pet.objects.filter(user=request.user)
        qs = (qs | my_qs).distict()
    template_name = 'pets/list.html'
    context = {'object_list.html': qs}
    return render(request, template_name, context)

def pet_detail_view(request, id):
    obj = Pet.objects.get(id=id)
    template_name = 'pets/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def pet_update_view(request, id):
    obj = Pet.objects.get(id=id)
    form = PetUpdateForm(request.POST or None, instance=obj)
    if request.POST:
        if form.is_valid():
            form.save()

    context={"form": form}
    return render(request, 'pets/update.html', context)

def pet_delete_view(request, id):
    obj = Pet(id=id)
    if request.method == POST:
        obj.delete()
        return redirect('home')
    context = {"object": obj}
    return render(request, 'pets/delete.html', context)
