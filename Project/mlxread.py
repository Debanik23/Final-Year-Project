from smbus2 import SMBus
from mlx90614 import MLX90614
import time
import drivers
display = drivers.Lcd()

def get_temp():
    bus = SMBus(1)
    sensor = MLX90614(bus, address=0x5A)
    
    ambient_temp = int(sensor.get_ambient())
    object_temp = int(sensor.get_object_1())
    bus.close()
    
    return object_temp


# while True:
#     a=get_temp()
#     print(a)
#     display.lcd_display_string(f'{a}', 1)  # Write line of text to first line of display
#     time.sleep(3)
#     display.lcd_clear() 
