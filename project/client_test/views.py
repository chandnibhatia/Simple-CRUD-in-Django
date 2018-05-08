from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Client, Country, State, City
from django.db.models import Q
from .forms import Client_DetailsForm, Client_DetailsUpdateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.contrib import messages


def getPaginator(request, object):
    page = request.GET.get('page', 1)
    paginator = Paginator(object, 5)
    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        clients = paginator.page(1)
    except EmptyPage:
        clients = paginator.page(paginator.num_pages)
    return clients


def get_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country=country_id).order_by('name')
    return render(request, 'client_test/states.html', {'states': states})


def get_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state=state_id).order_by('name')
    return render(request, 'client_test/cities.html', {'cities': cities})


def client_details(request):
    if request.POST:
        field_value = request.POST.get('value_placeholder')
        if field_value:
            clients = Client.objects.filter(
                Q(client_name__contains=field_value) | Q(email_address__contains=field_value) | Q(
                    phone_number__contains=field_value) | Q(suburb__contains=field_value) | Q(
                    mobile_number__contains=field_value))
        else:
            client_detail = Client.objects.order_by('client_name')
            clients = getPaginator(request, client_detail)

        return render(request, 'client_test/client_details.html', {'client_details': clients})

    else:
        form = Client_DetailsForm()
        client_detail = Client.objects.order_by('client_name')
        clients = getPaginator(request, client_detail)

        return render(request, 'client_test/client_details.html', {'client_details': clients, 'form': form})


def save_updated_user(request):
    data = dict()

    if request.method == 'POST':

        client = get_object_or_404(Client, email_address=request.POST.get("email_address"))
        form = Client_DetailsUpdateForm(request.POST, instance=client)
        if form.is_valid():
            
            form.save()
            return redirect('/')
        else:
            data['form_is_valid'] = False

    context = {'form': form}
    data['html_form'] = render_to_string('client_test/user_update_add.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def get_updated_user(request, pk):
    data = dict()
    client = get_object_or_404(Client, pk=pk)
    form = Client_DetailsUpdateForm(instance=client)


    context = {'form': form}
    data['html_form'] = render_to_string('client_test/user_update_add.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)

    # args = {}
    # if request.method == 'POST':
    #     client = get_object_or_404(Client, email_address=request.POST.get("email_address"))
    #     form = Client_DetailsUpdateForm(request.POST, instance=client)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'User Updated Successfully.')
    #         return redirect('/')
    # else:
    #     form = Client_DetailsUpdateForm()
    #
    # args['form'] = form
    # return render(request, 'client_test/update_user.html', args)


def user_new(request):
    data = dict()

    if request.method == 'POST':

        print(request.POST)
        form = Client_DetailsForm(request.POST)
        if form.is_valid():
            #form.cleaned_data()
            form.save()
            return redirect('/')
        else:
            data['form_is_valid'] = False
    else:
        form = Client_DetailsForm()

    context = {'form': form}
    data['html_form'] = render_to_string('client_test/user_update_add.html',
                                         context,
                                         request=request
                                         )
    return JsonResponse(data)


def delete_user(request, pk):

    try:
        client = get_object_or_404(Client, pk=pk)
        client.delete()
        messages.success(request, 'User Deleted Successfully.')
        return redirect('/')
    except Exception:
        raise
