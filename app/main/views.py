from flask import render_template,request,redirect,url_for
from . import main
from flask_login import login_required

@main.route('/')
def index():
    '''
    View root page function returning index page
    '''
    title = 'Soi | Where you express yourself'
    return render_template('index.html', title = title)

@main.route('/comment')
@login_required
def index():
    '''
    View root page function returning index page
    '''
    title = 'Soi | Where you express yourself'
    return render_template('index.html', title = title)

@main.route('/posting')
@login_required
def index():
    '''
    View root page function returning index page
    '''
    title = 'Soi | Where you express yourself'
    return render_template('index.html', title = title)