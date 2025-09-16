import serial
ser = serial.Serial("/dev/ttyCH341USB0", baudrate = 9600, bytesize = 8, parity = 'N', stopbits = 1)

def send_hex_data(hex_string):
    byte_array = bytearray.fromhex(hex_string)

    ser.write(byte_array)

# hex_data = 'A0 07 01 A8'
# hex_data = 'A0 07 00 A7'
hex_data = 'A0 06 00 A6'
# hex_data = 'A0 06 01 A7'
# hex_data = 'A0 08 00 A8'
# hex_data = 'A0 05 01 A6'
# hex_data = 'A0 06 01 A7'

send_hex_data(hex_data)

ser.close()

# #sudo chmod 777 /dev/ttyCH341USB0 


# import serial.tools.list_ports

# # 获取串口列表
# uart_class = list(serial.tools.list_ports.comports())
# if len(uart_class) <= 0:
#     print("can't find the urat")
# else:
#     for i in uart_class:
#         uart_temp_str = str(i)
#         uart_list = uart_temp_str.split()
#         for j in uart_list:
#             if "CH340" == j:
#                 uart_num = uart_list[0]
#                 print(uart_num)