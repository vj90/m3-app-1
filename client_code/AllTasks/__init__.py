from ._anvil_designer import AllTasksTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import helpers as hp
import logging


class AllTasks(AllTasksTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #logging.info('AllTasks: Initializing AllTasks')
    # Any code you write here will run before the form opens.

  @handle("", "show")
  def form_show(self, **event_args):
    hp.clear_link_roles()
    self.layout.nav_tasks.role = 'selected'
    self.all_tasks_panel.items = anvil.server.call('get_tasks')

  
  def refresh_tasks(self, **event_args):
    #logging.info('AllTasks: Refreshing Tasks')
    self.all_tasks_panel.items = anvil.server.call('get_tasks')
    self.refresh_data_bindings()
