from flask import render_template,request,redirect,url_for
from . import main

@main.route('/')
def index():
    '''
    View root page function returning index page
    '''
    title = 'Soi | Where you express yourself'
    return render_template('index.html', title = title)