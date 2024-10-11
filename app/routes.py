from flask import Blueprint
from .controllers.home_controller import HomeController
from .controllers.about_controller import AboutController

def setup_routes(app):
    home_controller = HomeController()
    about_controller = AboutController()
    
    @app.route('/')
    def home():
        return home_controller.index()
    
    @app.route('/about')
    def about():
        return about_controller.index()
