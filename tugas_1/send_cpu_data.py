import firebase_admin
from firebase_admin import credentials, db
import psutil
import time

# Inisialisasi Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\ASUS\OneDrive\Desktop\Eric\kuliah\pc\pc-if41025\tugas_1\tugas1-realtimedb.json")
print(cred)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tugas1-pc-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# Referensi ke node 'cpu_usage' di Firebase
ref = db.reference('cpu_usage')

# Fungsi untuk mengirim data CPU usage ke Firebase
def push_cpu_data():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)  # Mengambil CPU usage

        data = {
            'cpu': cpu_percent,
            'timestamp': time.time()  # Menyimpan timestamp
        }

        ref.push(data)  # Mengirim data ke Firebase

        print(f"Data sent to Firebase: {data}")
        time.sleep(5)  # Mengirim data setiap 5 detik

if __name__ == "__main__":
    push_cpu_data()