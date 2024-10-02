import weather_analyzer

def main():
    filename = input("Enter the weather data file name: ")
    try:
        data = weather_analyzer.read_weather_data(filename)
        avg_temp = weather_analyzer.calculate_average_temperature(data)
        total_rainfall = weather_analyzer.calculate_total_rainfall(data)
        highest_temp_day = weather_analyzer.find_highest_temperature_day(data)

        print(f"Average Temperature: {avg_temp: .2f}°C")
        print(f"Total Rainfall: {total_rainfall}mm")
        print(f"Highest Temperature on Day: {highest_temp_day}")
    except FileNotFoundError:
        print("File note found. Please check the file name")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()