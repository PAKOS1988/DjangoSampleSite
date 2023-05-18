from django.shortcuts import render, redirect
from .models import *
from .forms import *
from telebot import TeleBot

bot=TeleBot('6219829235:AAEAsYwaJYXkMoHD-GnT-evNfv0j0sWEDmc', parse_mode='HTML')

# Create your views here.
def index(request):
    all_categories = Category.objects.all()
    all_products = Product.objects.all()
    search_bar = serchproduct()
    context1 = {'all_categories': all_categories, 'all_products': all_products, 'form': search_bar}
    #Получение значения введенное в поисковой строке сайта
    if request.method == 'POST':
        prod_find = request.POST.get('seachproduct')
        print(prod_find)
        try:
            search_result = Product.objects.get(prod_name=prod_find)
            return redirect(f'/item/{search_result.id}')
        except:
            return redirect('/')
    # from_frontend = request.GET.get('exact_product')
    #
    # #Проверка на ввод данных в поисковике
    # if from_frontend is not None:
    #     all_products = Product.objects.filter(prod_name=from_frontend)
    #     print(all_products)
    # else:
    #     pass

    return render(request,'Index.html', context1)

def current_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product':product}
    return render(request, 'about_product.html', context)

def get_exact_category(request,pk):
    exact_category = Category.objects.get(id=pk)
    categories = Category.objects.all()
    category_products = Product.objects.filter(prod_coteg=exact_category)
    return render(request, 'categrory_products.html',{'category_products':category_products, 'categories':categories})

def get_exact_product(request,pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    if request.method == "POST":
        Cart.objects.create(cart_user_id=request.user.id,
                              cart_prod_name=product,
                              cart_prod_quantity=request.POST.get("cart_prod_quantity"),
                              cart_prod_total=product.prod_price * int(request.POST.get('cart_prod_quantity')))
        return redirect('/cart')

    return render(request, 'about_product.html', context)

# def get_cart_product(request,pk):
#     exact_product_incart = Product.objects.get(id=pk)
#     if request.method == 'POST':
#         Cart.objects.create(cart_user_id=request.user.id,
#                             cart_prod_name=exact_product_incart,
#                             cart_prod_quantity=request.POST.get('user_product_quantity'),
#                                        tcart_prod_total=exact_product_incart.prod_price*int(request.POST.get('user_product_quantity')))
#     return redirect('/cart')

def get_user_cart(request):
    cart = Cart.objects.filter(cart_user_id=request.user.id)
    total = sum([i.cart_prod_total for i in cart])
    return render(request, 'user_cart.html', {'cart': cart, "total": total})


def complete_order(request):
    #получвем корзину пользователя по айди пользователя
    user_cart = Cart.objects.filter(cart_user_id = request.user.id)
    # формируем сообщения для тг админа
    result_message='Новый заказ(сайт)\n\n'
    total_for_all_cart=0
    for cart in user_cart:
        result_message += f'<b>{cart.cart_prod_name}</b> x {cart.cart_prod_quantity} = {cart.cart_prod_total} сум\n'
        total_for_all_cart += cart.cart_prod_total

    result_message += f'\n----------\n<b>ИТОГО: {total_for_all_cart}сум</b>'
    #Отправляем админу сообщение в тг
    bot.send_message(1268659822, result_message)
    user_cart.delete()
    return redirect('/')