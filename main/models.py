from django.db import models


class Accounts(models.Model):
    """ Models did not used."""
    username = models.CharField(max_length=20)
    followers = models.IntegerField()
    following = models.IntegerField()
    description = models.CharField(max_length=160)


class LastTweets(models.Model):
    """ Models did not used."""
    user = models.OneToOneField(Accounts, on_delete=models.CASCADE, primary_key=True)
    tweet = models.CharField(max_length=240)
    date = models.DateField()
