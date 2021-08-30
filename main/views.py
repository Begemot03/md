import datetime
from django.db.models.query import QuerySet
from django.http.response import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .forms import ClientForm
from .models import ClientModelB
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import math

@login_required
def index(request):
    return render(request, 'main/index.html')

@login_required
def showClient(request):
    offset = 4
    data = dict()
    clients = ClientModelB.objects.filter(user=request.user)
    fsm = request.GET.get('fsm')
    data['fsm'] = fsm if fsm != None else ''
    if fsm != None:
        fsm = str(fsm).strip().split()
        
        sname = fsm[0] if len(fsm) > 0 else None
        fname = fsm[1] if len(fsm) > 1 else None
        mname = fsm[2] if len(fsm) > 2 else None
            
        if sname != None:
            print(1)
            clients = clients.filter(secondName=sname)
            print(clients)
        if fname != None:
            print(2)
            clients = clients.filter(firstName=fname)
        if mname != None:
            print(3)
            clients = clients.filter(middleName=mname)

    data['clients'] = clients
    
    pages = math.ceil(len(data['clients']) / offset)
    data['clients'] = list(data['clients'])[(int(request.GET.get('page')) - 1) * offset: offset * (int(request.GET.get('page')))]
    data['pages'] = {
        'prev': str(int(request.GET.get('page')) - 1) if int(request.GET.get('page')) > 1 else '1',
        'next': str(int(request.GET.get('page')) + 1) if int(request.GET.get('page')) < pages else str(pages),
    }
    
    if int(request.GET.get('page')) < 2 or int(request.GET.get('page')) == 2:
        data['pages']['link'] = [1, 2, 3]
    else:
        data['pages']['link'] = list(range(min(pages - 3, int(request.GET.get('page')) - 2) + 1, min(pages, int(request.GET.get('page')) + 2) + 1))

    return render(request, 'main/client_view_list.html', data)

@login_required
def createClient(request):
    clientForm = ClientForm()

    data = {
        'form': clientForm,
    }

    return render(request, 'main/client_information_create.html', data)

@login_required
def saveInfo(request):
    data = dict()

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            client = ClientModelB()
            client.firstName = form.cleaned_data.get('firstName')
            client.secondName = form.cleaned_data.get('secondName')
            client.middleName = form.cleaned_data.get('middleName')
            client.age = form.cleaned_data.get('age')
            client.address = form.cleaned_data.get('address')
            client.mail = form.cleaned_data.get('mail')
            client.imgBefore = form.cleaned_data.get('imgBefore')
            client.imgAfter = form.cleaned_data.get('imgAfter')
            client.comment1 = form.cleaned_data.get('comment1')
            client.comment2 = form.cleaned_data.get('comment2')
            client.comment3 = form.cleaned_data.get('comment3')
            client.sel1 = form.cleaned_data.get('sel1')
            client.sel2 = form.cleaned_data.get('sel2')
            client.sel3 = form.cleaned_data.get('sel3')
            client.date = datetime.date.today()
            client.user = request.user
            client.save()

    return HttpResponseRedirect('/view?page=1')

@login_required
def editInfo(request, id):
    try:
        data = dict()
        client = ClientModelB.objects.get(id=id)

        data['clients'] = client
        print(1)
        if request.method == 'POST':
            form = ClientForm(request.POST, request.FILES)
            if form.is_valid():
                client.firstName = form.cleaned_data.get('firstName')
                client.secondName = form.cleaned_data.get('secondName')
                client.middleName = form.cleaned_data.get('middleName')
                client.age = form.cleaned_data.get('age')
                client.address = form.cleaned_data.get('address')
                client.mail = form.cleaned_data.get('mail')
                client.imgBefore = form.cleaned_data.get('imgBefore')
                client.imgAfter = form.cleaned_data.get('imgAfter')
                client.comment1 = form.cleaned_data.get('comment1')
                client.comment2 = form.cleaned_data.get('comment2')
                client.comment3 = form.cleaned_data.get('comment3')
                client.sel1 = form.cleaned_data.get('sel1')
                client.sel2 = form.cleaned_data.get('sel2')
                client.sel3 = form.cleaned_data.get('sel3')
                client.save()
                return HttpResponseRedirect('/view?page=1')
        else:
            data['form'] = ClientForm()
            return render(request, 'main/client_information_edit.html', data)
    except ClientModelB.DoesNotExist:
        return HttpResponseRedirect('/view?page=1')

@login_required
def deleteInfo(request, id):
    try:
        client = ClientModelB.objects.get(id=id)
        client.delete()
        return HttpResponseRedirect('/view?page=1')
    except ClientModelB.DoesNotExist:
        return HttpResponseRedirect('/view?page=1')

@login_required
def fullInfo(request, id):
    try:
        data = dict()
        client = ClientModelB.objects.get(id=id)
        data['clients'] = client

        return render(request, 'main/client_information_full.html', data)
    except ClientModelB.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")