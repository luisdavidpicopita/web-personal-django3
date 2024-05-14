from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi Web Personal</h1>
<ul>
    <li><a href="/">Portada</a>
    <li><a href="/about">Acerca de...</a>
</ul>
"""

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")

def portofolio(request):
    return render(request, "core/portfolio.html")

def contacto(request):
    return render(request, "core/contacto.html")