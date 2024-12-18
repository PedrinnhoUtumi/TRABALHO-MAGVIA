byte_sequence = b'{{'  # ou [0x7B, 0x7B]
number = int.from_bytes(byte_sequence, byteorder='big')  # 'big' pois o primeiro byte é mais significativo
print(number)  # Saída: 31611
