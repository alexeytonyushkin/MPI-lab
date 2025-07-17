import tldevice
import serial.tools.list_ports
import time
import matplotlib.pyplot as plt

ports = serial.tools.list_ports.comports()

print("Available serial ports:")
for port in ports:
    print(f"  {port.device} - {port.description}")

device = tldevice.Device("COM7")

magneto_data1 = []
magneto_data2 = []
num_samples = 100

for i in range(num_samples):
    data = device.field()
    field_data2 = device.field2()
    magneto_data1.append(data)
    magneto_data2.append(field_data2)
    print("Magnetometer Data:", data)
    time.sleep(0.1)

plt.plot(magneto_data1)
plt.plot(magneto_data2)
plt.show()
field_data2 = device.field2()
print("Magnetometer Data (Field2):", field_data2)

# Or check the status of the device
device_status = device.status()
print("Device Status:", device_status)


file = open('log.tsv', 'w')
for row in device.data.stream_iter():
    rowstring = "\t".join(map(str, row)) + "\n"
    file.write(rowstring)

# Get the mode of the device (e.g., operational mode)
mode_info = device.mode()
print("Device Mode:", mode_info)

