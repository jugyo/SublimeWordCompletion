import commands
import sublime_plugin
import sublime

# TODO: capytalize if needed
class WordCompletion(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if len(prefix) < 3:
            return []

        words = self.look(prefix)
        return [(w, w) for w in words]

    def command(self):
        try:
            return self.view.settings().get("word_completion").get("command")
        except AttributeError:
            return "look"

    def look(self, prefix):
        result = commands.getoutput("%s %s" % (self.command(), prefix))
        if len(result) > 0:
            return result.split("\n")
        else:
            return []
