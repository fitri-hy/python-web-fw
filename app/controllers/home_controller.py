from flask import render_template
from ..components.navbar import render_navbar
from ..components.footer import render_footer

class HomeController:
    def index(self):
        navbar = render_navbar()
        footer = render_footer()
        return render_template('home.html', navbar=navbar, footer=footer)
