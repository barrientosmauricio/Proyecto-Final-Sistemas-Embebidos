# !/usr/bin/env python3
# ## ###############################################
#
# led_manager.py
# Controls leds in the GPIO
#
# Autor: Mauricio Matamoros
# License: MIT
# Autores: Francisco Javier Solano Tavera, Salma Arelly Ramirez Fierro, Luis Mauricio Barrientos Veana
# Date: 16/08/2021			
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

# Set up pins as output and default it to low
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

# DECLARANDO PWM EN LOS PINES A UTILIZAR
pwm8 = GPIO.PWM(32, 1)
pwm7 = GPIO.PWM(26, 1)
pwm6 = GPIO.PWM(24, 1)
pwm5 = GPIO.PWM(22, 1)
pwm4 = GPIO.PWM(18, 1)
pwm3 = GPIO.PWM(16, 1)
pwm2 = GPIO.PWM(12, 1)
pwm1 = GPIO.PWM(10, 1)

# FUNCION QUE DETIENE LA OPERACION DEL PWM
def pwm_off():	
	pwm1.stop()
	pwm2.stop()
	pwm3.stop()
	pwm4.stop()
	pwm5.stop()
	pwm6.stop()
	pwm7.stop()
	pwm8.stop()
pass

#FUNCION QUE DETIENE LA OPERACION DE LOS FOCOS
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



# FUNCION QUE ACTIVA EL MODO CASA INTELIGENTE
#	type toma 15 valores: luces, apagar_luces,
#	camaras, camaras_apagadas, timbre, atenuar_75,
#	atenuar_50, atenuar_25, atenuar_10, abrir_cochera,
#	cerrar_cochera, programar_encendido_luces6,
#	programar_encendido_luces12, programar_apagado_luces6


def casa(type='inteligente'):
	switcher = {
		'luces'     : _casa_luces,
		'apagar_luces'    : _casa_apagar_luces,
		'camaras' : _casa_camaras,
		'camaras_apagadas' : _casa_camaras_apagadas,
		'timbre'   : _casa_timbre,
		'atenuar_75' : _casa_atenuar_75,
		'atenuar_50' : _casa_atenuar_50,
		'atenuar_25' : _casa_atenuar_25,
		'atenuar_10' : _casa_atenuar_10,
		'abrir_cochera' : _casa_abrir_cochera,
		'cerrar_cochera' : _casa_cerrar_cochera,
		'programar_encendido_luces6' : _casa_programar_encendido_luces6,
		'programar_encendido_luces12' : _casa_programar_encendido_luces12,
		'programar_apagado_luces6' : _casa_programar_apagado_luces6,
		'programar_apagado_luces12' : _casa_programar_apagado_luces12


	}
	func = switcher.get(type, None)
	if func:
		func()



################## ENCENDER/APAGAR FOCOS ####################

def _casa_luces():
	ledsoff()
	pwm_off()	

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


""" APAGA LAS LUCES"""

