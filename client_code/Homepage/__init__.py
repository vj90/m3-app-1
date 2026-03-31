from ._anvil_designer import HomepageTemplate
from anvil import *
import anvil.users
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil.designer import in_designer
from ..AllTasks import AllTasks
import logging
logging.basicConfig(level=logging.DEBUG)

class Homepage(HomepageTemplate):
 def __init__(self, **properties):
   # Set Form properties and Data Bindings.
  self.init_components(**properties)
   #if not in_designer:
     #pass
     #anvil.users.login_with_form()
   # Any code you write here will run before the form opens.
  logging.info('Initializing homepage!')
  

 @handle("nav_tasks", "click")
 def nav_tasks_click(self, **event_args):
  open_form('AllTasks')

 @handle("nav_home", "click")
 def nav_home_click(self, **event_args):
   open_form('Home')

 @handle("quick_task_button", "click")
 def quick_task_button_click(self, **event_args):
  new_task_text = self.quick_task_text_box.text
  if new_task_text:
    if self.quick_task_urgent_bool.checked:
      anvil.server.call('add_quick_urgent_task', new_task_text)
      Notification("Urgent task added!").show()
    else:
      anvil.server.call('add_quick_task', new_task_text)
      Notification("Task added!").show()
    self.quick_task_text_box.text = ""
    open_form(anvil.get_open_form())

 @handle("quick_task_text_box", "pressed_enter")
 def quick_task_text_box_pressed_enter(self, **event_args):
   self.quick_task_button_click()