import os
from google import genai

# Use your actual API key
API_KEY = "AIzaSyAGcUGYnFMmaO81IKrDyA1Au6HSjYNhCDM"

client = genai.Client(api_key=API_KEY)

print("Fetching available Free Tier models for your key...")
print("-" * 50)

try:
    # In the new SDK, models.list() returns a generator of Model objects
    for model in client.models.list():
        # Check if the model supports generating content
        # The new SDK uses 'supported_methods' as a list of strings
        if hasattr(model, 'supported_methods') and 'generateContent' in model.supported_methods:
            model_id = model.name.replace('models/', '')
            print(f"Model ID:    {model_id}")
            print(f"Display Name: {model.display_name}")
            print("-" * 50)
        # If the above fails, let's just print everything to be safe
        elif not hasattr(model, 'supported_methods'):
             print(f"Model Found: {model.name}")

except Exception as e:
    print(f"Detailed Error: {e}")
    # Fallback: Just try to print the raw model name if it's a different object type
    print("Trying simplified list...")
    for m in client.models.list():
        print(f"- {m.name}")