from django.conf import settings
from django.db import models
from django.utils.timezone import now

from apps.base.models import BaseModel


class Budget(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Usuário',
        on_delete=models.CASCADE,
        db_index=True,
        related_name='budgets'
    )
    start_date = models.DateField('Início')
    end_date = models.DateField('Fim')

    def _is_active(self):
        return self.start_date <= now() <= self.end_date
    is_active = property(_is_active)

    class Meta:
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'
