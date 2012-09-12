import os
from flask import Flask, render_template, request
import pusher

app = Flask(__name__)

pusher.app_id = os.environ['PUSHER_APP_ID']
pusher.key = os.environ['PUSHER_KEY']
pusher.secret = os.environ['PUSHER_SECRET']

@app.route('/', methods = ['GET', 'POST'])
def index(name = None):
    msg = None

    if request.method == 'POST':
        if request.form['action'] == 'on':
            p = pusher.Pusher()
            p['servo_channel'].trigger('activate_servo', {'command': 'on'})

            msg = 'Unlocked!'

    return render_template('index.html', msg=msg)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
