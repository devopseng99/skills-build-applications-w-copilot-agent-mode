import logging
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta, date
from bson import ObjectId

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating test data...')

        # Create users
        users = [
            User(email='john.smith@school.edu', name='John Smith', age=16, team='Red Team'),
            User(email='sarah.wilson@school.edu', name='Sarah Wilson', age=17, team='Blue Team'),
            User(email='mike.johnson@school.edu', name='Mike Johnson', age=16, team='Red Team'),
            User(email='emily.brown@school.edu', name='Emily Brown', age=17, team='Blue Team')
        ]
        User.objects.bulk_create(users)
        self.stdout.write('Created users')

        # Create teams
        teams = [
            Team(name='Red Team', members=['john.smith@school.edu', 'mike.johnson@school.edu']),
            Team(name='Blue Team', members=['sarah.wilson@school.edu', 'emily.brown@school.edu'])
        ]
        Team.objects.bulk_create(teams)
        self.stdout.write('Created teams')

        # Create activities
        activities = [
            Activity(user='john.smith@school.edu', type='Running', duration=30, date=date.today()),
            Activity(user='sarah.wilson@school.edu', type='Swimming', duration=45, date=date.today()),
            Activity(user='mike.johnson@school.edu', type='Basketball', duration=60, date=date.today()),
            Activity(user='emily.brown@school.edu', type='Volleyball', duration=40, date=date.today())
        ]
        Activity.objects.bulk_create(activities)
        self.stdout.write('Created activities')

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user='john.smith@school.edu', points=120),
            Leaderboard(user='sarah.wilson@school.edu', points=150),
            Leaderboard(user='mike.johnson@school.edu', points=100),
            Leaderboard(user='emily.brown@school.edu', points=130)
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)
        self.stdout.write('Created leaderboard entries')

        # Create workouts
        workouts = [
            Workout(name='Morning Cardio', description='30-minute cardio workout including running and jumping jacks'),
            Workout(name='Swim Training', description='45-minute swimming session focusing on freestyle and backstroke'),
            Workout(name='Basketball Drills', description='1-hour basketball practice with shooting and dribbling drills'),
            Workout(name='Volleyball Practice', description='40-minute volleyball session working on serves and spikes')
        ]
        Workout.objects.bulk_create(workouts)
        self.stdout.write('Created workouts')

        self.stdout.write(self.style.SUCCESS('Successfully populated database with test data'))