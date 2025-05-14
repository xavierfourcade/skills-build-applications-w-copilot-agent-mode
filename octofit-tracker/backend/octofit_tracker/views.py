from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import users_collection, teams_collection, activity_collection, leaderboard_collection, workouts_collection
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

# Create your views here.

class UserView(APIView):
    def get(self, request):
        users = list(users_collection.find({}, {"_id": 0}))
        return Response(users)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            users_collection.insert_one(serializer.validated_data)
            return Response({"message": "User created successfully"})
        return Response(serializer.errors, status=400)

# Similar views can be created for Team, Activity, Leaderboard, and Workout.
