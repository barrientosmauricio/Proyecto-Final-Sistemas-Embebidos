# !/usr/bin/env python3
# ## ###############################################
#
# led_manager.py
# Controls leds in the GPIO
#
# Autor: Francisco Javier Solano Tavera
# 
#
# ## ###############################################

# Future imports (Python 2.7 compatibility)
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from tkinter.constants import FALSE, TRUE

# Import Raspberry Pi's GPIO control library
import RPi.GPIO as GPIO
# Imports sleep functon
from time import sleep
# Initializes virtual board (comment out for hardware deploy)
import virtualboard

# Disable warnings
# GPIO.setwarnings(False)
# Set up Rpi.GPIO library to use physical pin numbers
GPIO.setmode(GPIO.BOARD)

# Set up pin no. 32 as output and default it to low
GPIO.setup(32, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW)
pwm = GPIO.PWM(32, 1)

def ledsoff():
	GPIO.output(10, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(18, GPIO.LOW)
	GPIO.output(22, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(26, GPIO.LOW)
	GPIO.output(32, GPIO.LOW)
	GPIO.output(36, GPIO.LOW)
	GPIO.output(38, GPIO.LOW)
	GPIO.output(40, GPIO.LOW)
	GPIO.output(37, GPIO.LOW)
pass

""" Enciende el leds especificados en num, apagando los demás
	(To be developed by the student)
"""

def leds(num):
	ledsoff()
	GPIO.output(32, GPIO.HIGH if (num & 0x00000001) > 0 else GPIO.LOW )
	GPIO.output(26, GPIO.HIGH if (num & 0x00000002) > 0 else GPIO.LOW )
	GPIO.output(24, GPIO.HIGH if (num & 0x00000004) > 0 else GPIO.LOW )
	GPIO.output(22, GPIO.HIGH if (num & 0x00000008) > 0 else GPIO.LOW )
	pass

""" Activa el modo marquesina
	type toma tres valores: left, right y pingpong
	(To be developed by the student)
"""
def marquee(type='pingpong'):
	switcher = {
		'left'     : _marquee_left,
		'right'    : _marquee_right,
		'pingpong' : _marquee_pingpong,
		'timbre'   : _marquee_timbre,
		'atenuado' : _marquee_atenuado
	}
	func = switcher.get(type, None)
	if func:
		func()


"""	Despliega en número proporcionado en el display de siete segmentos.
	(To be developed by the student)
"""

def bcd(num):
	ledsoff()
	GPIO.output(36, GPIO.HIGH if (num & 0x00000001) > 0 else GPIO.LOW )
	GPIO.output(38, GPIO.HIGH if (num & 0x00000002) > 0 else GPIO.LOW )
	GPIO.output(40, GPIO.HIGH if (num & 0x00000004) > 0 else GPIO.LOW )
	GPIO.output(37, GPIO.HIGH if (num & 0x00000008) > 0 else GPIO.LOW )
	pass


""" ENCIENDE LAS LUCES"""

def _marquee_left():
	ledsoff()

#while True: # Forever
	                # Wait 500ms
	GPIO.output(32, GPIO.HIGH) # Turn led on
	GPIO.output(26, GPIO.HIGH)
	GPIO.output(24, GPIO.HIGH)
	GPIO.output(22, GPIO.HIGH)
	GPIO.output(18, GPIO.HIGH)
	GPIO.output(16, GPIO.HIGH)
	GPIO.output(12, GPIO.HIGH)
	GPIO.output(10, GPIO.HIGH)

	print("Luces encendidas")
	
	pass

	#sleep(0.5)                 # Wait 500ms
	'''GPIO.output(10, GPIO.HIGH) # Turn led on
	sleep(0.5)
	GPIO.output(10, GPIO.LOW)  # Turn led off
	GPIO.output(12, GPIO.HIGH) # Turn led on
	sleep(0.5)
	GPIO.output(12, GPIO.LOW)  # Turn led off
	GPIO.output(16, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(16, GPIO.LOW)  # Turn led off
	GPIO.output(18, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(18, GPIO.LOW)  # Turn led off
	GPIO.output(22, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(22, GPIO.LOW)  # Turn led off
	GPIO.output(24, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(24, GPIO.LOW)  # Turn led off
	GPIO.output(26, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(26, GPIO.LOW)  # Turn led off
	GPIO.output(32, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(32, GPIO.LOW)  # Turn led off
	pass'''

""" APAGA LAS LUCES"""

def _marquee_right():
	ledsoff()

	GPIO.output(32, GPIO.LOW)  # Turn led off
	GPIO.output(26, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(22, GPIO.LOW)
	GPIO.output(18, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(10, GPIO.LOW) 

	print("Luces Apagadas")
	#sleep(0.5)                 # Wait 500ms
	'''GPIO.output(32, GPIO.HIGH) # Turn led on
	sleep(0.5)
	GPIO.output(32, GPIO.LOW)  # Turn led off
	GPIO.output(26, GPIO.HIGH) # Turn led on
	sleep(0.5)
	GPIO.output(26, GPIO.LOW)  # Turn led off
	GPIO.output(24, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(24, GPIO.LOW)  # Turn led off
	GPIO.output(22, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(22, GPIO.LOW)  # Turn led off
	GPIO.output(18, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(18, GPIO.LOW)  # Turn led off
	GPIO.output(16, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(16, GPIO.LOW)  # Turn led off
	GPIO.output(12, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(12, GPIO.LOW)  # Turn led off
	GPIO.output(10, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(10, GPIO.LOW)  # Turn led off'''

	pass

""" ACTIVA CAMARAS DE VIGILANCIA"""

def _marquee_pingpong():
	ledsoff()
	GPIO.output(12, GPIO.HIGH)
	GPIO.output(16, GPIO.HIGH)
	sleep(0.5)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	print("Desplegado de camaras de vigilancia")

	'''GPIO.output(10, GPIO.HIGH) # Turn led on
	sleep(0.5)
	GPIO.output(10, GPIO.LOW)  # Turn led off
	GPIO.output(12, GPIO.HIGH) # Turn led on
	sleep(0.5)
	GPIO.output(12, GPIO.LOW)  # Turn led off
	GPIO.output(16, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(16, GPIO.LOW)  # Turn led off
	GPIO.output(18, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(18, GPIO.LOW)  # Turn led off
	GPIO.output(22, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(22, GPIO.LOW)  # Turn led off
	GPIO.output(24, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(24, GPIO.LOW)  # Turn led off
	GPIO.output(26, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(26, GPIO.LOW)  # Turn led off
	GPIO.output(32, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(32, GPIO.LOW)  # Turn led off
	GPIO.output(32, GPIO.HIGH) # Turn led on
	sleep(0.5)
	GPIO.output(32, GPIO.LOW)  # Turn led off
	GPIO.output(26, GPIO.HIGH) # Turn led on
	sleep(0.5)
	GPIO.output(26, GPIO.LOW)  # Turn led off
	GPIO.output(24, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(24, GPIO.LOW)  # Turn led off
	GPIO.output(22, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(22, GPIO.LOW)  # Turn led off
	GPIO.output(18, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(18, GPIO.LOW)  # Turn led off
	GPIO.output(16, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(16, GPIO.LOW)  # Turn led off
	GPIO.output(12, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(12, GPIO.LOW)  # Turn led off
	GPIO.output(10, GPIO.HIGH) # Turn led on
	sleep(0.5)                 # Espera 500ms
	GPIO.output(10, GPIO.LOW)  # Turn led off'''
	pass


def _marquee_timbre():
	ledsoff()
	GPIO.output(10, GPIO.HIGH)
	print("Timbre ON")
	sleep(2)
    
	GPIO.output(10, GPIO.LOW)
	print("Timbre OFF")
	sleep(1)
	


	'''flag = True
	while flag:
		GPIO.output(10, GPIO.HIGH)
		
		print("Tocando Timbre")

		try:
			flag= False
			GPIO.output(10, GPIO.LOW)
			#print("No hay nadie")
			#print("Soltaste Timbre")
			#flag= False
			#if _marquee_timbre == TRUE:
			
		except: 
			
			print("No hay nadie")'''
			

	pass

def _marquee_atenuado():
	ledsoff()
#pwm = GPIO.PWM(32, 1)
	print("Starting pwm")
# Set duty cycle to 50% to blink 500ms on 500ms off
	pwm.start(50)
	print("Pwm started")
	flag = True

	# Blink the led
	while flag:
		try:
			dutyCycle = int(input("Set duty cycle: "))
			pwm.ChangeDutyCycle(dutyCycle)
		except:
			flag = False
			pwm.ChangeDutyCycle(0)

# Stop the PWM
	pwm.stop()
# Reset all ports to its default state (inputs)
#GPIO.cleanup()
	pass		