def _casa_apagar_luces():
	ledsoff()
	pwm_off()	

	GPIO.output(32, GPIO.LOW)  # Turn led off
	GPIO.output(26, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(22, GPIO.LOW)
	GPIO.output(18, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(10, GPIO.LOW) 

	print("Luces Apagadas")
	pass
################## ENCENDER/APAGAR FOCOS ####################


################## ACTIVAR/DESACTIVAR CAMARAS DE VIGILANCIA ####################
def _casa_camaras():
	ledsoff()
	
	pwm6.start(50) #Se activa sexta camara 
	pwm5.start(50) #Se activa quinta camara
	pwm4.start(50) #Se activa cuarta camara
	pwm3.start(50) #Se activa tercera camara
	print("Desplegado de camaras de vigilancia")

	pass

""" DESACTIVA CAMARAS DE VIGILANCIA"""
def _casa_camaras_apagadas():
	ledsoff()
	pwm_off()

	print("Apagando camaras de vigilancia")
	
	
	pass
################## ACTIVAR/DESACTIVAR CAMARAS DE VIGILANCIA ####################


################## ACTIVAR TIMBRE ####################
def _casa_timbre():
	ledsoff()
	pwm_off()
	GPIO.output(10, GPIO.HIGH)
	print("Timbre ON")
	sleep(2)
    
	GPIO.output(10, GPIO.LOW)
	print("Timbre OFF")
	sleep(1)
################## ACTIVAR TIMBRE ####################

			
################## ATENUAR FOCOS ####################
	pass

def _casa_atenuar_75():
	pwm_off()
	ledsoff()
	pwm8.start(75)
	pwm7.start(75)
	pwm6.start(75)
	pwm5.start(75)
	pwm4.start(75)
	pwm3.start(75)
	pwm2.start(75)
	pwm1.start(75)
	print("Atenuendo focos al 75%")

	pass	

def _casa_atenuar_50():
	pwm_off()
	ledsoff()
	pwm8.start(50)
	pwm7.start(50)
	pwm6.start(50)
	pwm5.start(50)
	pwm4.start(50)
	pwm3.start(50)
	pwm2.start(50)
	pwm1.start(50)
	print("Atenuendo focos al 50%")	

	pass

def _casa_atenuar_25():
	pwm_off()
	ledsoff()
	pwm8.start(25)
	pwm7.start(25)
	pwm6.start(25)
	pwm5.start(25)
	pwm4.start(25)
	pwm3.start(25)
	pwm2.start(25)
	pwm1.start(25)
	print("Atenuendo focos al 25%")

	pass

def _casa_atenuar_10():
	pwm_off()
	ledsoff()
	pwm8.start(10)
	pwm7.start(10)
	pwm6.start(10)
	pwm5.start(10)
	pwm4.start(10)
	pwm3.start(10)
	pwm2.start(10)
	pwm1.start(10)
	print("Atenuendo focos al 10%")

	pass		
#####################  ATENUAR FOCOS ######################


################### ABRIR Y CERRAR COCHERA #####################

def _casa_abrir_cochera():
	pwm_off()
	ledsoff()
	
	sleep(0.5)                 # Wait 500ms
	GPIO.output(10, GPIO.HIGH) # Turn led on
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
	print("Abriendo cochera%")

	pass


def _casa_cerrar_cochera():
		
	sleep(0.5)                 # Wait 500ms
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
	print("Cerrando cochera%")
	pass


################### ABRIR Y CERRAR COCHERA #####################

################### PROGRAMADO DE ENCENDIDO/APAGADO DE LUCES #####################


def _casa_programar_encendido_luces6():
	ledsoff()
	pwm_off()	

	sleep(6)                 # Wait 500ms
	GPIO.output(32, GPIO.HIGH)  # Turn led off
	GPIO.output(26, GPIO.HIGH)
	GPIO.output(24, GPIO.HIGH)
	GPIO.output(22, GPIO.HIGH)
	GPIO.output(18, GPIO.HIGH)
	GPIO.output(16, GPIO.HIGH)
	GPIO.output(12, GPIO.HIGH)
	GPIO.output(10, GPIO.HIGH)
	print("Encendiendo luces en 6 segundos%")
	pass

def _casa_programar_encendido_luces12():
	ledsoff()
	pwm_off()	

	sleep(12)                 # Wait 500ms
	GPIO.output(32, GPIO.HIGH)  # Turn led off
	GPIO.output(26, GPIO.HIGH)
	GPIO.output(24, GPIO.HIGH)
	GPIO.output(22, GPIO.HIGH)
	GPIO.output(18, GPIO.HIGH)
	GPIO.output(16, GPIO.HIGH)
	GPIO.output(12, GPIO.HIGH)
	GPIO.output(10, GPIO.HIGH)
	print("Encendiendo luces en 12 segundos%")
	pass


def _casa_programar_apagado_luces6():
	
	pwm_off()	

	sleep(6)                 # Wait 500ms
	GPIO.output(32, GPIO.LOW)  # Turn led off
	GPIO.output(26, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(22, GPIO.LOW)
	GPIO.output(18, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(10, GPIO.LOW)
	print("Apagando luces en 6 segundos%")
	pass

def _casa_programar_apagado_luces12():
	
	pwm_off()	

	sleep(12)                 # Wait 500ms
	GPIO.output(32, GPIO.LOW)  # Turn led off
	GPIO.output(26, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(22, GPIO.LOW)
	GPIO.output(18, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(10, GPIO.LOW)
	print("Apagando luces en 12 segundos%")
	pass

################### PROGRAMADO DE ENCENDIDO/APAGADO DE LUCES #####################
