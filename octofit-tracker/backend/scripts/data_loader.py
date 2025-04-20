#!/usr/bin/env python3
import requests
import time
from datetime import timedelta
import logging
import os
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_BASE_URL = "http://web:8000/api"

def wait_for_api():
    max_retries = 30
    retry_delay = 2
    for i in range(max_retries):
        try:
            response = requests.get(f"{API_BASE_URL}/")
            if response.status_code == 200:
                logger.info("API is ready!")
                return True
        except requests.exceptions.ConnectionError:
            logger.info(f"API not ready, attempt {i+1}/{max_retries}. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
    logger.error("API did not become available in time")
    return False

def create_user(username, email, password):
    try:
        response = requests.post(f"{API_BASE_URL}/users/", json={
            "username": username,
            "email": email,
            "password": password
        })
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error creating user {username}: {e}")
        return None

def create_team(name, member_ids):
    try:
        response = requests.post(f"{API_BASE_URL}/teams/", json={
            "name": name,
            "members": member_ids
        })
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error creating team {name}: {e}")
        return None

def create_activity(user_id, activity_type, duration):
    try:
        response = requests.post(f"{API_BASE_URL}/activities/", json={
            "user": user_id,
            "activity_type": activity_type,
            "duration": duration
        })
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error creating activity for user {user_id}: {e}")
        return None

def create_workout(name, description):
    try:
        response = requests.post(f"{API_BASE_URL}/workouts/", json={
            "name": name,
            "description": description
        })
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error creating workout {name}: {e}")
        return None

def load_sample_data():
    if not wait_for_api():
        sys.exit(1)

    logger.info("Creating users...")
    users = [
        create_user("thundergod", "thundergod@mhigh.edu", "thundergodpassword"),
        create_user("metalgeek", "metalgeek@mhigh.edu", "metalgeekpassword"),
        create_user("zerocool", "zerocool@mhigh.edu", "zerocoolpassword"),
        create_user("crashoverride", "crashoverride@mhigh.edu", "crashoverridepassword"),
        create_user("sleeptoken", "sleeptoken@mhigh.edu", "sleeptokenpassword")
    ]
    users = [u for u in users if u is not None]
    
    if not users:
        logger.error("Failed to create any users")
        return

    logger.info("Creating teams...")
    teams = [
        create_team("Blue Team", [u["id"] for u in users[:3]]),
        create_team("Gold Team", [u["id"] for u in users[3:]])
    ]

    logger.info("Creating activities...")
    activities = [
        create_activity(users[0]["id"], "Cycling", str(timedelta(hours=1))),
        create_activity(users[1]["id"], "Crossfit", str(timedelta(hours=2))),
        create_activity(users[2]["id"], "Running", str(timedelta(hours=1, minutes=30))),
        create_activity(users[3]["id"], "Strength", str(timedelta(minutes=30))),
        create_activity(users[4]["id"], "Swimming", str(timedelta(hours=1, minutes=15)))
    ]

    logger.info("Creating workouts...")
    workouts = [
        create_workout("Cycling Training", "Training for a road cycling event"),
        create_workout("Crossfit", "Training for a crossfit competition"),
        create_workout("Running Training", "Training for a marathon"),
        create_workout("Strength Training", "Training for strength"),
        create_workout("Swimming Training", "Training for a swimming competition")
    ]

    logger.info("Sample data loading complete!")

if __name__ == "__main__":
    load_sample_data()