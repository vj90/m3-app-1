from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.task_list_label.text = self.item['task']
    self.task_list_dropdown.items = [("To Do", 0), ("In Progress", 1), ("Blocked", 2), ("Completed", 3)]
    self.task_list_due_date.date = self.item['end_date']
    self.task_list_due_date.format = "%d.%m.%y"
    print(self.task_list_due_date.margin)
    # 2. Set the DropDown to the current status in the database
    # If the status is empty (new task), default to "Backlog"
    current_status = self.item['status']
    self.task_list_dropdown.selected_value = current_status if current_status is not None else 0

  @handle("task_list_dropdown", "change")
  def task_list_dropdown_change(self, **event_args):
    new_val = self.task_list_dropdown.selected_value
    anvil.server.call('update_task_status', self.item, new_val)

  @handle("task_list_due_date", "change")
  def task_list_due_date_change(self, **event_args):
    new_val = self.task_list_due_date.date
    anvil.server.call('update_task_due_date', self.item, new_val)
