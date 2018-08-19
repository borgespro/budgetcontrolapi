from django.conf import settings
from django.db import models

from apps.base.models import BaseModel


class Category(BaseModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='Usuário',
        on_delete=models.CASCADE,
        db_index=True,
        related_name='categories'
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, related_name='children')
    name = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        unique_together = ('user', 'name',)
