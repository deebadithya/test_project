from django.db import models

# Create your models here.
class Organisation(models.Model):
    name = models.CharField(null=False)
    status = models.IntegerField(default=0, null=False)
    personal = models.BooleanField(default=False, null=True)
    settings = models.JSONField(default={}, null=True)
    created_at = models.BigIntegerField(null=True)
    updated_at = models.BigIntegerField(null=True)

class User(models.Model):
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(unique=False, null=False)
    profile = models.JSONField(default={}, null=False)
    status = models.IntegerField(default=0, null=False)
    setttings = models.JSONField(default={}, null=True)
    created_at = models.BigIntegerField(null=True)
    updated_at = models.BigIntegerField(null=True)

class Role(models.Model):
    name = models.CharField(null=False)
    description = models.CharField(null=True)
    org_id = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=False)


class Member(models.Model):
    org_id = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, null=False)
    status = models.IntegerField(null=False, default=0)
    settings = models.JSONField(default={}, null=True)
    created_at = models.BigIntegerField(null=True)
    updated_at = models.BigIntegerField(null=True)
