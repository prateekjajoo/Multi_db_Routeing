from django.conf.urls import url
from .views import ProductCreateView, UserLoginView, UserCreateView, UserListView, ProductUpdateView, ProductDeleteView
from .views import UserUpdateView, UserDeleteView, AllProductListView, LogoutView, email
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'pro-create/', ProductCreateView.as_view(), name="product_create"),
    url(r'pro-update/(?P<pk>[\w-]+)/(?P<string>[\w\-]+)$', ProductUpdateView.as_view(), name="product_update"),
    url(r'pro-delete/(?P<pk>[\w-]+)/(?P<string>[\w\-]+)$', ProductDeleteView.as_view(), name="product_delete"),
    url(r'user-update/(?P<pk>[\w-]+)/$', UserUpdateView.as_view(), name="user_update"),
    url(r'user-delete/(?P<pk>[\w-]+)/$', UserDeleteView.as_view(), name="user_delete"),
    url(r'user-create/', UserCreateView.as_view(), name="user_create"),
    url(r'user-list/', UserListView.as_view(), name="user_list"),
    url(r'pro-list/', AllProductListView.as_view(), name="pro_list"),
    url(r'login', UserLoginView.as_view(), name="user_login"),
    url("logout", LogoutView.as_view(), name="logout"),
    url("email", email, name="email"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
