from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Item, Item_variation, Item_image, Category, Order, Status, Discount, OrderItem
import nested_admin



from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)
class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline, ]
    list_display = ['username','email','date_joined','is_active']
admin.site.register(User, UserProfileAdmin)


class Item_imageInline(nested_admin.NestedTabularInline):
    model = Item_image
    extra = 1
    ordering = ['num', ]


class Item_variationInline(nested_admin.NestedStackedInline):
    model = Item_variation
    inlines = [Item_imageInline, ]
    extra = 1
    ordering = ['num',]


class ItemAdmin(nested_admin.NestedModelAdmin):
    #inlines = [Item_variationInline,]
    inlines = [Item_variationInline,]
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('category',)
    # list_display = ('title', 'published_date', 'start_date', 'end_date', 'main_page')
    # list_editable = ['main_page', ]
    # list_filter = ['published_date', 'main_page']
    search_fields = ['title']
    list_display = ['title','new_flag']


admin.site.register(Item, ItemAdmin)

class CategoryAdmin(DjangoMpttAdmin):
    exclude = ('num',)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)



class DiscountAdmin(admin.ModelAdmin):
    inlines = []
    list_display = ['title','level1','level2','level3']
admin.site.register(Discount, DiscountAdmin)




class ItemInLineOrder(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('item','title','cols','price')
    extra = 0


    list_display = ('title','item','cols','price')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


    # def has_add_permission(self, request):
    #     return False
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False



class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id','created_date','total_price','status' )

    readonly_fields = ('email','address','phone_number','customer')

    inlines = [
        ItemInLineOrder,
    ]



admin.site.register(Order, OrdersAdmin)






#class OrderAdmin(admin.ModelAdmin):
    #pass
    # exclude=("customer ",)
    # readonly_fields=('customer', )


    # list_display = ('title', 'published_date', 'main_page')
    # list_editable = ['main_page', ]
    # list_filter = ['published_date', 'main_page']
    # search_fields = ['title', 'text']

#admin.site.register(Order, OrderAdmin)


#class StatusAdmin(admin.ModelAdmin):
    #list_display = ('title', 'num', 'default_status')
    #list_editable = ['default_status', ]

#admin.site.register(Status, StatusAdmin)


