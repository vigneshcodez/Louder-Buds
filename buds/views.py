from django.shortcuts import render, redirect
from .models import Category, Product_article, comparision

# Create your views here.


def home(request):
    category = Category.objects.all()
    article = Product_article.objects.all()

    return render(request, 'pages/home.html', {'category': category, 'article': article})


def review(request):
    article = Product_article.objects.filter(latest=True)
    return render(request, 'pages/review.html', {'article': article})


def bestbuy(request):
    article = Product_article.objects.filter(bestbuy=True)
    return render(request, 'pages/bestbuy.html', {'article': article})


def detailedview(request, id):
    article = Product_article.objects.filter(id=id).first()
    return render(request, 'pages/detailedview.html', {'article': article})


def searchpage(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        if searched != '':
            article = Product_article.objects.filter(
                Product_name__icontains=searched)
            return render(request, 'pages/searchpage.html', {'article': article, 'searched': searched})
        else:
            return redirect('home')
    else:
        return redirect('home')


def comparisonpage(request):
    article = comparision.objects.all()
    return render(request, 'pages/comparisionmainpage.html', {'article': article})


def detailedcomparisionpage(request, id):
    article = comparision.objects.get(id=id)
    return render(request, 'pages/detailedcomparisionpage.html', {'item': article})
