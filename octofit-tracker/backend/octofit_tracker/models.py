from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.JSONField()

class Activity(models.Model):
    user = models.EmailField()
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    user = models.EmailField()
    points = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()