from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def get_active_budget(self):
        return self.budgets.filter(is_active=True).first()

