import subprocess

def list_wifi_routers():
    try:
        # Execute the nmcli command to list available Wi-Fi networks
        result = subprocess.run(
                ['nmcli', '-f', 'SSID, BSSID, SIGNAL', 'dev', 'wifi'],
                capture_output=True,
                text=True
                )

        # Check for command execution errors
        if result.returncode != 0:
            print("Error executing nmcli:", result.stderr)
            return

        # Parse and display the output
        lines = result.stdout.strip().split('\n')
        if len(lines) < 2:
            print("No Wi-Fi networks found")
            return

        # Print header
        print(f"{'SSID':<30}{'BSSID':<20}{'RSSI (Signal Strength)'}")
        print("-"*70)

        # Parse and display each Wi-Fi network 
        # Skip the header line
        for line in lines[1:]:
            # Split the line into columns
            parts = line.split()
            if len(parts) >= 3:
                ssid = ' '.join(parts[:-2]).strip()
                bssid = parts[-2]
                rssi = parts[-1]
                print(f"{ssid:<30}{bssid:<20}{rssi}")

    except FileNotFoundError:
        print("Error: 'nmcli' command not found. Ensure NetworkManager is installed")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    list_wifi_routers()

