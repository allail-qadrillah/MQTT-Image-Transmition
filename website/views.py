from flask import Blueprint, render_template, redirect, url_for, request, flash
from .mqtt import MqttClient
import os
import re

views = Blueprint('views', __name__)
client = MqttClient()

"""                                        DASHBOARD                                              """
@views.route('/user', methods=['POST', 'GET'])
def dashboard():
  
  list_gambar = os.listdir("website/static/img/history")
  list_gambar.sort(reverse=True)
  
  image = {
      'image_name': client.split_string(list_gambar[0]),
      'image_path': 'static/img/history/'+list_gambar[0]
  }

  return render_template('index.html', 
                          item=image,
                          broker = client.broker,
                          status = client.connected
                        )

"""                                        HISTORY                                              """
@views.route('/history', methods=['POST', 'GET'])
def history():
  
  list_gambar = os.listdir("website/static/img/history")
  list_gambar.sort(reverse=True)

  history = [ 
        {
            "image_path": "static/img/history/" + item,
            "image_name": client.split_string(item)
        }
        for item in list_gambar 
    ]

  return render_template('history.html', history=history)

@views.route('/', methods=['POST', 'GET'])
def door():
  if request.method == 'POST':
      broker = request.form['broker']
      port = request.form['port']
      timeout = request.form['timeout']

      client.connectTo(broker=broker, port=int(port), timeout=int(timeout))
      if client.connected:
        # jika berhasil connect pergi ke /user
        return redirect(url_for('views.dashboard'))
      else:
        # jika tidak tampilkan alert
        flash("Broker tidak ditemukan")

  return render_template('door.html')