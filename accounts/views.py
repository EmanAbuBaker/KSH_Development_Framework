from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User, UserManager 
from django.contrib.auth import login as log_in, get_user, get_user_model
from django.http import HttpResponse, request
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic.edit import UpdateView , DeleteView
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import get_user, get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import  get_user, get_user_model
from django.shortcuts import redirect


#from accounts.forms import RegistrationForm,AccountAuthenticationForm, AccountUpdateForm
from accounts.models import Account






# view the list of the users.
class usersListView(PermissionRequiredMixin,generic.ListView):
#class usersListView(generic.ListView):

    permission_required = 'catalog.can_mark_returned'
    model = User
    template_name ='accounts/user_list.html'



# view details of the specific user.
class UserDetailView(generic.DetailView):
    model = User
    template_name ='accounts/user_detail.html'



# update specific user with specific fields.
class UserUpdate(UpdateView):
    model = User
    fields =['is_active','is_staff','is_superuser','groups','user_permissions']
    success_url = reverse_lazy('user_list')



# delete specific user.
class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('user_list')



def my_view(request):
    output = _("Welcome to my site.")
    return HttpResponse(output)
