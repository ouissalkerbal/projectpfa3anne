#views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import TypeDeCable, TypeDeConnecteurs, PurchaseOrder, SimpleMessage
from .forms import PurchaseOrderForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



def home(request):
    return render(request, 'index.html')

def service_commercial(request):
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            print(form.cleaned_data)
            
            type_de_connecteurs_id = form.cleaned_data['type_de_connecteurs']
            type_de_connecteurs = TypeDeConnecteurs.objects.get(id=type_de_connecteurs_id)

            type_de_cable_id = form.cleaned_data['type_de_cable']
            type_de_cable = TypeDeCable.objects.get(id=type_de_cable_id)

            purchase_order = PurchaseOrder(
                n_commande=form.cleaned_data['n_commande'],
                nombre_de_jaretiere=form.cleaned_data['nombre_de_jaretiere'],
                type_de_cable=type_de_cable,  # Assign the TypeDeCable instance
                type_de_connecteurs=type_de_connecteurs,  # Assign the TypeDeConnecteurs instance
                delai_de_livraison=form.cleaned_data['delai_de_livraison'],
                metrage=form.cleaned_data['metrage'],
                date_field=form.cleaned_data['date_field'],
                city=form.cleaned_data['city_field'],
                viewed=False
            )
            
            purchase_order.save()
            # Rename 'messages' variable to 'success_message' to avoid conflict
            success_message = "Commande enregistrée avec succès!"
            messages.success(request, success_message)  # French message
            return redirect('app:service_commercial')  # Redirect to the same page
        else:
            print("Form is invalid")
            print(form.errors)
    else:
        form = PurchaseOrderForm()

    # Rename 'messages' variable to 'message_list' to avoid conflict
    message_list = SimpleMessage.objects.all()
    
    types_de_cable = TypeDeCable.objects.all()
    types_de_connecteurs = TypeDeConnecteurs.objects.all()

    context = {
        'form': form,
        'types_de_cable': types_de_cable,
        'types_de_connecteurs': types_de_connecteurs,
        'message_list': message_list,  # Update variable name here
    }
    return render(request, 'service_commercial.html', context)


def service_atelier(request):
    atelier_orders = PurchaseOrder.objects.all()
    unviewed_purchase_orders = PurchaseOrder.objects.filter(viewed=False)  # Add this line

    if request.method == 'POST':
        order_id = request.POST.get('order_id')  # Assuming you have an input with the order ID in your form
        purchase_order = PurchaseOrder.objects.get(pk=order_id)

        if 'confirm' in request.POST:
            purchase_order.confirmed = True
            purchase_order.not_confirmed = False
        elif 'not_confirm' in request.POST:
            purchase_order.confirmed = False
            purchase_order.not_confirmed = True

        purchase_order.save()

    context = {
        'atelier_orders': atelier_orders,
        'unviewed_purchase_orders': unviewed_purchase_orders,  # Add this line
    }
    return render(request, 'atelier.html', context)

def purchase_order_detail(request, purchase_order_id):
    purchase_order = get_object_or_404(PurchaseOrder, pk=purchase_order_id)
    return render(request, 'purchase_order_detail.html', {'purchase_order': purchase_order})

def bon_de_commande(request):
    atelier_orders = PurchaseOrder.objects.order_by('-date_field')  # Order by date_field in descending order
    context = {'atelier_orders': atelier_orders}
    return render(request, 'bon_de_commande.html', context)

def notifications_view(request):
    unviewed_purchase_orders = PurchaseOrder.objects.filter(viewed=False)

    # Mark fetched purchase orders as viewed
    for purchase_order in unviewed_purchase_orders:
        purchase_order.viewed = True
        purchase_order.save()

    context = {
        'unviewed_purchase_orders': unviewed_purchase_orders,
    }
    return render(request, 'notifications.html', context)

@csrf_exempt
def save_message(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')

        # Save the message in the database
        SimpleMessage.objects.create(message=message)

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})

def fetch_messages(request):
    # Retrieve new messages (messages with viewed=False)
    new_messages = SimpleMessage.objects.filter(viewed=False)

    # Mark fetched messages as viewed
    for message in new_messages:
        message.viewed = True
        message.save()

    # Prepare the response data
    messages_data = [{'message': message.message} for message in new_messages]

    return JsonResponse({'messages': messages_data})