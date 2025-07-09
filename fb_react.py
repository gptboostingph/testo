import uiautomator2 as u2
import time
import json

# Load coordinates
with open("coordinates.json", "r") as f:
    coords = json.load(f)

# Connect to device
print("[*] Connecting to device...")
d = u2.connect()

# Get inputs
post_url = input("Enter Facebook post URL: ").strip()
reaction = input("Enter reaction (like, love, haha, wow, sad, angry): ").lower()

# Reaction positions
reaction_pos = coords["reactions"].get(reaction)
if not reaction_pos:
    print(f"[-] Unknown reaction type: {reaction}")
    exit()

# Function: React to post
def react_to_post():
    print("[*] Launching Facebook Lite...")
    d.app_start("com.facebook.lite")
    time.sleep(3)

    print("[*] Navigating to post...")
    if d(resourceId="com.facebook.lite:id/search_edit_text").exists:
        d(resourceId="com.facebook.lite:id/search_edit_text").click()
        d.send_keys(post_url)
        d.press("enter")
        time.sleep(5)

    print("[*] Performing reaction...")
    if d(descriptionContains="Like").exists:
        d(descriptionContains="Like").long_click()
        time.sleep(2)
        d.click(*reaction_pos)
        print(f"[+] Reacted with {reaction.upper()}")
        return True
    else:
        print("[-] Could not find like button.")
        return False

# Function: Switch Account
def switch_account():
    print("[*] Switching account...")
    d(description="Menu").click()
    time.sleep(1)
    d.click(*coords["switch_button"])  # Tap 'Switch account'
    time.sleep(2)
    d.click(*coords["next_profile"])   # Tap on next profile
    time.sleep(5)

# Start reacting loop
for i in range(coords["account_count"]):
    print(f"[*] Reacting with account #{i+1}")
    if react_to_post():
        if i < coords["account_count"] - 1:
            switch_account()
    else:
        print("[-] Reaction failed, skipping account switch.")
💬 Let Me Know:
Would you like me to:

✅ Repackage this into a clean .zip again?

🛑 Add a stop prompt (e.g. Type stop to end after each loop)?

🔁 Add looping through a list of post links instead of just one?

You're super close now — just need to run the clean .py and you're good to go.









