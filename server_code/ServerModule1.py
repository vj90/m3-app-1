import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, timedelta

@anvil.server.callable
def add_quick_task(description):
  # This adds a new row to your 'tasks' table
  current_user = 'test' # anvil.users.get_user()
  if current_user:
    app_tables.tasks.add_row(
      task=description,
      status=0,
      created=datetime.now().date(),
      start_date=datetime.now().date(),
      urgent=False,
      #user=current_user,
    )


@anvil.server.callable
def add_quick_urgent_task(description):
  # This adds a new row to your 'tasks' table
  current_user = 'test' #anvil.users.get_user()
  if current_user:
    app_tables.tasks.add_row(
      task=description,
      status=0,
      created=datetime.now().date(),
      start_date=datetime.now().date(),
      end_date=datetime.now().date() + timedelta(weeks=2),
      urgent=True,
      #user=current_user
    )


@anvil.server.callable
def get_tasks():
  current_user = 'test' #anvil.users.get_user()
  if current_user:
    # Search ONLY for tasks where the owner is this user
    return app_tables.tasks.search(
      tables.order_by("created", ascending=False),
      #user=current_user,
    )
  return [] # Return empty list if no one is logged in

  
@anvil.server.callable
def update_task_status(task_row, new_status):
  # Check if the row exists and update the status column
  # Check if the task actually belongs to the user trying to change it
  current_user = anvil.users.get_user()
  if task_row is not None :#and task_row['user'] == current_user:
    task_row['status'] = new_status

@anvil.server.callable
def update_task_due_date(task_row, new_date):
  # Check if the row exists and update the status column
  current_user = anvil.users.get_user()
  if task_row is not None :#and task_row['user'] == current_user:
    task_row['end_date'] = new_date