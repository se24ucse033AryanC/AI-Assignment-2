# Simple Reflex AQI Agent

def calculate_aqi(pm25):

    if pm25 <= 30:
        return "Good"
    elif pm25 <= 60:
        return "Satisfactory"
    elif pm25 <= 90:
        return "Moderate"
    elif pm25 <= 120:
        return "Poor"
    elif pm25 <= 250:
        return "Very Poor"
    else:
        return "Severe"


def read_sensor_data(file):

    with open(file, "r") as f:
        pm25 = float(f.read().strip())

    return pm25


def main():

    pm25 = read_sensor_data("sensor_data.txt")

    aqi = calculate_aqi(pm25)

    print("PM2.5 Value:", pm25)
    print("AQI Status:", aqi)


if __name__ == "__main__":
    main()