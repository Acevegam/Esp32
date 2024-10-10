from flask import Flask, jsonify
import requests

app = Flask(__name__)

# IP de la ESP32 servidora y puerto
ESP32_SERVER_IP = '192.168.1.82'  # Coloca aquí la IP local o pública de la ESP32 servidora
ESP32_SERVER_PORT = 80

@app.route('/', methods=['GET'])
def index():
    return jsonify({'status': 'active', 'message': 'API is running'})

@app.route('/ledon', methods=['GET'])
def led_on():
    # Enviar solicitud al servidor ESP32 para encender el LED
    try:
        response = requests.get(f'http://{ESP32_SERVER_IP}:{ESP32_SERVER_PORT}/ledon')
        return jsonify({'status': 'success', 'message': 'LED is ON', 'esp32_response': response.text})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

@app.route('/ledoff', methods=['GET'])
def led_off():
    # Enviar solicitud al servidor ESP32 para apagar el LED
    try:
        response = requests.get(f'http://{ESP32_SERVER_IP}:{ESP32_SERVER_PORT}/ledoff')
        return jsonify({'status': 'success', 'message': 'LED is OFF', 'esp32_response': response.text})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

