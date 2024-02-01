import csv
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Site
from .forms import SiteForm, CSVUploadForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


@login_required
def list_sites(request):
    sites = Site.objects.filter(user=request.user)
    return render(request, 'sites/list_sites.html', {'sites': sites})


@login_required
def add_site(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.user = request.user  
            site.save()
            return redirect('/') 
    else:
        form = SiteForm()
    return render(request, 'sites/add_site.html', {'form': form})

@login_required
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

@login_required
def suppress_site(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    if request.method == 'POST':
        site.delete()
        return redirect('/')

    return render(request, 'sites/suppress_site.html', {'site': site})



@login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'

    writer = csv.writer(response)
    writer.writerow(['Nom', 'URL', 'Identifiant', 'Mot de passe'])

    sites = Site.objects.all()
    for site in sites:
        writer.writerow([site.nom, site.url, site.identifiant, site.mot_de_passe])

    return response


@login_required
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

            return redirect('list_sites')
    else:
        form = CSVUploadForm()

    return render(request, 'sites/import_csv.html', {'form': form})

@csrf_exempt
def toggle_dark_mode(request):
    if request.method == 'POST':
        # Basculement du mode sombre
        request.session['DARK_MODE'] = not request.session.get('DARK_MODE', False)
        request.session.save()
        return JsonResponse({'status': 'success'})
    elif request.method == 'GET':
        # Pour récupérer l'état actuel du mode (clair ou sombre)
        dark_mode = request.session.get('DARK_MODE', False)
        return JsonResponse({'dark_mode': dark_mode})
    return JsonResponse({'status': 'error'})



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
