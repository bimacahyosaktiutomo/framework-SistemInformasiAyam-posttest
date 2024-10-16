import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.models import Q
from .models import Produks
from .forms import ProduksForm

# Create your views here.
def homepage(request):
    produks = Produks.objects.all()
    return render(request, 'homepage/index.html', {'produks': produks})

def about(request):
    return render(request, 'homepage/about.html')

def katalog(request):
    query = request.GET.get('q')
    produks = Produks.objects.all()
    if query:
        produks = Produks.objects.filter(
            Q(name__icontains=query) |
            Q(kategori__icontains=query) |
            Q(description__icontains=query) 
        )
    else:
        produks = Produks.objects.all()
    return render(request, 'homepage/katalog.html', {'produks' : produks, 'query' : query})

# READ, CREATE, SEARCHING
def dashboard(request):
    query = request.GET.get('q')
    produks = Produks.objects.all()
    if query:
        produks = Produks.objects.filter(
            Q(name__icontains=query) |
            Q(kategori__icontains=query) |
            Q(description__icontains=query) 
        )
    else:
        produks = Produks.objects.all()

    if request.method == 'POST':
        form = ProduksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produk berhasil ditambah!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Produk gagal ditambah!')
    else:
        form = ProduksForm()
    return render(request, 'adminpage/dashboard.html', {'form': form, 'produks': produks , 'query' : query})

# UPDATE
def produks_update(request, produks_id):
    produks = get_object_or_404(Produks, id=produks_id)
    old_image = produks.image
    if request.method == 'POST':
        form = ProduksForm(request.POST, request.FILES, instance=produks)
        if form.is_valid():
            if request.FILES:
                if old_image and os.path.isfile(str(old_image.path)):
                    os.remove(os.path.join(settings.MEDIA_ROOT, str(old_image)))
            form.save()
            messages.success(request, 'Produk berhasil diubah!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Produk gagal diubah!')
    else:
        form = ProduksForm(instance=produks)
    return render(request, 'adminpage/produks/update.html', {'form': form, 'produks': produks})

#DELETE
def produks_delete(request, produks_id):
    produks = get_object_or_404(Produks, id=produks_id)
    if produks.image:
        try:
            os.remove(os.path.join(settings.MEDIA_ROOT, str(produks.image)))  # Adjust if necessary
        except Exception as e:
            messages.error(request, f'Error deleting image file: {e}')
    produks.delete()
    messages.success(request, 'Data Produk berhasil dihapus')
    return JsonResponse({'success': True})