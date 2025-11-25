from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Dummy models for demonstration; replace with your actual models if they exist
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')
        wonderwoman = User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='password')
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password')

        # Activities
        Activity.objects.create(user='ironman', type='Running', duration=30, team='Marvel')
        Activity.objects.create(user='batman', type='Cycling', duration=45, team='DC')
        Activity.objects.create(user='wonderwoman', type='Swimming', duration=60, team='DC')
        Activity.objects.create(user='spiderman', type='Yoga', duration=20, team='Marvel')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=50)
        Leaderboard.objects.create(team='DC', points=70)

        # Workouts
        Workout.objects.create(name='Morning Cardio', difficulty='Easy')
        Workout.objects.create(name='Strength Training', difficulty='Hard')
        Workout.objects.create(name='Flexibility', difficulty='Medium')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
