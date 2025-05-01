from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class auction(admin.ModelAdmin):
    list_display = ("id" , "user", "active_bool","title" , "desc" , "starting_bid" , "image_url" , "category")

class watchl(admin.ModelAdmin):
    list_display = ("id", "watch_list" , "user")

class bidadmin(admin.ModelAdmin):
    list_display = ("id","user","listingid","bid")

class CommentAdmin(admin.ModelAdmin):  # Correct the class name here
    list_display = ("id", "user", "comment", "listingid")

class win(admin.ModelAdmin):
    list_display = ("id","user", "bid_win_list")
class CustomUserAdmin(UserAdmin):
    # Ensure this line is properly indented
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_active")  # Customize as needed
    search_fields = ("username", "email")  # Fields to search
    ordering = ("username",)  # Default ordering


# Register your models here.
admin.site.register(auctionlist, auction)
admin.site.register(bids, bidadmin)
admin.site.register(comments, CommentAdmin)
admin.site.register(watchlist, watchl)
admin.site.register(winner, win)
admin.site.register(User, CustomUserAdmin)