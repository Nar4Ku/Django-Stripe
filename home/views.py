from stripeKeys import STRIPE_PRIVATE_KEY, STRIPE_PUBLIC_KEY 
from django.shortcuts import render
from django.http import JsonResponse
import stripe
import json

stripe_pub = STRIPE_PUBLIC_KEY          # Settando com a Chave Publica
stripe_private = STRIPE_PRIVATE_KEY     # Settando com a Chave Privada

stripe.api_key = stripe_private         # Atribuindo a chave privada ao artibuto api_key


def home(request):
    
    # print('Key: {}'.format(stripe_pub))
        
    context = {
        'key': stripe_pub,            #Passando a chave publica para variavel de contexto
    }

    return render(request, 'home.html', context)


def checkout(request):

    # from stripe import
    
    token  = request.POST['stripeToken']
    
    # Criando um  comprador e puxando os dados do formulário 
    # customer = stripe.Customer.create(
    #     email = request.POST['stripeEmail'],
    #     source = token
    # )

    # Criando um pedido de compra
    try:
        charge = stripe.Charge.create(
            # customer = customer.id,
            amount = 500,                   #Deixar Dinamico depois
            currency = 'usd',               #'brl' real   
            description = 'Some descrip',    #Deixar Dinamico depois
            card = token
        )

        x = charge.save()
        if charge.save():
            print('\nfoi??')
            # print(x)
    except:
        print('foi não')

    return JsonResponse(charge)    # Obtendo o return in Json para verificação dos attrs

    # context = {
    #     'token': token,
    # }
    #return render(request, 'success.html', context)