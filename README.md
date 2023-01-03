#  ESP32: Micropython Web server with  SYSTEM control panel + Weather Station                                 
                                   " Connecting world ,down to Earth"
  ![image](https://user-images.githubusercontent.com/121890637/210415215-8061e4a0-7d1c-425f-9211-69d9a9dc0c1c.png) 
  
![image](https://user-images.githubusercontent.com/121890637/210415812-e357f53c-9e5e-446d-bae6-86a66e6728a0.png)

This is an asynchronous ESP32 web server with the DHT11 that displays temperature and humidity using esp32 using MicroPython Code.
We will first interface the Sensor with ESP32 only and check the temperature and humidity reading in Shell Window. Similarly, we will add extra 0.96″/1.3″ I2C  oled display to the same circuit and display the Humidity Temperature reading on OLED Screen.

![image](https://user-images.githubusercontent.com/121890637/210415846-b0b7192c-4abd-4b89-949a-99e8b3be4da9.png)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/121890637/210417511-3906a461-4e96-42ef-9ccd-43fda5828cb5.png)



  ![image](https://user-images.githubusercontent.com/121890637/210416427-9afae960-e92a-4b97-b38b-c8d186ca726e.png)
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------
  
![image](https://user-images.githubusercontent.com/121890637/210417606-1d9ba95f-74a3-4762-b8eb-1ba6b015f8ef.png)
     
     -User are able to control , system remotely  - system reboot, deep sleep ,led on ,led off, send mail.

    -User will get email that contain device data.
  
    -The web server we’ll build updates the readings    
      automatically with the need to refresh the web page.

     -Display the Humidity Temperature reading on OLED Screen.

---------------------------------------------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/121890637/210418305-6f14c465-d081-4eb3-8dc2-2a1df36342c0.png)

    -ESP32 ESP-32S Development Board (ESP-WROOM-32)

    -DHT11 Humidity Temperature Sensor

    -Jumper Wires

    -Breadboard

    - Oled 
---------------------------------------------------------------------------------------------------------------------------------------------------------------

  DHT11 Humidity Temperature Sensor![image](https://user-images.githubusercontent.com/121890637/210418826-09d44ed9-2353-4cce-a136-c0410fcc9868.png)

![image](https://user-images.githubusercontent.com/121890637/210418905-52aa47c4-78f8-4079-82e5-e0f2a11286bb.png)

The DHT11 is a basic, ultra low-cost digital temperature and humidity sensor. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air, and spits out a digital signal on the data pin (no analog input pins needed).
![image](https://user-images.githubusercontent.com/121890637/210421704-215c5f1f-d4ed-4cac-924e-1ee6fb192a91.png)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

Interfacing DHT11 Sensor with ESP32 using MicroPython Code![image](https://user-images.githubusercontent.com/121890637/210419304-b569923a-7b51-4783-9654-43107b76e8dc.png)
DHT11 Sensor & ESP32 & start with MicroPython Code for measuring Humidity & Temperature. The connection is fairly simple. Connect the DHT11 VCC & GND pin to ESP32 3.3V Pin & GND Pin. Connect the digital output pin to ESP32 GPIO5 Pin.
![image](https://user-images.githubusercontent.com/121890637/210419332-f8dfe227-babb-4b53-8be9-890febb4a6a3.png)

![image](https://user-images.githubusercontent.com/121890637/210419365-3050a5af-4126-48fa-b147-e2b9330d8ab1.png)

---------------------------------------------------------------------------------------------------------------------------------------------------------------
ESP32 DHT11 MicroPython Code![image](https://user-images.githubusercontent.com/121890637/210419773-e3a36182-23dd-4c46-bc03-a55ac604c25d.png)

       from machine import Pin
       from time import sleep
       import dht 
       sensor = dht.DHT11(Pin(5))
       while True:
         try:
           sleep(2)
           sensor.measure()
           t = sensor.temperature()
           h = sensor.humidity()
           print('Temperature: %3.1f C' %t)
           print('Humidity: %3.1f %%' %h)
         except OSError as e:
           print('Sensor Reading Failed')

---------------------------------------------------------------------------------------------------------------------------------------------------------------

Monitor DHT11 Humidity Temperature Data on OLED with MicroPython Code![image](https://user-images.githubusercontent.com/121890637/210420628-f379aaa3-5cc2-44a3-83c5-21e80d662817.png)
Here is the connection diagram. The OLED Display is an I2C Module. So connect the SDA & SCL pin of OLED Display to ESP32 D26 & D25 Pin respectively.
![image](https://user-images.githubusercontent.com/121890637/210420660-4728a8c0-9002-4c3a-8f91-a6c65c358a93.png)

![image](https://user-images.githubusercontent.com/121890637/210420682-ed062498-3ffe-4f4d-b2ab-dc04df18e439.png)
---------------------------------------------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/121890637/210421114-8cf40745-9b25-4f6f-80ce-67033b771e1a.png)

Open a browser and type the ESP32 IP address. Your web server should display the latest sensor readings.
![image](https://user-images.githubusercontent.com/121890637/210421147-f8538b3c-4a0a-4f95-8c3d-6643bf620249.png)

![image](https://user-images.githubusercontent.com/121890637/210421263-a7f32643-e744-404b-b36e-51af32a0e06a.png)


![image](https://user-images.githubusercontent.com/121890637/210421203-2bdee35d-7662-4240-afaf-f15ce34c3229.png)
