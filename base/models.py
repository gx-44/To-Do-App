from django.db import models
from django.contrib.auth.models import User

PRIORITY_CHOICES = (
    ('high', 'High'),
    ('medium', 'Medium'),
    ('low', 'Low'),
)

LABEL_CHOICES = (
    ('personal', 'Personal'),
    ('work', 'Work'),
    ('shopping', 'Shopping'),
)


class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    priority = models.CharField(
        max_length=6, choices=PRIORITY_CHOICES, default='high')
    label = models.CharField(
        max_length=8, choices=LABEL_CHOICES, default='personal')
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
