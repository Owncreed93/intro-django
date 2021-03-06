from django.db import models


class Course(models.Model):
    created_at = models.DateTimeField(
        auto_now_add = True
    )
    name = models.CharField(max_length =  180, default = None)
    description = models.TextField(default = None)


    def __str__(self):
        return self.name
