#!/usr/bin/env python3
import datetime
import urllib.request
import json
import reverse_geocoder as rg


# part1
def main():
    URL = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(URL).read()
    output_json = json.loads(response.decode())
    print(output_json)

# part2
    if (output_json["message"] == "success"):
        print("CURRENT LOCATION OF THIS ISS:")
        print(f'Lon: {output_json["iss_position"]["longitude"]}')
        print(f'Lat: {output_json["iss_position"]["latitude"]}')

# part3
        epoch = output_json['timestamp']
        utctime = datetime.datetime.fromtimestamp(
            epoch).replace(tzinfo=datetime.timezone.utc)
        local_time = utctime.replace(
            tzinfo=datetime.timezone(datetime.timedelta(hours=-7)))
        print(f"Timestamp: {local_time}")

# part4
        lon = output_json["iss_position"]["longitude"]
        lat = output_json["iss_position"]["latitude"]

        coords_tuple = (lat, lon)

        result = rg.search(coords_tuple, verbose=False)

        city = result[0]["name"]
        country = result[0]["cc"]

        print(f"City/Country: {city}, {country}")


if __name__ == "__main__":
    main()

