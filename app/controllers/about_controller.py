from flask import render_template
from ..components.navbar import render_navbar
from ..components.footer import render_footer

class AboutController:
    def index(self):
        navbar = render_navbar()
        footer = render_footer()
        return render_template('about.html', navbar=navbar, footer=footer)
