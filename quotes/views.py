# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import QuoteForm, AuthorForm
from .models import Quote, Author
from .utils import get_mongodb


def main(request):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "quotes/index.html", context={'quotes': page_obj})


def author_info(request, _id):
    db = get_mongodb()
    author = Author.objects.get(pk=_id)
    return render(request, 'quotes/author.html', context={'author': author})


def add_quote(request):
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            return redirect(to="quotes:main")
        else:
            return render(request, "quotes/new_quote.html", context={'form': QuoteForm(), "message": "Form not valid"})
    return render(request, "quotes/new_quote.html", context={'form': QuoteForm()})


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_quote = form.save()
            return redirect(to="quotes:main")
        else:
            return render(request, "quotes/new_author.html",
                          context={'form': AuthorForm(), "message": "Form not valid"})
    return render(request, "quotes/new_author.html", context={'form': AuthorForm()})