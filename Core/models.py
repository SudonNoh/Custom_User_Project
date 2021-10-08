from django.db import models


class TimeStampedModel(models.Model):
    # A timestamp representing when this object was created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # A timestap representing when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        # This class will become base of a Abstract Class
        abstract =True
        ordering = ['-created_at', '-updated_at']