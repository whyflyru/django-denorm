# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
try:
    from django.contrib.contenttypes.fields import GenericForeignKey
except ImportError:
    from django.contrib.contenttypes.generic import GenericForeignKey
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class DirtyInstance(models.Model):
    """
    Holds a reference to a model instance that may contain inconsistent data
    that needs to be recalculated.
    DirtyInstance instances are created by the insert/update/delete triggers
    when related objects change.
    """
    class Meta:
        app_label="denorm"

    content_type = models.ForeignKey(ContentType)
    object_id = models.CharField(blank=True, null=True, db_index=True, max_length=32)
    content_object = GenericForeignKey()

    def __str__(self):
        return 'DirtyInstance: %s,%s' % (self.content_type, self.object_id)
