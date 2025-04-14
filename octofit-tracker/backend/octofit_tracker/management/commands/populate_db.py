from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create users
        users = [
            User(email='john.doe@example.com', name='John Doe', age=16, team='Team A'),
            User(email='jane.smith@example.com', name='Jane Smith', age=17, team='Team B')
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(name='Team A', members=['john.doe@example.com']),
            Team(name='Team B', members=['jane.smith@example.com'])
        ]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(user='john.doe@example.com', type='Running', duration=30, date='2025-04-12'),
            Activity(user='jane.smith@example.com', type='Cycling', duration=45, date='2025-04-12')
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user='john.doe@example.com', points=100),
            Leaderboard(user='jane.smith@example.com', points=120)
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Morning Run', description='A quick 5km run to start the day.'),
            Workout(name='Evening Yoga', description='Relaxing yoga session to wind down.')
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))