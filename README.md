# pingo_flask_example
Controlling components of Raspberry Pi with Flask and Pingo

## What this project do?

See video: https://www.youtube.com/watch?v=NdoaMmsNWCs

This is an educational project to show how to use Python/Flask/Pingo/Raspberry interconnected with buzzer, simple LED and RGB LED.

## What do you need?

- 1 Raspberry Pi
- 1 Buzzer
- 1 Red led
- 1 RBG led
- 3 Resistors (330 ohms)
- Some jumpers (cables)

## How i install/use/assembly this project?

We need assemble this "structure":

![Raspberry PI](/contrib/draw.png "Raspberry PI")


Inside your S.O. on Raspberry clone this project:

```
$ git clone git@github.com:rafaelhenrique/pingo_flask_example.git --recursive
```

Create an virtualenv (i prefer [virtualenv-wrapper](https://virtualenvwrapper.readthedocs.org/en/latest/ "virtualenv-wrapper")):

```
$ mkvirtualenv pingo_flask_example
```

Enter on pingo-io directory and installs pingo ([recommended by developers](http://www.pingo.io/docs/#installing-from-github)):

```
$ cd pingo-io
$ python setup.py develop
```

Install requirements:

```
$ pip install -r requirements.txt
```

Connect your arduino into usb port and then run:

```
$ python run.py
```

Access webpage on your browser (inside or outside of Raspberry):

```
http://<ip of your raspberry>:5000
```
