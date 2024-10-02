from flask import Flask, render_template, jsonify
import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Inisialisasi Firebase Admin SDK
credentials_json = os.getenv("GOOGLE_CREDENTIALS")
firebase_url = os.getenv("FIREBASE_URL")

cred = credentials.Certificate(r"tugas1-realtimedb.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': firebase_url
})

# Referensi ke node 'cpu_usage' di Firebase
ref = db.reference('cpu_usage')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    snapshot = ref.order_by_key().limit_to_last(10).get()  # Ambil 10 data terakhir
    data = [{'cpu': value['cpu'], 'timestamp': value['timestamp']} for key, value in snapshot.items()]
    return jsonify(data)

# Tidak perlu app.run() karena Vercel yang akan mengurus servernya