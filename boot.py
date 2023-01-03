

import network
import machine
from machine import TouchPad,Pin,I2C
from machine import PWM
import time
import usocket as socket
import time
import esp32
import json
import ssd1306
import dht
import umail


from machine import RTC



tp = TouchPad(Pin(14))

i2c = machine.I2C(1, scl = machine.Pin(25), sda = machine.Pin(26), freq = 400000)    #Init i2c
oled=ssd1306.SSD1306_I2C(128,64,i2c,0x3c) 
 
p15=Pin(5, Pin.IN)
d=dht.DHT11(p15)

rtc = RTC()
rtc.datetime() # set a specific date and time
rtc.datetime() # get date and time


#change your wifi credentials here.
ssid = 'yourssid'
password = '12345678'



#here we set up the network connection
station = network.WLAN(network.STA_IF)
station.active(False)
station.active(True)
#station.config(reconnects = 5)

station.connect(ssid,password)

while station.isconnected() == False:
  pass
print(station.ifconfig())


# Initialising Socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET - Internet Socket, SOCK_STREAM - TCP protocol

Host = '' # Empty means, it will allow all IP address to connect
Port = 80 # HTTP port
s.bind((Host,Port)) # Host,Port

s.listen(5) # It will handle maximum 5 clients at a time
print("server create")

while True:
  
# HTML Document
  d.measure()       #Measurement of temperature and humidity
  t=d.temperature() #Read Celsius temperature
  h=d.humidity()    #Read relative humidity
  
  time.sleep(0.3)                #Delay of 1 second
  
  oled.fill(0)
  oled.text("Temperature",20,10)
  oled.text(str(t),40,20)
  oled.text("*C", 60,20)
  oled.text("Humidity",30,40)
  oled.text(str(h),40,55)
  oled.text("%", 60,55)
  oled.show()

  yu=esp32.raw_temperature()
  date=rtc.datetime()
  magnetic=esp32.hall_sensor()
  fre=machine.freq()
  tou=tp.read()


  jsonResult = {"room temperature ": t ,"room Humidity ": h ,"date and time ": date ,"Raw temperature sensor": yu ,"Hall effect(magnetic) sensor ":magnetic,"machine frequency ": fre,"ESP32 internal touch sensor pin 14 ": tou,
  }
  html = ''' 

  <!DOCTYPE html>
  <html>

  <center><h2 style="color:green";>ESP32 SYSTEM control panel .  Down to earth </h2></center>
  <hr>
  <form style="color:blue;">
  <center>
  <h3> <u>Device control panel</u> </h3>

  <button style="height:100px;width:200px;background-color: #4CAF50" name="LED" value='ON' type='submit'><h2>Led  ON </h2></button>
  <button style="height:100px;width:200px;background-color: #4CAF50" name="LED" value='OFF' type='submit'> <h2>Led OFF </h2></button><br><br>
  <button style="height:100px;width:200px;background-color: #4CAF50" name="command" value='deepsleep' type='submit'><h2>  Deepsleep 10 sec </h2></button>
  <button style="height:100px;width:200px;background-color: #4CAF50" name="command" value='reset' type='submit'> <h2>Reset </h2></button>
  <button style="height:100px;width:200px;background-color: #4CAF50" name="command" value='sendmail' type='submit'> <h2>send mail </h2></button>
  </center>
  <br>
  <hr>



  '''+ "room temperature = "+json.dumps(t) + "&nbsp &nbsp &nbsp"+"  room Humidity = " + json.dumps(h)+"<br>"+" Date and Time = "+ json.dumps(date) + "<br>" +"Raw Device temperature = "+ json.dumps(yu)+"<br>"+"Hall effect(magnetic) = "+ json.dumps(magnetic)+"<br>"+"machine frequency = "+ json.dumps(fre)+"<br>"+"ESP32 internal touch sensor pin 14 = "+ json.dumps(tou)                                                     


  pwm = PWM(Pin(2))
  pwm.duty(0)


  pwm.freq(1)
  

  
  connection_socket,address=s.accept() # Storing Conn_socket & address of new client connected
  print("Got a connection from ", address)
  request=connection_socket.recv(1024) # Storing Response coming from client
  print("Content ", request) # Printing Response 
  request=str(request) # Coverting Bytes to String
    # Comparing & Finding Postion of word in String 
  LED_ON =request.find('/?LED=ON')
  LED_OFF =request.find('/?LED=OFF')
  deepsleep =request.find('/?command=deepsleep')
  reset =request.find('/?command=reset')
  sendmail =request.find('/?command=sendmail')
  
  if(LED_ON==6):
    pwm.duty(1023)
    pwm.duty(1023)
    pwm.duty(1023)
    pwm.duty(1023)

    
  if(LED_OFF==6):
    pwm.duty(0)
  
  if(deepsleep==6):
    machine.deepsleep(10000)
    
  if(reset==6):
    machine.reset()
    
  if(sendmail==6):
    smtp = umail.SMTP('smtp.gmail.com', 587, username='devilbnfghff@gmail.com', password='lvcghfghff') 
    smtp.to('devilfhfhhgfgr@gmail.com') 
    smtp.send("(esp32 server temperature data ) "+"    "+"room temperature = "+json.dumps(t) + "       "+"  room Humidity = " + json.dumps(h)+"       "+"Date and Time = "+ json.dumps(date) + "     " +"Raw Device temperature = "+ json.dumps(yu)+"    "+"Hall effect(magnetic) = "+ json.dumps(magnetic)+"   "+"machine frequency = "+ json.dumps(fre)+"   "+"ESP32 internal touch sensor pin 14 = "+ json.dumps(tou) ) 
    smtp.quit()
    
    
  # Sending HTML document in response everytime to all connected clients  
  response=html 
  connection_socket.send(response)
  
  #Closing the socket
  connection_socket.close() 









