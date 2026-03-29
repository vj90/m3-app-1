import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, timedelta

@anvil.server.callable
def add_quick_task(description):
  # This adds a new row to your 'tasks' table
  app_tables.tasks.add_row(
    task=description,
    status=0,
    created=datetime.now().date(),
    start_date=datetime.now().date(),
    end_date=datetime.now().date() + timedelta(weeks=2),
    urgent=False,
  )