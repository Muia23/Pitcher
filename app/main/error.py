from flask import render_template
from . import main

def error404_page(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('error404.html'),404