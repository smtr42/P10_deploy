"""Custom manage.py command."""
from django.core.management.base import BaseCommand

from openfoodfact.utils import req_and_clean
from products.models import Product
from datetime import datetime


class Command(BaseCommand):
    """Custom manage.py command to build database."""

    help = "Fetch data from OpenFoodFact API and build database"

    def handle(self, page_size=100, *args, **kwargs):
        """Execution when the command is called."""
        data = req_and_clean(page_size)
        Product.objects.delete_data_in_tables()
        Product.objects.create_db_from_openfoodfacts(data)
        with open("cron.log", "a") as log:
            log.write("Build effectué avec succès : " + str(datetime.now()) + "\n")
