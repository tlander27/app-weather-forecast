import requests

API_KEY = key-here


def get_data(place, days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nbr_values = 8 * days
    filtered_data = filtered_data[:nbr_values]
    return filtered_data


if __name__ == "__main__":
    get_data(place="asdf", days=2)
