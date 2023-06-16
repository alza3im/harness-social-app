from __future__ import absolute_import, unicode_literals

# Makes sure the app is always imported when Django starts, to allow shared_tasks to use the apps
from .celery import app as celery_app

__all__ = ("celery_app",)
