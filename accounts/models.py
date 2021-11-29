from django.db import models
from django.contrib.auth.models import AbstractBaseUser , UserManager



# create new model to deal with user ,
# this model is dynamics, we could extend it in demand.
class Account (AbstractBaseUser):

    def __str__(self):
        return self.username
    

