from django.shortcuts import render


def main(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def sale(request):
    return render(request, 'main/sale.html')
