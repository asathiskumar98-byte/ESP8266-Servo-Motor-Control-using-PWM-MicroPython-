# 🌀 ESP8266 Servo Motor Control using PWM (MicroPython)

This project demonstrates how to control a **servo motor** connected to an **ESP8266** board using **Pulse Width Modulation (PWM)** with **MicroPython**.  
The servo sweeps smoothly from **0° → 180° → 0°**, showing precise position control using variable PWM duty cycles.

---

## 🧠 Project Overview

| Component | Description |
|------------|-------------|
| **Board** | ESP8266 |
| **IDE** | Thonny IDE |
| **Language** | MicroPython |
| **USB Driver** | Silicon Labs CP210x USB to UART Bridge |
| **Servo Pin** | GPIO2 |
| **PWM Frequency** | 50 Hz |
| **PWM Resolution** | 10-bit (0–1023 duty range) |

---

## ⚙️ Requirements

- ESP8266 board (NodeMCU or compatible)  
- Servo motor (e.g., SG90, MG90S)  
- External 5V power supply (recommended for servo)  
- Micro USB cable  
- [Thonny IDE](https://thonny.org/)  
- [CP210x USB Driver](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)  
- MicroPython firmware flashed on ESP8266  

---

## ⚙️ Servo Timing Reference

| Servo Angle | Pulse Width | Duty (10-bit PWM) | Description |
|--------------|-------------|-------------------|--------------|
| 0° | 1.0 ms | ≈ 20 | Minimum position |
| 90° | 1.5 ms | ≈ 70 | Mid position |
| 180° | 2.0 ms | ≈ 120 | Maximum position |

🧩 **Note:**  
A **50 Hz frequency** means each PWM cycle lasts **20 ms**.  
Adjusting the **ON time** (1–2 ms) within that 20 ms frame controls the servo angle.

---

## 💻 Code

```python
# Time period = 20ms => Frequency = 1 / 20ms = 50Hz
# 10-bit PWM = ESP8266
# 1ms ON + 19ms OFF = 0 Degree
# 1.5ms ON + 18.5ms OFF = 90 Degree
# 2ms ON + 18ms OFF = 180 Degree

import machine
import utime

servo = machine.Pin(2, machine.Pin.OUT)
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
