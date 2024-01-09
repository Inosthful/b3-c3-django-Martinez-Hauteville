from django.shortcuts import render, get_object_or_404, redirect
from .models import Site
from .forms import SiteForm

def list_sites(request):
    sites = Site.objects.all()
    return render(request, 'sites/list_sites.html', {'sites': sites})

def add_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SiteForm()
    return render(request, 'sites/add_site.html', {'form': form})

def change_site(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    if request.method == 'POST':
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SiteForm(instance=site)
    return render(request, 'sites/change_site.html', {'form': form, 'site': site})

def suppress_site(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    if request.method == 'POST':
        site.delete()
        return redirect('/')

    return render(request, 'sites/suppress_site.html', {'site': site})