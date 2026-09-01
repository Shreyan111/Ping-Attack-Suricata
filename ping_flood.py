from pythonping import ping

host_address = input("Enter the host address to ping: ")

while True:
    try:
        response = ping(host_address, count=10000, timeout=1, size=1000)
        print(f"Ping to {host_address}: {response.rtt_avg_ms} ms")

    except KeyboardInterrupt:
        print("\nPing flood stopped by user.")
        break

    except Exception as e:
        print(f"Error pinging {host_address}: {e}")

    input("Press Enter to continue pinging or Ctrl+C to stop...")