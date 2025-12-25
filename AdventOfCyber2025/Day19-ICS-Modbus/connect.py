from pymodbus.client import ModbusTcpClient
# Connect to the PLC on port 502
client = ModbusTcpClient('10.65.154.75', port=502)

# Establish connection
if client.connect():
	print("Connected to PLC successfully")
else:
	print("Connection failed")
