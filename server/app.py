from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv()

app_name = os.environ.get("APP_NAME")
app = Flask(
    __name__,
    static_folder='../dist/{}/'.format(app_name),
    static_url_path='/')

# Set up the index route
@app.route('/')
def index():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
