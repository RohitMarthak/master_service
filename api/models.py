from django.db import models
from django.utils import timezone
import os
from uuid import uuid4
from django.core.exceptions import ValidationError

def master_category_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}.webp'
    return os.path.join('master_category_images', filename)

class MasterCategory(models.Model):
    name = models.CharField(max_length=255)
    priority = models.IntegerField(default=0)
    gender = models.CharField(max_length=100, default=' ')
    mastercategory_image = models.ImageField(upload_to=master_category_image, null=True, blank=True)  # Add the img field here
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        # Unique constraint for name based on gender
        unique_together = ['name', 'gender']

    def _str_(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.priority:
            # If priority is not set, assign the last priority + 1
            last_priority = MasterCategory.objects.all().order_by('-priority').first()
            self.priority = (last_priority.priority + 1) if last_priority else 1

        super().save(*args, **kwargs)


def master_service_image(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}.webp'
    return os.path.join('master_service_images', filename)

class MasterService(models.Model):
    service_name = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None)    
    categories = models.ForeignKey(MasterCategory, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=255, default=None, null=True, blank=True)
    priority = models.IntegerField(default=0)
    service_image = models.ImageField(upload_to=master_service_image, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    # price = models.FloatField(default=None)
    # service_time = models.CharField(max_length=255, default=None)
    # discount = models.FloatField(default=None)

    # class Meta:
    #     # Unique constraint for name based on gender
    #     unique_together = ['service_name', 'gender']

    def _str_(self):
        return self.service_name

    def save(self, *args, **kwargs):
        if not self.priority:
            # If priority is not set, assign the last priority + 1
            last_priority = MasterService.objects.filter(categories=self.categories).order_by('-priority').first()
            self.priority = (last_priority.priority + 1) if last_priority else 1

        super().save(*args, **kwargs)