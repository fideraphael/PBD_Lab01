from django.shortcuts import render
from wishlist.models import WishlistItem
def show_wishlist(request):
    return render(request, "wishlist.html",context)
data_wishlist_item = WishlistItem.objects.all()
context = {
    'list_item': data_wishlist_item,
    'name': 'Raphael'
}
# Create your views here.
