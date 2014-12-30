import sublime, sublime_plugin
import urllib.request
import urllib.parse
import binascii
import json
import sys
import os
from subprocess import Popen, PIPE

class HtmlToJadeFromFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		source = self.view.file_name()
		if source.endswith(".html"):
			target = source + '.jade'
		if target:
			with open(source, 'r') as f:
				html = f.read()
			jade = HTHTools.post_html_return_jade(html)
			if jade != None:
				with open(target, 'w') as f:
					f.write(jade)
				self.view.window().open_file(target)

	def is_enabled(self):
		return True #return (self.view.file_name().endswith(".html") or self.view.file_name().endswith(".html"))

class HtmlToJadeFromSelectionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				html = self.view.substr(region)
				jade = HTHTools.post_html_return_jade(html)
				if jade != None:
					self.view.replace(edit, region, jade)

	def is_enabled(self):
		return True #return self.view.file_name().endswith(".jade")

class HtmlToJadeFromClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		html = sublime.get_clipboard()
		jade = HTHTools.post_html_return_jade(html)
		if jade != None:
			for region in self.view.sel():
				self.view.replace(edit, region, jade)

	def is_enabled(self):
		return True #return self.view.file_name().endswith(".jade")

class HTHTools:
	@classmethod
	def post_html_return_jade(self, html):
		settings = sublime.load_settings("html2jade.sublime-settings")
		cmd = '''
			html2jade --bodyless --donotencode<< EOF
			%s
		''' % html
		cwd = None
		env = {"PATH": settings.get('binDir')}

		jade = Popen(cmd, env=env, cwd=cwd, stdout=PIPE, stderr=PIPE, shell=True)
		jade = jade.communicate(input="".encode("utf8"))
		jade = jade[0].decode('utf8')
		return jade

