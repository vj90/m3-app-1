from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # 1. Set the Label to the task text
    self.task_list_label.text = self.item['task']
    # 2. Set the DropDown to the current status in the database
    # If the status is empty (new task), default to "Backlog"
    current_status = self.item['status']
    self.task_list_dropdown.selected_value = current_status if current_status is not None else 0

  @handle("task_list_dropdown", "change")
  def task_list_dropdown_change(self, **event_args):
    self.item['status'] = self.task_list_dropdown.selected_value
