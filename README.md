# Socket-Programming-and-Data-Visualization_b08901066


## set up
1,確保你的server host跟stm32板子連到同一個網路
2,在server.py中host填入socket server的ip
3,在mbed_json填入wifi-SSID, password
4,確保防火牆不阻撓stm32連到server




## run code
1.先跑server.py
2.再跑main.cpp，之後重複按stm32的reset鍵 就可以重跑

## reference
引入板子型號的函式庫() https://os.mbed.com/teams/ST/code/BSP_B-L475E-IOT01//file/bfe8272ced90/Drivers/BSP/B-L475E-IOT01/
處理mbed printf 函式庫的不完整 https://os.mbed.com/teams/ST/code/BSP_B-L475E-IOT01//file/bfe8272ced90/Drivers/BSP/B-L475E-IOT01/

