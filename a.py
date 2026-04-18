import serial
import time

RUN_2D = [0x5A, 0x77, 0xFF, 0x02, 0x00, 0x01, 0x00, 0x03]

try:
    # 1. 포트 개방
    ser = serial.Serial('/dev/ttyUSB0', 3000000, timeout=1)
    print("✅ Port Open:", ser.name)
    
    # 2. 구동 명령 전송
    ser.write(bytes(RUN_2D))
    print("✅ Command Sent. Reading raw hex data for 3 seconds...\n")
    
    # 3. 3초간 수신되는 모든 원시 데이터를 Hex로 출력
    end_time = time.time() + 3
    while time.time() < end_time:
        if ser.in_waiting > 0:
            raw_data = ser.read(ser.in_waiting)
            print(raw_data.hex(' '))  # 바이트 단위로 띄어쓰기해서 출력
        time.sleep(0.05)
        
    ser.close()
    print("\n✅ Test Finished.")

except Exception as e:
    print("❌ Error:", e)
