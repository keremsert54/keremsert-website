from django.db import models
from core.models import AbstractModel


# Create your models here.

class Message(AbstractModel):
    name = models.CharField(
        default='',
        max_length=250,
        verbose_name='Name',
        help_text='',
        blank=True,
    )
    email = models.EmailField(
        default='',
        max_length=254,
        verbose_name='Email',
        help_text='',
        blank=True,
    )
    subject = models.CharField(
        default='',
        max_length=254,
        verbose_name='Subject',
        help_text='',
        blank=True,
    )
    message = models.TextField(
        default='',
        verbose_name='Message',
        help_text='',
        blank=True,
    )

    def __str__(self):
        return f'Message: {self.name}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        ordering = ('name',)
