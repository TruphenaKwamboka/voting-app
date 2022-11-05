from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Voter(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="voter")
    personal_id = models.CharField(max_length=254, blank=False)
    department = models.CharField(max_length=254, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ["-created_date"]

        db_table = "Poll Voters"

    def __str__(self) -> str:
        
        return self.user.username