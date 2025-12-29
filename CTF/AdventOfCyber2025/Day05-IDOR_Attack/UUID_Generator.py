import uuid
import datetime

def generate_v1_uuids():
    # --- Configuration ---
    # Target Date: 20 November 2025
    # Window: 20:00 UTC to 24:00 UTC (4 hours)
    start_time_iso = "2025-11-20 20:00:00"
    duration_hours = 4
    
    # Generate one UUID every minute: 4 hours * 60 minutes = 240 UUIDs
    total_uuids = 240
    
    # Reference UUID details (from user input) to maintain "Node" consistency
    # Ref: 463effe4-a3c8-11f0-96e7-026ccdf7d769
    # Node ID: 026ccdf7d769 (48 bits)
    # Clock Sequence: 0x16e7 (derived from 96e7 where 9 is variant 1001)
    node_id = 0x026ccdf7d769
    clock_seq = 0xac99 

	#37f0010f-a489-11f0-ac99-026ccdf7d769
    # --- Constants ---
    # UUID Epoch is October 15, 1582
    UUID_EPOCH = datetime.datetime(1582, 10, 15, tzinfo=datetime.timezone.utc)
    
    # Start time as datetime object
    start_dt = datetime.datetime.fromisoformat(start_time_iso).replace(tzinfo=datetime.timezone.utc)
    
    # Total duration in seconds
    total_seconds = duration_hours * 3600
    
    # Interval between UUIDs
    # 14400 seconds / 240 UUIDs = 60.0 seconds (1 minute) per UUID
    step_seconds = total_seconds / total_uuids
    
    print(f"Generating {total_uuids} UUIDs starting from {start_dt} UTC...")
    print(f"Step interval: {step_seconds} seconds")

    output_file = "uuid_list_v1.txt"
    
    with open(output_file, "w") as f:
        for i in range(total_uuids):
            # Calculate current time for this step
            current_dt = start_dt + datetime.timedelta(seconds=i * step_seconds)
            
            # 1. Calculate 100-nanosecond intervals since UUID Epoch
            delta = current_dt - UUID_EPOCH
            timestamp = int(delta.total_seconds() * 1e7)
            
            # 2. Construct the UUID fields
            # Time Low (32 bits)
            time_low = timestamp & 0xffffffff
            
            # Time Mid (16 bits)
            time_mid = (timestamp >> 32) & 0xffff
            
            # Time Hi and Version (16 bits)
            # Version 1 is 0x1xxx, so we mask the time bits and OR with version
            time_hi = (timestamp >> 48) & 0x0fff
            time_hi_and_version = time_hi | (1 << 12)
            
            # Pack it into standard UUID format
            generated_uuid = uuid.UUID(
                fields=(
                    time_low, 
                    time_mid, 
                    time_hi_and_version, 
                    (clock_seq >> 8) & 0xff, # Clock Seq Hi
                    clock_seq & 0xff,        # Clock Seq Low
                    node_id
                )
            )
            
            # Write to file
            f.write(f"{generated_uuid}\n")

    print(f"Done! {total_uuids} UUIDs saved to {output_file}")
    
    # Print first and last 3 for verification
    print("\n--- Preview ---")
    with open(output_file, "r") as f:
        lines = f.readlines()
        for line in lines[:3]: print(line.strip())
        print("...")
        for line in lines[-3:]: print(line.strip())

if __name__ == "__main__":
    generate_v1_uuids()
