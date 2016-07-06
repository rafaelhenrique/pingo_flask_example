# -*- coding; utf-8 -*-
import time

import pingo
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

try:
    print("Loading board...")
    board = pingo.detect.get_board()
    print("Its ok...")
except Exception as e:
    print("Error on get_board: {}".format(e))
    sys.exit(1)

pin_buzzer = board.pins[12]
pin_buzzer.mode = pingo.OUT

pin_led = board.pins[16]
pin_led.mode = pingo.OUT


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buzzer', methods=['POST'])
def buzzer():
    if not pin_buzzer.state or pin_buzzer.state == 'LOW':
        pin_buzzer.hi()
    else:
        pin_buzzer.lo()
    return redirect(url_for('index'))


@app.route('/led', methods=['POST'])
def led():
    if not pin_led.state or pin_led.state == 'LOW':
        pin_led.hi()
    else:
        pin_led.lo()
    return redirect(url_for('index'))

