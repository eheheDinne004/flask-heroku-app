 
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Chao mung ban den voi ung dung Flask tren Heroku!</h1><p>Trien khai thanh cong.</p>"

if __name__ == '__main__':
    # Heroku se cap mot cong (Port) ngau nhien qua bien moi truong
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)