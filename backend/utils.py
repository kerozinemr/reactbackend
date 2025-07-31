import requests

def get_ors_route(coordinates):
    # Replace with your actual ORS API key
    api_key = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImY2ZmM1YmMzZDI0ZjRjNzFhYTY1NDNmYTM3YWZhODdlIiwiaCI6Im11cm11cjY0In0="
    
    url = "https://api.openrouteservice.org/v2/directions/driving-car"
    
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'coordinates': coordinates  # Expected: [[lng, lat], [lng, lat], ...]
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"ORS API Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error calling ORS API: {e}")
        return None