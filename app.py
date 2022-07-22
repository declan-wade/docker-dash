import docker
import logging
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/", methods=['GET', 'POST'])
def index():
  client = docker.from_env()
  payload = []
  getimage = []
  exited_containers = client.containers.list(filters={'status': 'exited'})
  exited = len(exited_containers)
  running_containers = client.containers.list(filters={'status': 'running'})
  running = len(running_containers)
  
  for container in client.containers.list(all=True):
      conts = []
      conts.append(container.name) #0
      conts.append(container.status) #1
      conts.append(container.ports) #2
      getimage.append(container.image)
      image = str(getimage[0])
      image_clean = image.split("'")
      conts.append(image_clean[1]) #3
      conts.append(container.id) #4
      
      payload.append(conts)

  return render_template('index.html',cont=payload, exited=exited, running=running)

@app.route("/stop", methods=['POST'])
def stop():
  if request.method == 'POST':
    client = docker.from_env()
    value = request.form.get('Stop')
    client.api.stop(value)
  return redirect('/')

@app.route("/start", methods=['POST'])
def start():
  if request.method == 'POST':
    client = docker.from_env()
    value = request.form.get('Start')
    client.api.start(value)
  return redirect('/')

@app.route("/restart", methods=['POST'])
def restart():
  if request.method == 'POST':
    client = docker.from_env()
    value = request.form.get('Restart')
    client.api.restart(value)
  return redirect('/')