from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
import os

# API version configuration
API_VERSION = os.getenv('API_VERSION', 'v1')
API_SUB_PATH = f'api/{API_VERSION}/'

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def api_root(request, format=None):
    # Use request.build_absolute_uri to get the correct base URL
    def build_url(path):
        return request.build_absolute_uri(f'/{API_SUB_PATH}{path}/')
        
    return Response({
        'message': 'Welcome to OctoFit Tracker API',
        'endpoints': {
            'users': build_url('users'),
            'teams': build_url('teams'),
            'activities': build_url('activities'),
            'leaderboard': build_url('leaderboard'),
            'workouts': build_url('workouts')
        }
    })

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer