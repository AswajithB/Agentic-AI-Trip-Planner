import requests
import os
import shutil

def verify_pdf_generation():
    url = "http://localhost:8000/query"
    payload = {"question": "Plan a 1 day trip to London"}
    
    print(f"Sending request to {url}...")
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        
        print("Response received.")
        
        saved_file = data.get("saved_file")
        if saved_file and os.path.exists(saved_file):
            print(f"SUCCESS: File created at {saved_file}")
            
            if saved_file.endswith(".pdf"):
                 print("SUCCESS: File has .pdf extension.")
            else:
                 print(f"FAILURE: File does not have .pdf extension: {saved_file}")

        else:
            print(f"FAILURE: 'saved_file' key missing or file not found: {saved_file}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")

if __name__ == "__main__":
    verify_pdf_generation()
