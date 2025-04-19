from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
import os

# API version configuration
API_VERSION = os.getenv('API_VERSION', 'v1')
API_SUB_PATH = f'api/{API_VERSION}/'

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://congenial-space-happiness-4pxppj9gg37rr9-8000.app.github.dev/'
    return Response({
        'message': 'Welcome to OctoFit Tracker API',
        'endpoints': {
            'users': base_url + API_SUB_PATH + 'users/',
            'teams': base_url + API_SUB_PATH + 'teams/',
            'activities': base_url + API_SUB_PATH + 'activities/',
            'leaderboard': base_url + API_SUB_PATH + 'leaderboard/',
            'workouts': base_url + API_SUB_PATH + 'workouts/'
        }
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer