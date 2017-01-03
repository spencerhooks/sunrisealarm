from flask import Flask, render_template
from streamgen import Player

p = Player()

app = Flask(__name__)
app.config["CACHE_TYPE"] = "null"

@app.route('/')
def clock():
    return render_template('clock.html')

@app.route('/settings/')
def settings():
    return render_template('settings.html')

@app.route('/play_sound')
def play_sound():
    p.play()
    return render_template('clock.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    cache.init_app(app)
