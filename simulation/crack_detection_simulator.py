import random
import time

def simulate_crack_detection():
    print("🚂 Railway Track Crack Detection System Started...\n")
    sections = 10
    for i in range(1, sections + 1):
        crack_found = random.choice([True, False, False, False])
        print(f"Scanning Section {i}...")
        time.sleep(1)
        if crack_found:
            print(f"⚠️ Crack detected at Section {i}! Notifying control center...\n")
        else:
            print("✅ No crack found.\n")
    print("🔁 Scanning cycle complete. System on standby.")

simulate_crack_detection()
