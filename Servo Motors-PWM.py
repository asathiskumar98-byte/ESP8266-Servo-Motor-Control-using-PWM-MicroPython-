# Time period = 20ms = Freq = 1 / Timeperiod =1 / 20ms = 50Hz
# 10 bit PWM = ESP8266
# 1ms On + 19ms Off = 0 Degree
# 1.5ms On + 18.5ms Off = 90 Degree
# 2ms On + 18ms Off = 180 Degree

import machine
import utime

servo = machine.Pin(2,machine.Pin.OUT)

pwm = machine.PWM(servo)

pwm.init(freq=50, duty=20)

def pwm_duty(duty):
    pwm.duty(duty)
    
while True:
    for x in range(120, 20, -1):
        pwm_duty(x)
        utime.sleep_ms(100)
    utime.sleep_ms(500)
    for x in range(20, 120, 1):
        pwm_duty(x)
        utime.sleep_ms(100)
    utime.sleep_ms(500)