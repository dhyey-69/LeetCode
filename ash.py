import random

ash_coming = random.choice([True, False])  # Whether Ash is coming or not
presentation_end_time = random.randint(10, 13)  # Random end time between 10 AM and 1 PM
teammate_interference = random.choice([True, False])  # Whether teammate will mess things up
ash_accepts_ride = random.choice([True, False])  # Whether Ash agrees to the ride
transport_mode = random.choice(["Home", "Bus Station"])  # Where Ash is headed
situation = "Pending"

if not ash_coming:
    
    situation = "Mission Failed: Ash not coming 💀"

else:
    print("✅ Ash is coming to college!")

    if presentation_end_time > 12:
        situation = "❌ Too Late: No time to drop Ash, mission failed."
    else:
        print(f"✅ Presentation ends early at {presentation_end_time}:00 AM!")

        if teammate_interference:
            print("⚠️ Teammate says: 'We’re getting late for office!'")
            ash_accepts_ride = False

        if ash_accepts_ride:
            print(f"🚗 Success! Ash accepts the ride and is dropped at {transport_mode}.")
            situation = f"🎉 Mission Success: Dropped Ash at {transport_mode}!"
        else:
            situation = "❌ Ash declined the ride (maybe hesitation, maybe teammate interference)."

print("\n=== FINAL OUTCOME ===")
print(situation)