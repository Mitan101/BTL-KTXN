from flask import Flask, request, send_file
import os
import time

app = Flask(__name__)

HOME_DIR = os.path.expanduser("~")
SYSTEM_TXT_PATH = os.path.join(HOME_DIR, "system.txt")
SCREENSHOT_TXT_PATH = os.path.join(HOME_DIR, "screenshot.txt")
EXE_PATH = os.path.join(HOME_DIR, "CVE-2022-21882.exe")

@app.route('/system.txt', methods=['GET'])
def get_system_txt():
    if os.path.exists(SYSTEM_TXT_PATH):
        return send_file(SYSTEM_TXT_PATH, as_attachment=True)
    else:
        return 'File system.txt not found', 404

@app.route('/screenshot.txt', methods=['GET'])
def get_screenshot_txt():
    if os.path.exists(SCREENSHOT_TXT_PATH):
        return send_file(SCREENSHOT_TXT_PATH, as_attachment=True)
    else:
        return 'File screenshot.txt not found', 404

@app.route('/CVE-2022-21882.exe', methods=['GET'])
def get_exe():
    if os.path.exists(EXE_PATH):
        return send_file(EXE_PATH, as_attachment=True)
    else:
        return 'File CVE-2022-21882.exe not found', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
