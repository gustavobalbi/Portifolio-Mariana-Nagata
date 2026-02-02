import urllib.request
import json
import re

url = "https://script.google.com/macros/s/AKfycbwW9bozMP1wxp83gHWAPCP2bjXYtBySjlu3TmJ_r30FwxkaKHi7J_iP5eIyEnjQW-tp/exec"
try:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        if data:
            original_url = data[0]["url"]
            print(f"Original: {original_url}")

            # Extract ID
            match = re.search(r"id=([a-zA-Z0-9_-]+)", original_url)
            if match:
                file_id = match.group(1)
                print(f"File ID: {file_id}")

                # Try LH3 URL
                lh3_url = f"https://lh3.googleusercontent.com/d/{file_id}"
                print(f"LH3 URL: {lh3_url}")

                try:
                    img_resp = urllib.request.urlopen(lh3_url)
                    print(f"LH3 Status: {img_resp.getcode()}")
                except Exception as e_lh3:
                    print(f"LH3 Error: {e_lh3}")
            else:
                print("Could not extract ID")

except Exception as e:
    print(f"Error: {e}")
