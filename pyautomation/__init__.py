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
pin_buzzer.lo()

pin_led = board.pins[16]  # GPIO 23
pin_led.mode = pingo.OUT
pin_led.lo()

red_led = board.pins[11]  # GPIO 17
red_led.mode = pingo.OUT
red_led.lo()

blue_led = board.pins[15]  # GPIO 22 
blue_led.mode = pingo.OUT
blue_led.lo()

green_led = board.pins[13]  # GPIO 27
green_led.mode = pingo.OUT
green_led.lo()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/buzzer', methods=['POST'])
def buzzer():
    pin_buzzer.toggle()
    return redirect(url_for('index'))


@app.route('/led', methods=['POST'])
def led():
    pin_led.toggle()
    return redirect(url_for('index'))

@app.route('/rgb/<color>', methods=['POST'])
def rgb(color):
    if color == "red":
        red_led.toggle()

    elif color == "green":
        green_led.toggle()

    elif color == "blue":
        blue_led.toggle()

    return redirect(url_for('index'))

