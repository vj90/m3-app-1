from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("add_quick_task_button", "click")
  def add_quick_task_button_click(self, **event_args):
    new_task_text = self.add_quick_task_text_box.text
    if new_task_text:
      anvil.server.call('add_quick_task', new_task_text)
    # Clear the box for the next task
    self.add_quick_task_text_box.text = ""
    Notification("Task added!").show()
