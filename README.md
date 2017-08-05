# zim-scrolltoline-plugin

This is a small plugin for Zim-wiki program (http://zim-wiki.org/) to keep cursor at the given height while typing text. 
This plugin can be used in Zim 0.63/0.65.

**This plugin doesn't support Zim 0.66 or above.**

### How does it work
This plugin uses built-in gtk.TextView function to automatically scroll text after pressing some general keys which can move cursor up or down (like Up, Down, Enter, PgUp, PgDn). To allow scrolling the text should be big enough and cursor position shouldn't be in the beginning/end of the text. The height can be set in plugin's settings.

### How to install
You can install it like any other plugin for Zim by copying [scrolltoline.py](scrolltoline.py) file to the folder with plugins (for more information look at https://github.com/jaap-karssenberg/zim-wiki/wiki/Plugins). To use the plugin enable it in Zim preferences (Edit->Preferences in the top menu) and press on the appeared button in the toolbar.
