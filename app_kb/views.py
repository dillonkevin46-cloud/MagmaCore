from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article

@login_required
def article_list(request):
    articles = Article.objects.filter(is_public=True).select_related('category').order_by('-created_at')
    return render(request, 'app_kb/article_list.html', {'articles': articles})
