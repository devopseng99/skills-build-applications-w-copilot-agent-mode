from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(email="test@example.com", name="Test User", age=20, team="Team A")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Team A", members=["test@example.com"])
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        activity = Activity.objects.create(user="test@example.com", type="Running", duration=30, date="2025-04-12")
        self.assertEqual(activity.type, "Running")

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(user="test@example.com", points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Morning Run", description="A quick 5km run to start the day.")
        self.assertEqual(workout.name, "Morning Run")