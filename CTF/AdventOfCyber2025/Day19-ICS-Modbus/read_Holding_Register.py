from pymodbus.client import ModbusTcpClient
client = ModbusTcpClient('10.65.154.75', port=502)
# Establish connection
if client.connect():
	print("Connected to PLC successfully")
	# Read holding register 0 (Package Type)
	result = client.read_holding_registers(address=0, count=1, slave=1)
	if not result.isError():
		package_type = result.registers[0]
		print(f"HR0 (Package Type): {package_type}")
		if package_type == 0:
			print("  Christmas Presents")
		elif package_type == 1:
			print("  Chocolate Eggs")
		elif package_type == 2:
			print("  Easter Baskets")
	#delivery zone
	result = client.read_holding_registers(address=1, count=1, slave=1)
	if not result.isError():
		Delivery_Zone = int(result.registers[0])
		print(f"HR1 (Delivery Zone): {Delivery_Zone}")
		if Delivery_Zone >= 1 and package_type <= 9:
			print("  normal")
		else:
			print("  WARNING: Ocean dump zone")
	# HR4 -> System signature
	#Default is 100
	result = client.read_holding_registers(address=4, count=1, slave=1)
	if not result.isError():
		signature = int(result.registers[0])
		print(f"HR4 (System signature): {signature}")
		if signature == 100:
			print("  normal")
		else:
			print("  WARNING: Wrong signature")
			
	print("<Coils Investigation ----->")
	lst = ["Inventory_Verification","Protection_Override","","",""]
	for i in range(10,15+1):
		result = client.read_coils(address=i, count=1, slave=1)
		if not result.isError():
			verification = result.bits[0]
			print(f"C{i} Status: {verification}")
	
else:
	print("Connection failed")

	


