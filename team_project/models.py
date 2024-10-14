from django.db import models

class CaptchaModel(models.Model):
    email = models.EmailField(unique=True)
    captcha = models.CharField(max_length=4)
    create_time = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255)
    captcha = models.CharField(max_length=10)  # 视需求调整

    def __str__(self):
        return self.username
