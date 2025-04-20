from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user')
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user')
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()