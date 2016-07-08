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

pin_buzzer = board.pins[12]  # GPIO 18
pin_buzzer.mode = pingo.OUT

pin_led = board.pins[16]  # GPIO 23
pin_led.mode = pingo.OUT

red_led = board.pins[11]  # GPIO 17
red_led.mode = pingo.OUT
blue_led = board.pins[15]  # GPIO 22 
blue_led.mode = pingo.OUT
green_led = board.pins[13]  # GPIO 27
green_led.mode = pingo.OUT


def revert_state(pin):
    if not pin.state or pin.state == 'LOW':
        pin.hi()
    else:
        pin.lo()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buzzer', methods=['POST'])
def buzzer():
    revert_state(pin_buzzer)
    return redirect(url_for('index'))


@app.route('/led', methods=['POST'])
def led():
    revert_state(pin_led)
    return redirect(url_for('index'))

@app.route('/rgb/<color>', methods=['POST'])
def rgb(color):
    if color == "red":
        revert_state(red_led)

    elif color == "green":
        revert_state(green_led)

    elif color == "blue":
        revert_state(blue_led)

    return redirect(url_for('index'))

