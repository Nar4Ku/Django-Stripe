from stripeKeys import STRIPE_PRIVATE_KEY, STRIPE_PUBLIC_KEY 
from django.shortcuts import render
from django.http import JsonResponse
import stripe
import json

stripe_pub = STRIPE_PUBLIC_KEY          # Settando com a Chave Publica
stripe_private = STRIPE_PRIVATE_KEY     # Settando com a Chave Privada

stripe.api_key = stripe_private         # Atribuindo a chave privada ao artibuto api_key


def home(request):
    import math

    amount = 17210
    if request.method == 'POST':
        print(request.POST['payment'])
        if request.POST['payment'] == 1:
            centavos = request.POST['valParcelas']
            amount = math.trunc((float(centavos)*100))
        else:
            centavos = request.POST['valVista']
            amount = math.trunc((float(centavos)*100))
        print("valor em centavos", amount)

    # Valores que estaram no modal do cartão --Modificar
    btn_title = "Modal"
    titulo = 'Titulo Modal'
    subtitulo = 'SubTitulo Modal'
    imagem = 'https://stripe.com/img/documentation/checkout/marketplace.png'
    btn_modal_title = 'Pagar'

    context = {
        'key': stripe_pub,            #Passando a chave publica para variavel de contexto
        'amount': amount,
        'modalTitle' : titulo,
        'modalSubTitle': subtitulo,
        'img': imagem,
        'btn_title': btn_title,
        'btn_modal_title': btn_modal_title
    }

    return render(request, 'home.html', context)


def checkout(request):

    # from stripe import
    token  = request.POST['stripeToken']
    
    # Criando um pedido de compra
    try:
        charge = stripe.Charge.create(
            amount = 500,                   #Deixar Dinamico depois
            currency = 'brl',  
            description = 'Some descrip',    #Deixar Dinamico depois
            card = token,
            # metadata={'order_id': 'ID_transation'}
        )

    except:
        print('Handler error')

    return JsonResponse(charge)    # Obtendo o return in Json para verificação dos attrs

    # context = {
    #     'token': token,
    # }
    #return render(request, 'success.html', context)


    # 4% + 0.50