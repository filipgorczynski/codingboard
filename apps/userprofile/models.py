from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, related_name="userpfrofile", on_delete=models.CASCADE
    )
    is_employer = models.BooleanField(default=False)


User.userprofile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])