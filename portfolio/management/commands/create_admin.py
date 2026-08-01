import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Creates or updates a superuser automatically from environment variables"

    def handle(self, *args, **options):
        username = os.getenv('ADMIN_USERNAME', 'admin')
        email = os.getenv('ADMIN_EMAIL', 'codesimplified7@gmail.com')
        password = os.getenv('ADMIN_PASSWORD')

        if not password:
            self.stdout.write(self.style.WARNING("ADMIN_PASSWORD environment variable not set. Skipping superuser creation."))
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"Successfully created superuser '{username}'"))
        else:
            user = User.objects.get(username=username)
            user.set_password(password)
            user.is_superuser = True
            user.is_staff = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Successfully updated password & permissions for superuser '{username}'"))
