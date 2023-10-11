from flask import Blueprint, render_template, redirect, url_for, request, flash
from .mqtt import MqttClient
import os
import re

views = Blueprint('views', __name__)
client = MqttClient()

"""                                        DASHBOARD                                              """
@views.route('/user', methods=['POST', 'GET'])
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

@views.route('/', methods=['POST', 'GET'])
def door():
  if request.method == 'POST':
      broker = request.form['broker']
      topic = request.form['topik']

      client.connectTo(broker=broker, topic=topic)
      if client.connected:
        # jika berhasil connect pergi ke /user
        return redirect(url_for('views.dashboard'))
      else:
        # jika tidak tampilkan alert
        flash("Broker ataupun Topiknya tidak ditemukan")

  return render_template('door.html')