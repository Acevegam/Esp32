from flask import Flask, jsonify
import requests

app = Flask(__name__)

# URL pública de Ngrok
ESP32_SERVER_URL = '192.168.1.82'  # Usa solo la URL pública de Ngrok

@app.route('/', methods=['GET'])
def index():
    return jsonify({'status': 'active', 'message': 'API is running'})

@app.route('/ledon', methods=['GET'])
def led_on():
    # Enviar solicitud al servidor ESP32 para encender el LED
    try:
        response = requests.get(f'{ESP32_SERVER_URL}/ledon')  # Usa la URL de Ngrok directamente
        return jsonify({'status': 'success', 'message': 'LED is ON', 'esp32_response': response.text})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/ledoff', methods=['GET'])
def led_off():
    # Enviar solicitud al servidor ESP32 para apagar el LED
    try:
        response = requests.get(f'{ESP32_SERVER_URL}/ledoff')  # Usa la URL de Ngrok directamente
        return jsonify({'status': 'success', 'message': 'LED is OFF', 'esp32_response': response.text})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
