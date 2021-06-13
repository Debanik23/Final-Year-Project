from ultrasonic import *
from mlxread import *
from pi_face_recognition import getFace
import requests
import time
import drivers
from lcd_scroll import long_string

display = drivers.Lcd()



while True:
    display.lcd_clear()
    distance = ultrasonic()
    if int(distance) < 50:
        display.lcd_display_string("Commencing Face ", 1)
        display.lcd_display_string("Recognition...", 2)
        time.sleep(2)
        display.lcd_clear()  
        display.lcd_display_string("Please face the", 1)
        display.lcd_display_string("camera...", 2)
        
        result = getFace()
        if result == "Unknown":
            display.lcd_clear() 
            display.lcd_display_string("Not a familiar", 1)
            display.lcd_display_string("face", 2)
            print("Not a Familiar Face")
            time.sleep(2)
            #Gate remains closed
            continue

        else:
            display.lcd_clear()  
            display.lcd_display_string("Welcome !", 1)
            time.sleep(2)
            display.lcd_clear()  
            display.lcd_display_string("Measuring", 1)
            display.lcd_display_string("temperature...", 2)
            time.sleep(3)
            display.lcd_clear()
            long_string(display, "Please keep your hand in front of the sensor", 1)
            print("Measuring temperature..Please keep your hand in front of the sensor.")
            temp = get_temp()
            if temp < 37 :
                display.lcd_clear()
                print("temperature ok!")
                display.lcd_display_string("temperature ok!", 1)
                time.sleep(2)
            else:
                display.lcd_clear()
                print("temperature high!")
                display.lcd_display_string("temperature High!", 1)
                time.sleep(2)
                #send email
                #Gate Open
            pload = {"name":int(result),"temp":temp}
            print(pload)
            r = requests.post('http://asst-tech.herokuapp.com/api/visitor',data = pload)
            print(r.json())
            
    else:
        print("come closer")


