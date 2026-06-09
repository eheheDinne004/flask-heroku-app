from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>My Flask App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #74ebd5, #ACB6E5);
                height: 100vh;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
            }

            .box {
                background: white;
                padding: 40px;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            }

            h1 {
                color: #333;
                font-size: 28px;
            }

            .name {
                color: #2c3e50;
                font-size: 22px;
                margin-top: 10px;
                font-weight: bold;
            }

            p {
                color: #666;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>Chao mung ban den voi Flask App</h1>
            <div class="name">Bùi Thủy Ngọc Duyên</div>
            <p>Trien khai thanh cong tren Render 🚀</p>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)