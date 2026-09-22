import requests

ACCESS_TOKEN = "AQVpixnM6tOwczMxBtybgySc0SBUVZ9MTvxyFyXnG5s_9OspuY8wGOjuoEekQX1uwXoVvijAGJc16iKDWMpGe1BPHZozSK39UlL5hTD1berbMhzUFoA3qbfBgCmqyNCcVHbVtHuONbGDcqGEN4-bioRkhFjQvLYjKCgj8J7VYt_YN3o93PhLVSVuJwP3cESDMxARN1-FrDbA-OMcW91JL5wknqgF_Q5WgW72DC81wIHdag_NuN1TfVju2ZNUgrKsSaMB3XC5ZvFqVuRk7YCUn3JG9PtHtntg3HJ4bLgwwss_u3qZeCfRcNHL_YOP31Kcu73hPrABm2GruYhfFoydX0YAOoQBlA"



headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "X-Restli-Protocol-Version": "2.0.0",
}

response = requests.get(
    "https://api.linkedin.com/v2/me",
    headers=headers
)

print("Status Code:", response.status_code)
print("Response:")
print(response.text)