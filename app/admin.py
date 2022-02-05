from re import search
from django.contrib import admin
from .models import Profile, Address

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'dob', 
        'gender',
        'phone_number',
    )
    list_filter = (
		'name',
        'gender',
	)
    list_editable = (
		'dob',
		'phone_number',
	)
    search_fields = (
		"name",
		)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        'address1', 
        'address2',
        'pincode',
    )
    list_editable = (
        'address2',
        'pincode',
    )
    search_fields = (
        'pincode',
    )