#!/usr/bin/env python3
import requests
import time
from datetime import timedelta
import logging
import os
import sys
from requests.auth import HTTPBasicAuth

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

API_BASE_URL = os.environ.get('API_URL', 'http://web:8000/api/v1')
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin')
ACTION = os.environ.get('ACTION', 'load')  # 'load' or 'delete'
MAX_RETRIES = int(os.environ.get('MAX_RETRIES', 30))
RETRY_DELAY = int(os.environ.get('RETRY_DELAY', 2))

def get_auth():
    return HTTPBasicAuth(ADMIN_USERNAME, ADMIN_PASSWORD)

def wait_for_api():
    for i in range(MAX_RETRIES):
        try:
            response = requests.get(f"{API_BASE_URL}/", auth=get_auth(), verify=False)
            if response.status_code == 200:
                logger.info("API is ready!")
                return True
        except requests.exceptions.ConnectionError:
            logger.info(f"API not ready, attempt {i+1}/{MAX_RETRIES}. Retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)
    logger.error("API did not become available in time")
    return False

def delete_all_data():
    """Delete all data from the system via API calls"""
    endpoints = ['activities', 'leaderboard', 'teams', 'workouts', 'users']
    
    for endpoint in endpoints:
        logger.info(f"Deleting all {endpoint}...")
        try:
            # First get all items
            response = requests.get(
                f"{API_BASE_URL}/{endpoint}/",
                auth=get_auth(),
                verify=False
            )
            response.raise_for_status()
            items = response.json()
            
            # Then delete each item
            for item in items:
                item_id = item.get('id')
                if item_id:
                    delete_response = requests.delete(
                        f"{API_BASE_URL}/{endpoint}/{item_id}/",
                        auth=get_auth(),
                        verify=False
                    )
                    delete_response.raise_for_status()
                    logger.info(f"Deleted {endpoint} with id {item_id}")
            
            logger.info(f"Successfully deleted all {endpoint}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error deleting {endpoint}: {e}")
            return False
    
    return True

def create_users():
    """Create sample users via API"""
    users = []
    user_data = [
        {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
        {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
        {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
        {"username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
        {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"}
    ]
    
    for user in user_data:
        try:
            response = requests.post(
                f"{API_BASE_URL}/users/",
                json=user,
                auth=get_auth(),
                verify=False
            )
            response.raise_for_status()
            users.append(response.json())
            logger.info(f"Created user {user['username']}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error creating user {user['username']}: {e}")
    
    return users

def create_teams(users):
    """Create teams and assign users via API"""
    teams = []
    team_data = [
        {"name": "Blue Team", "members": [u["id"] for u in users[:3]]},
        {"name": "Gold Team", "members": [u["id"] for u in users[3:]]}
    ]
    
    for team in team_data:
        try:
            response = requests.post(
                f"{API_BASE_URL}/teams/",
                json=team,
                auth=get_auth(),
                verify=False
            )
            response.raise_for_status()
            teams.append(response.json())
            logger.info(f"Created team {team['name']}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error creating team {team['name']}: {e}")
    
    return teams

def create_activities(users):
    """Create activities for users via API"""
    activities = []
    activity_data = [
        {"user": users[0]["id"], "activity_type": "Cycling", "duration": str(timedelta(hours=1))},
        {"user": users[1]["id"], "activity_type": "Crossfit", "duration": str(timedelta(hours=2))},
        {"user": users[2]["id"], "activity_type": "Running", "duration": str(timedelta(hours=1, minutes=30))},
        {"user": users[3]["id"], "activity_type": "Strength", "duration": str(timedelta(minutes=30))},
        {"user": users[4]["id"], "activity_type": "Swimming", "duration": str(timedelta(hours=1, minutes=15))}
    ]
    
    for activity in activity_data:
        try:
            response = requests.post(
                f"{API_BASE_URL}/activities/",
                json=activity,
                auth=get_auth(),
                verify=False
            )
            response.raise_for_status()
            activities.append(response.json())
            logger.info(f"Created activity {activity['activity_type']} for user {activity['user']}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error creating activity: {e}")
    
    return activities

def create_leaderboard_entries(users):
    """Create leaderboard entries via API"""
    entries = []
    entry_data = [
        {"user": users[0]["id"], "score": 100},
        {"user": users[1]["id"], "score": 90},
        {"user": users[2]["id"], "score": 95},
        {"user": users[3]["id"], "score": 85},
        {"user": users[4]["id"], "score": 80}
    ]
    
    for entry in entry_data:
        try:
            response = requests.post(
                f"{API_BASE_URL}/leaderboard/",
                json=entry,
                auth=get_auth(),
                verify=False
            )
            response.raise_for_status()
            entries.append(response.json())
            logger.info(f"Created leaderboard entry for user {entry['user']}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error creating leaderboard entry: {e}")
    
    return entries

def create_workouts():
    """Create workout entries via API"""
    workouts = []
    workout_data = [
        {"name": "Cycling Training", "description": "Training for a road cycling event"},
        {"name": "Crossfit", "description": "Training for a crossfit competition"},
        {"name": "Running Training", "description": "Training for a marathon"},
        {"name": "Strength Training", "description": "Training for strength"},
        {"name": "Swimming Training", "description": "Training for a swimming competition"}
    ]
    
    for workout in workout_data:
        try:
            response = requests.post(
                f"{API_BASE_URL}/workouts/",
                json=workout,
                auth=get_auth(),
                verify=False
            )
            response.raise_for_status()
            workouts.append(response.json())
            logger.info(f"Created workout {workout['name']}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error creating workout: {e}")
    
    return workouts

def load_sample_data():
    """Load all sample data via API calls"""
    if not wait_for_api():
        sys.exit(1)

    logger.info("Creating users...")
    users = create_users()
    if not users:
        logger.error("Failed to create users, aborting")
        return False

    logger.info("Creating teams...")
    teams = create_teams(users)

    logger.info("Creating activities...")
    activities = create_activities(users)

    logger.info("Creating leaderboard entries...")
    leaderboard = create_leaderboard_entries(users)

    logger.info("Creating workouts...")
    workouts = create_workouts()

    logger.info("Sample data loading complete!")
    return True

def main():
    if ACTION.lower() == 'delete':
        logger.info("Deleting all existing data...")
        if delete_all_data():
            logger.info("Successfully deleted all data")
        else:
            logger.error("Failed to delete all data")
            sys.exit(1)
    
    if ACTION.lower() == 'load':
        logger.info("Loading sample data...")
        if load_sample_data():
            logger.info("Successfully loaded sample data")
        else:
            logger.error("Failed to load sample data")
            sys.exit(1)

if __name__ == "__main__":
    main()