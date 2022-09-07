from django.shortcuts import render
from wishlist.models import WishlistItem
def show_wishlist(request):
    data_wishlist_item = WishlistItem.objects.all()
    context = {
        'list_item': data_wishlist_item,
        'name': 'Raphael'
    }
    return render(request, "wishlist.html",context)

# Create your views here.
