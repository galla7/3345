import os

# Fetch API key from environment variable (for secrets workflow)
API_KEY = os.getenv("API_KEY")  
# API_KEY = "12345-INSECURE-KEY"  # For hardcoded workflow (DON'T COMMIT THIS!)

def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    print(get_weather("London"))
