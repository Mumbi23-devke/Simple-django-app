from django.shortcuts import render, redirect

from .models import Client


def homepage(request):
    data = Client.objects.all()
    context = {"data": data}
    return render(request, "home.html", context)


def insertdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        destination = request.POST.get('destination')
        period = request.POST.get('period')
        nationality = request.POST.get('nationality')
        people = request.POST.get('people')

        query = Client.objects.create(name=name, email=email, destination=destination, period=period,
                                      nationality=nationality, people=people)
        query.save()
        return redirect("/")
    return render(request, "home.html")


# noinspection PyUnreachableCode
def delete(request, id):
    d = Client.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "home.html")


def updatedata(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        destination = request.POST.get('destination')
        period = request.POST.get('period')
        nationality = request.POST.get('nationality')
        people = request.POST.get('people')

        edit_data = Client.objects.get()
        edit_data.name = name
        edit_data.email = email
        edit_data.destination = destination
        edit_data.period = period
        edit_data.nationality = nationality
        edit_data.people = people
        edit_data.save()

        return redirect("/")

    data = Client.objects.get(id=id)
    data.update()
    context = {"data": data}
    return render(request, "home.html", context)

