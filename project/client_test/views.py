from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
#from django.views import generic
from .models import Client
from django.db.models import Q
from .forms import Client_DetailsForm, Client_DetailsUpdateForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.contrib import messages


# class AjaxTemplateMixin(object):
#     def dispatch(self, request, *args, **kwargs):
#         if not hasattr(self, 'ajax_template_name'):
#             split = self.template_name.split('.html')
#             split[-1] = '_inner'
#             split.append('.html')
#             self.ajax_template_name = ''.join(split)
#         if request.is_ajax():
#             self.template_name = self.ajax_template_name
#         return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)


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
        form = Client_DetailsForm()
        client_detail = Client.objects.order_by('client_name')
        clients = getPaginator(request,client_detail)

        return render(request, 'client_test/client_details.html', {'client_details': clients,'form':form})


def update_user(request, pk):
    client = get_object_or_404(Client, pk=pk)
    form = Client_DetailsUpdateForm(instance=client)
    return render(request, 'client_test/update_user.html', {'form': form,'pk':pk})

def save_updated_user(request):
    args = {}
    if request.method == 'POST':
        client = get_object_or_404(Client, email_address=request.POST.get("email_address"))
        form = Client_DetailsUpdateForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Updated Successfully.')
            return redirect('/')
    else:
        form = Client_DetailsUpdateForm()

    args['form'] = form
    return render(request, 'client_test/update_user.html', args)



def user_new(request):

    data = dict()

    if request.method == 'POST':
        form = Client_DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Added Successfully.')
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
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    messages.success(request, 'User Deleted Successfully.')
    return redirect('/')
