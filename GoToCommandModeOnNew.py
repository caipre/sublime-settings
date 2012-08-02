import sublime, sublime_plugin

class GoToCommandModeOnNew(sublime_plugin.EventListener):
   def on_new(self, view):
      view.run_command("exit_insert_mode")
