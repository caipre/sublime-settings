import sublime, sublime_plugin

class GoToCommandModeOnSaveCommand(sublime_plugin.EventListener):
   def on_pre_save(self, view):
      view.run_command("exit_insert_mode")
