import csv
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Site
from .forms import SiteForm, CSVUploadForm

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

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nom', 'URL', 'Identifiant', 'Mot de passe'])

    sites = Site.objects.all()
    for site in sites:
        writer.writerow([site.nom, site.url, site.identifiant, site.mot_de_passe])

    return response

def import_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(decoded_file)

            for row in csv_reader:
                site = Site(
                    nom=row['Nom'],
                    url=row['URL'],
                    identifiant=row['Identifiant'],
                    mot_de_passe=row['Mot de passe']
                )
                site.save()

            return redirect('liste_sites')
    else:
        form = CSVUploadForm()

    return render(request, 'import_csv.html', {'form': form})