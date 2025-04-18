import logging
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        try:
            # Connect to MongoDB
            client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
            db = client[settings.DATABASES['default']['NAME']]

            # Drop existing collections
            db.users.drop()
            logger.info("Dropped users collection.")
            db.teams.drop()
            logger.info("Dropped teams collection.")
            db.activity.drop()
            logger.info("Dropped activity collection.")
            db.leaderboard.drop()
            logger.info("Dropped leaderboard collection.")
            db.workouts.drop()
            logger.info("Dropped workouts collection.")

            # Create users
            users = [
                User(email='john.doe@example.com', name='John Doe', age=16, team='Team A'),
                User(email='jane.smith@example.com', name='Jane Smith', age=17, team='Team B')
            ]
            User.objects.bulk_create(users)
            logger.info("Created users.")

            # Create teams
            teams = [
                Team(name='Team A', members=['john.doe@example.com']),
                Team(name='Team B', members=['jane.smith@example.com'])
            ]
            Team.objects.bulk_create(teams)
            logger.info("Created teams.")

            # Create activities
            activities = [
                Activity(user='john.doe@example.com', type='Running', duration=30, date='2025-04-12'),
                Activity(user='jane.smith@example.com', type='Cycling', duration=45, date='2025-04-12')
            ]
            Activity.objects.bulk_create(activities)
            logger.info("Created activities.")

            # Create leaderboard entries
            leaderboard_entries = [
                Leaderboard(user='john.doe@example.com', points=100),
                Leaderboard(user='jane.smith@example.com', points=120)
            ]
            Leaderboard.objects.bulk_create(leaderboard_entries)
            logger.info("Created leaderboard entries.")

            # Create workouts
            workouts = [
                Workout(name='Morning Run', description='A quick 5km run to start the day.'),
                Workout(name='Evening Yoga', description='Relaxing yoga session to wind down.')
            ]
            Workout.objects.bulk_create(workouts)
            logger.info("Created workouts.")

            self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
        except Exception as e:
            logger.error(f"Error populating the database: {e}")

class Command(BaseCommand):
    help = 'Populate the leaderboard collection with sample data'

    def handle(self, *args, **kwargs):
        sample_data = [
            {"user": "john.doe@example.com", "points": 150},
            {"user": "jane.smith@example.com", "points": 200},
        ]

        for entry in sample_data:
            try:
                Leaderboard.objects.update_or_create(user=entry["user"], defaults={"points": entry["points"]})
                logger.info(f"Successfully added/updated entry: {entry}")
            except Exception as e:
                logger.error(f"Error adding/updating entry {entry}: {e}")

        self.stdout.write(self.style.SUCCESS('Finished populating the leaderboard collection.'))