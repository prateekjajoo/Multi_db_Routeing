from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, UpdateView
from django.views.generic.edit import CreateView, DeleteView, View
from .models import Product, UserRole
from .forms import ProductForm, UserRoleForm
from django.contrib.auth import authenticate, login, logout
import unicodedata
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def email(reciver, message):
    """ This function for send mail it's get two parameters reciver email and message """
    subject = 'Username & password'
    message = message
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [reciver,]
    send_mail(subject, message, email_from, recipient_list )
    return HttpResponse("Successfully send mail")


class UserCreateView(LoginRequiredMixin, CreateView):
    """ This is user create view for user's creation """
    model = UserRole
    form_class = UserRoleForm

    def form_valid(self, form):
        user = form.save(commit=False)
        if form.is_valid():
            password = form.cleaned_data['password'] # for password encryption
            username = form.cleaned_data['username']
            user.set_password(password)
            for i in range(1, 6):   # to store all user in all five database
                db_name = "database{}".format(i)
                if db_name == "database1":
                    db_name = ''
                user.save(using=db_name)
            message = "Hello Please check your user name and password username= {} password = {}".format(username, password)
            email(username, message)
            messages.add_message(self.request, messages.SUCCESS, "Successfully Create User")  # Success message
            return redirect('user_create')

class LogoutView(View):
    """  Log out View for logout  """
    def get(self, request):
        logout(request)
        return redirect('user_login')


class UserListView(LoginRequiredMixin, ListView):
    """  User List View """
    model = UserRole


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """  User Update View"""
    model = UserRole
    form_class = UserRoleForm
    template_name = 'app/userrole_form.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        if form.is_valid():
            password = form.cleaned_data['password']
            user.set_password(password)
            for i in range(1, 6):
                db_name = "database{}".format(i)
                if db_name == "database1":
                    db_name = ''
                user.save(using=db_name)
            messages.add_message(self.request, messages.SUCCESS, "Successfully Update User")
            return redirect('user_list')


class UserDeleteView(LoginRequiredMixin, DeleteView):
    """ User Delete View for user deletion """
    def get(self, request, *args, **kwargs):
        id_ = self.kwargs['pk']
        for i in range(1, 6):
            db_name = "database{}".format(i)
            if db_name == "database1":
                db_name = ''
            UserRole.objects.using(db_name).get(id=id_).delete()

        messages.add_message(self.request, messages.warning, "Successfully Delete User")
        return redirect('user_list')


class AllProductListView(LoginRequiredMixin, ListView):
    """ All Product List View For admin  """
    model = Product
    template_name = 'app/product_list.html'

    def get(self, request, *args, **kwargs):
        final_list = {}
        for i in range(1, 6):
            db_name = "database{}".format(i)
            if db_name == "database1":
                db_name = 'default'
            final_list[db_name] = Product.objects.using(db_name).all()

        return render(request, 'app/product_list.html', {'final_list': final_list})


class UserLoginView(TemplateView):
    """ User Login View  """
    template_name = "app/login.html"

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            if request.user.is_superuser:  # check is user is super so its go superuser dashbord else normal user deshbord
                return redirect('user_create')
            else:
                return redirect('product_create')

        else:
            return render(request, 'app/login.html')

    def post(self, request):
        user_id = request.POST['username']
        user_password = request.POST['password']
        print(user_id)
        print(user_password)
        user = authenticate(username=user_id, password=user_password)
        if user:
            if user.is_superuser:
                login(request, user)
                messages.add_message(self.request, messages.SUCCESS, "Welcome Super User")
                return redirect('user_create')

            elif user:
                login(request, user)
                messages.add_message(self.request, messages.SUCCESS, "Welcome User")
                return redirect('product_create')

            else:
                message = "Invalid User Id "
                messages.add_message(self.request, messages.error, "Sorry You are Invalid user")
                return render(request, 'app/login.html', {"message": message})

        else:
            message = "Invalid User Id "
            return render(request, 'app/login.html', {"message": message})


class ProductCreateView(LoginRequiredMixin, CreateView):
    """ Product create view for product creation """
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        db_name = self.request.POST['db_name'].lower().strip()
        if db_name == 'database1':
            db_name = 'default'
        product_obj = form.save(commit=False)
        product_obj.user_id = self.request.user.id
        product_obj.save(using=db_name)
        messages.add_message(self.request, messages.SUCCESS, "Product Created Successfully")
        return redirect('product_create')

    def get_context_data(self, **kwargs):
        ctx = super(ProductCreateView, self).get_context_data(**kwargs)
        try:
            db_assign_list = UserRole.objects.get(id=self.request.user.id).db_assign
        except UserRole.DoesNotExist:
            raise Http404("Sorry, you can not add product here. if you want go to admin section !")
        # convert unicode to string and change string. and get list of assign database for perticular user
        db_assign_list = unicodedata.normalize('NFKD', db_assign_list).encode('ascii', 'ignore')
        db_assign_list = db_assign_list.replace('[', '').replace(']', '').replace('u', '').replace("'", '').split(',')
        ctx['db_list'] = db_assign_list

        final_list = {}
        """ Get list of pruduct of perticular user """
        for db_name in db_assign_list:
            db_name = db_name.strip()

            if db_name == 'database1':
                db_name = 'default'
            final_list[db_name] = Product.objects.using(db_name).filter(user=self.request.user)

        ctx['final_list'] = final_list
        return ctx


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """ For product update """
    model = Product
    form_class = ProductForm
    template_name = 'app/product_form.html'
    success_url = "app/pro-create/"

    def get_object(self, queryset=None):
        db_name = self.kwargs['string'].strip()
        id_ = self.kwargs['pk']
        obj = Product.objects.using(db_name).get(id=id_)
        obj.db = db_name
        return obj

    def form_valid(self, form):
        db_name = self.kwargs['string'].strip()
        if db_name == 'database1':
            db_name = 'default'
        product_obj = form.save(commit=False)
        product_obj.save(using=db_name)
        messages.add_message(self.request, messages.SUCCESS, "Product Update Successfully")
        if self.request.user.is_superuser:
            return redirect('pro_list')

        return redirect('product_create')


class ProductDeleteView(LoginRequiredMixin, DeleteView):

    """ For product delete view """

    model = Product

    def get(self, request, *args, **kwargs):
        db_name = self.kwargs['string'].strip()
        id_ = self.kwargs['pk']
        Product.objects.using(db_name).get(id=id_).delete()
        messages.add_message(self.request, messages.warning, "Product Deleted")
        if self.request.user.is_superuser:
            return redirect('pro_list')
        return redirect('product_create')

