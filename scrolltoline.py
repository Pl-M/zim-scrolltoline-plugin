# -*- coding: utf-8 -*-

# Copyright 2016 Pavel_M <plprgt@gmail.com>,
# released under the GNU GPL (v2 or v3).
# This plugin is for Zim-wiki program by Jaap Karssenberg.

import gobject
import gtk

from zim.actions import toggle_action
from zim.plugins import PluginClass, extends, WindowExtension

import logging
logger = logging.getLogger('zim.plugins.ScrollToLine')


class ScrollToLinePlugin(PluginClass):

	plugin_info = {
	'name': _('ScrollToLine'), # T: plugin name
	'description': _('''\
		This plugin automatically scrolls textview to keep typed text at the given height. 
		'''), # T: plugin description
	'author': 'Pavel_M',
	'help': 'Plugins:ScrollToLine',}

	plugin_preferences = (
		# key, type, label, default
		('height', 'int', _('Cursor height, %'), 50, (0, 100)), # T: plugin preference
	)


KEYVALS_SCROLL = map(gtk.gdk.keyval_from_name, ('Up', 'Down', 'Page_Up', 'Page_Down'))
KEYVALS_ENTER = map(gtk.gdk.keyval_from_name, ('Return', 'KP_Enter', 'ISO_Enter'))

@extends('MainWindow')
class ScrollToLineExtension(WindowExtension):
	uimanager_xml = '''
	<ui>
	<toolbar name='toolbar'>
		<placeholder name='tools'>
			<toolitem action='toggle_scrolling'/>
		</placeholder>
	</toolbar>
	</ui>'''

	def __init__(self, plugin, window):
		WindowExtension.__init__(self, plugin, window)
		self._textview = self.window.pageview.view
		self._signal = None
		self._preferences = plugin.preferences

	def _enable(self):
		if self._signal:
			self._disable()
		try:
			self._signal = self._textview.connect('key-release-event', self._scroll)
		except AttributeError:
			logger.error('ScrollToLine: plugin is not initialized.')

	def _disable(self):
		if self._signal:
			self._textview.disconnect(self._signal)
			self._signal = None

	def teardown(self):
		self._disable()

	def _scroll(self, textview, event):
		if (event.keyval in KEYVALS_SCROLL \
		and not event.state & gtk.gdk.SHIFT_MASK) \
		or event.keyval in KEYVALS_ENTER:
			buffer = self._textview.get_buffer()
			height = float(self._preferences['height'])/100
			self._textview.scroll_to_mark(
				buffer.get_insert(), within_margin = 0.0,
				use_align = True, xalign = 0.0, yalign = height)

	@toggle_action(_('Enable Scrolling'), stock = gtk.STOCK_GOTO_BOTTOM,
			tooltip = 'Enable Scrolling') # T: menu item
	def toggle_scrolling(self, active):
		if active:
			self._enable()
		else:
			self._disable()


