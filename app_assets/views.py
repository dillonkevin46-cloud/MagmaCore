from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Asset

@login_required
def asset_list(request):
    assets = Asset.objects.all().select_related('category').order_by('name')
    return render(request, 'app_assets/asset_list.html', {'assets': assets})
