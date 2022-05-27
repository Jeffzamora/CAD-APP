from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models
from django.forms import model_to_dict
from crum import get_current_request
from app import settings
from cad.cliente.models import Customer


class User(AbstractUser):
    token = models.UUIDField(primary_key=False, editable=False, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True,
                                 verbose_name="Cliente")

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'groups', 'user_permissions', 'last_login'])
        item['last_login'] = '' if self.last_login is None else self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['full_name'] = self.get_full_name()
        item['groups'] = [{'id': g.id, 'name': g.name} for g in self.groups.all()]
        item['customer'] = self.customer.name
        return item

    def get_group_session(self):
        try:
            request = get_current_request()
            groups = self.groups.all()
            if groups.exists():
                if 'group' not in request.session:
                    request.session['group'] = groups[0]
        except:
            pass
