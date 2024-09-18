#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)
	
	

C4 : float = 262
CS4 : float = 277
D4 : float = 294
DS4 : float = 311
E4 : float = 330
ES4 : float = 349
F4 : float = 349
FS4 : float = 370
G4 : float = 392
GS4 : float = 415
A4 : float = 440
AS4 : float = 466
B4 : float = 494

C5 : float = 262 * 2
CS5 : float = 277 * 2
D5 : float = 294 * 2
DS5 : float = 311 * 2
E5 : float = 330 * 2
ES5 : float = 349 * 2
F5 : float = 349 * 2
FS5 : float = 370 * 2
G5 : float = 392 * 2
GS5 : float = 415 * 2
A5 : float = 440 * 2
AS5 : float = 466 * 2
B5 : float = 494 * 2

C6 : float = 262 * 4
CS6 : float = 277 * 4
D6 : float = 294 * 4
DS6 : float = 311 * 4
E6 : float = 330 * 4
ES6 : float = 349 * 4
F6 : float = 349 * 4
FS6 : float = 370 * 4
G6 : float = 392 * 4
GS6 : float = 415 * 4
A6 : float = 440 * 4
AS6 : float = 466 * 4
B6 : float = 494 * 4


canonind = [
	(A5,16),
	(FS5,8),(G5,8),(A5,16),
	(FS5,8),(G5,8),(A5,16),
	(B4,8),(CS5,8),(D5,8),(E5,8),(FS5,8),(G5,8),
	(FS5,16),
	(D5,8),(E5,8),(FS5,16),
	(FS4,8),(G4,8),(A4,8),(B4,8),(A4,8),(G4,8),(A4,8),
	(FS4,8),(G4,8),(A4,8),(G4,16),
	(B4,8),(A4,8),(G4,16),
	(FS4,8),(E4,8),
	(FS4,8),(E4,8),(D4,8),(E4,8),(FS4,8),(G4,8),(A4,8),(B4,8),(G4,16),	
	(B4,8),(A4,8),(B4,16),
	(CS5,8),(D5,8),
	(A4,8),(B4,8),(CS5,8),(D5,8),(E5,8),(FS5,8),(G5,8),(A5,8)
]

for i in range(2):
	for note in canonind:
		playtone(note[0], note[1] / 45)
	


# Turn off the PWM
quiet()
