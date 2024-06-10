import requests

API_KEY = "8e2f8c907063f1717fcf325d0fbd9ba1"


def get_data(place, days=None, option=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nbr_values = 8 * days
    filtered_data = filtered_data[:nbr_values]
    if option == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if option == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Berlin", days=2, option="Sky"))