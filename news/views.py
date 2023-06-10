from django.shortcuts import render
from news.models import News

# Create your views here.

def news(request):
    newss = News.objects.all().order_by('-date') # для сортировки по дате добавления, будут отражаться самые ранние новости
    return render(request, 'news.html', {'newss': newss})