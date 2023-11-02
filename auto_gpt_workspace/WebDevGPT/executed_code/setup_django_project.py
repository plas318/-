import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
django.setup()

from django.core.management import call_command

call_command('startproject', 'blog_project')
call_command('startapp', 'users')
call_command('startapp', 'posts')
call_command('startapp', 'comments')