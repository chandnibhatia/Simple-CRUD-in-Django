from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views import generic
from .models import Client
from django.db.models import Q
from .forms import Client_DetailsForm, Client_DetailsUpdateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def getPaginator(request,object):
    page = request.GET.get('page', 1)
    paginator = Paginator(object, 5)
    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)
    return clients


def client_details(request):
    if request.POST:
        field_value = request.POST.get('value_placeholder')
        if field_value:
            clients = Client.objects.filter(
                Q(client_name__contains=field_value) | Q(email_address__contains=field_value) | Q(
                    phone_number__contains=field_value) | Q(suburb__contains=field_value))
        else:
            client_detail = Client.objects.order_by('client_name')
            clients = getPaginator(request,client_detail)

        return render(request, 'client_test/client_details.html', {'client_details': clients})

    else:
        client_detail = Client.objects.order_by('client_name')
        clients = getPaginator(request,client_detail)

        return render(request, 'client_test/client_details.html', {'client_details': clients})


def update_user(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = Client_DetailsUpdateForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Client_DetailsUpdateForm(instance=client)
        return render(request, 'client_test/update_user.html', {'form': form})


def user_new(request):
    if request.method == 'POST':
        form = Client_DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Client_DetailsForm()
        return render(request, 'client_test/user_update_add.html', {'form': form})


def delete_user(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('/')
