from flask import Blueprint, render_template, redirect, url_for, request
import os
import re

views = Blueprint('views', __name__)

"""                                        DASHBOARD                                              """
@views.route('/', methods=['POST', 'GET'])
def dashboard():
  
  image = {
    'image_name': 'uji coba gambar',
    'image_path': 'static/img/history/history_1.png'
  }

  return render_template('index.html', item=image)

"""                                        HISTORY                                              """
@views.route('/history', methods=['POST', 'GET'])
def history():
  history = []

  return render_template('history.html', history=history)