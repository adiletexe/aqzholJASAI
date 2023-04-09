from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import UserModel, Statistics

#mobile
@login_required
def next(request):
    drivers = UserModel.objects.all()
    return render(request, 'next.html', {'drivers':drivers})

@login_required
def info(request, info_pk):
    driver = get_object_or_404(UserModel, pk=info_pk)
    return render(request, 'info.html', {'driver':driver})

@login_required
def info2(request, info_pk):
    driver = get_object_or_404(UserModel, pk=info_pk)
    return render(request, 'info2.html', {'driver':driver})

@login_required
def info3(request, info_pk):
    driver = get_object_or_404(UserModel, pk=info_pk)

    sec0 = Statistics.objects.filter(second=0)
    s0 = sec0.first().numberofdrowsy

    sec1 = Statistics.objects.filter(second=10)
    s1 = sec1.first().numberofdrowsy

    sec2 = Statistics.objects.filter(second=20)
    s2 = sec2.first().numberofdrowsy

    sec3 = Statistics.objects.filter(second=30)
    s3 = sec3.first().numberofdrowsy

    sec4 = Statistics.objects.filter(second=40)
    s4 = sec4.first().numberofdrowsy

    s_list = []

    for i in [s0, s1, s2, s3, s4]:
        if i == 0:
            s_list.append(350)
        if i == 1:
            s_list.append(315)
        if i == 2:
            s_list.append(280)
        if i == 3:
            s_list.append(245)
        if i == 4:
            s_list.append(210)
        if i == 5:
            s_list.append(175)
        if i == 6:
            s_list.append(140)
        if i == 7:
            s_list.append(105)
        if i >= 8:
            s_list.append(70)

    s0 = s_list[0]
    s1 = s_list[1]
    s2 = s_list[2]
    s3 = s_list[3]
    s4 = s_list[4]

    context = {'driver':driver, 's0':s0, 's1':s1, 's2':s2, 's3':s3, 's4': s4}
    return render(request, 'info3.html', context)


def loginsystem(request):
    if request.method == "GET":
        return render(request, 'index.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('next')
        else:
            return render(request, 'index.html',
                          {'form': AuthenticationForm, 'error': 'Неверный логин и/или пароль'})


#comp
@login_required
def nextcomp(request):
    drivers = UserModel.objects.all()
    return render(request, 'nextcomp.html', {'drivers':drivers})

@login_required
def infocomp(request, info_pk):
    driver = get_object_or_404(UserModel, pk=info_pk)
    return render(request, 'infocomp.html', {'driver':driver})

@login_required
def info2comp(request, info_pk):
    driver = get_object_or_404(UserModel, pk=info_pk)
    return render(request, 'info2comp.html', {'driver':driver})

@login_required
def info3comp(request, info_pk):
    driver = get_object_or_404(UserModel, pk=info_pk)

    sec0 = Statistics.objects.filter(second=0)
    s0 = sec0.first().numberofdrowsy

    sec1 = Statistics.objects.filter(second=10)
    s1 = sec1.first().numberofdrowsy

    sec2 = Statistics.objects.filter(second=20)
    s2 = sec2.first().numberofdrowsy

    sec3 = Statistics.objects.filter(second=30)
    s3 = sec3.first().numberofdrowsy

    sec4 = Statistics.objects.filter(second=40)
    s4 = sec4.first().numberofdrowsy

    s_list = []

    for i in [s0, s1, s2, s3, s4]:
        if i == 0:
            s_list.append(450)
        if i == 1:
            s_list.append(400)
        if i == 2:
            s_list.append(355)
        if i == 3:
            s_list.append(310)
        if i == 4:
            s_list.append(265)
        if i == 5:
            s_list.append(220)
        if i == 6:
            s_list.append(175)
        if i == 7:
            s_list.append(130)
        if i >= 8:
            s_list.append(85)

    s0 = s_list[0]
    s1 = s_list[1]
    s2 = s_list[2]
    s3 = s_list[3]
    s4 = s_list[4]

    context = {'driver':driver, 's0':s0, 's1':s1, 's2':s2, 's3':s3, 's4': s4}
    return render(request, 'info3comp.html', context)


# auth
def loginsystemcomp(request):
    if request.method == "GET":
        return render(request, 'indexcomp.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('nextcomp')
        else:
            return render(request, 'indexcomp.html',
                          {'form': AuthenticationForm, 'error': 'Неверный логин и/или пароль'})

@login_required
def logoutsystem(request):
    if request.method == "GET":
        logout(request)
        return redirect('loginsystem')

@login_required
def logoutsystemcomp(request):
    if request.method == "GET":
        logout(request)
        return redirect('loginsystemcomp')