#!/usr/bin/env python

from flask import Flask
from adb_shell.adb_device import AdbDeviceTcp
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
import re

theater_fire = '10.128.2.34'
keys = 'adbkey'
windows_regex = re.compile(r"Window\{(?P<id>.+?) (?P<user>.+) (?P<package>.+?)(?:\/(?P<activity>.+?))?\}$", re.MULTILINE)

# Connect (authentication required)
with open(keys) as f:
    priv = f.read()
signer = PythonRSASigner('', priv)
dev = AdbDeviceTcp(theater_fire, 5555, default_timeout_s=9.)
dev.connect(rsa_keys=[signer], auth_timeout_s=0.1)

app = Flask(__name__)

#TODO add error handling
@app.route('/state')
def state():
    resp = dev.shell('dumpsys window windows | grep mCurrentFocus')
    match = windows_regex.search(resp)
    (pkg, activity) = match.group("package", "activity")
    cur_app = {"package": pkg, "activity": activity}
    return cur_app

# TODO add function to get list of installed apps
# @app.route('/get_apps')
# def get_apps():


if __name__ == "__main__":
    app.run(host='0.0.0.0')


