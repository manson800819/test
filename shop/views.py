from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Category, Product, Type1


global category
category=None
def product_list(request, category_slug=None):
    print(1)
    global category
    category = None
    categories = Category.objects.all()
    types = Type1.objects.all()
    products = Product.objects.filter(available=True)

    return render(request,
                      'shop/product/list.html',
                      {'category': category,
                       'categories': categories,
                       'products': products,
                       'types':types})

def product_list2(request, category_slug=None):
    categories = Category.objects.all()
    # types = Type1.objects.all()
    products = Product.objects.filter(available=True)
    a = 1
    global category
    category = get_object_or_404(Category, slug=category_slug)
    print(category)
    products = products.filter(category=category)

    types_id =Category.objects.filter(name = category).values_list('products_c__name')

    types_id = Product.objects.filter(name__in=types_id).values_list('type1_id').order_by('type1_id').distinct()

    types = Type1.objects.filter(id__in=types_id)
    print(123,types_id)
    return render(request,
                  'shop/product/list2.html',
                  {'category': category,
                       'categories': categories,
                       'products': products,
                       'types': types,"a":a})


def product_detail(request, product_id,slug_, slug):
    product = get_object_or_404(Product,
                                id=product_id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def product_list1(request, category_slug=None,type_slug=None):
    print(5)
    a = 0
    print(type_slug)
    print(category_slug)
    global category
    print( category )
    categories = Category.objects.all()
    types = Type1.objects.filter(available=True)

    products = Product.objects.filter(available=True)
    # category = get_object_or_404(Category, slug=category_slug)

    type1 = get_object_or_404(Type1, slug=type_slug)

    # types = types.filter(category=category)
    products = products.filter(category=category)
    print(products)

    products = products.filter(type1=type1)

    types_id =Category.objects.filter(name = category).values_list('products_c__name')

    types_id = Product.objects.filter(name__in=types_id).values_list('type1_id').order_by('type1_id').distinct()

    types = Type1.objects.filter(id__in=types_id)
    print(products)



    return render(request,
                  'shop/product/list_cat.html',{'category': category,
                       'categories': categories,
                       'products': products,
                       'types': types,"a":a,
                                                'type1':type1})