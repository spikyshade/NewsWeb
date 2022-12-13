from flask import Blueprint, render_template
from .news import general_news, tech_news, sports_news, business_news, science_news, health_news

views = Blueprint('views', __name__)

@views.route('/')
def general():
    return render_template('general.html', general_news=general_news())

@views.route('/technology', )
def tech():
    return render_template('tech.html', tech_news=tech_news())

@views.route('/sports')
def sports():
    return render_template('sports.html', sports_news=sports_news())

@views.route('/science')
def science():
    return render_template('science.html', science_news=science_news())

@views.route('/business')
def business():
    return render_template('business.html', business_news=business_news())

@views.route('/health')
def health():
    return render_template('health.html', health_news=health_news())

