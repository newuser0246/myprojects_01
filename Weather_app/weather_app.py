import requests
import time as tm
import subprocess as sub
from simple_chalk import chalk


class Weather:
    def __init__(self, city, api_key) -> None:
        self.city = city
        self.api_key = api_key

         #checking for favorites
        self.move_to_favorites()
        try:
            choice = int(input(" Enter '1' if you want to auto_refresh the app after certain interval, else enter '0'  : "))
        except Exception as e:
            print(chalk.red("ERROR : "),chalk.red(e))
            exit()
        interval = 0
        if choice == 1 or choice == 0:
            if choice == 1:
                try:
                    interval = int(input("Enter the Interval Time (in seconds) : "))
                except Exception as e:
                    print(chalk.red("ERROR : "),chalk.red(e))
                    exit()
            self.run_app(choice,interval)
        else:
            print(chalk.red("Error : Wrong Input"))
            print("Please enter '1' or '0' ")
            exit()

    def initialize(self):
        baseURL = "https://api.weatherapi.com/v1/current.json"
        url = f"{baseURL}?key={self.api_key}&q={self.city}"
        try:
            response = requests.get(url)
        except Exception:
            print(chalk.red("Connection Error ! "),chalk.red("Make sure you are connected to the Internet."))
            exit()
        return response
           
    def execute(self,data):
        # Fetching the data from API Response
        last_updated = data["current"]["last_updated"]
        status = data["current"]["condition"]["text"]
        #icon = data["current"]["condition"]["icon"]
        city = data["location"]["name"]
        country = data["location"]["country"]
        temperature = data["current"]["temp_c"]
        feels_like = data["current"]["feelslike_c"]
        wind_speed = data["current"]["wind_kph"]
        humidity = data["current"]["humidity"]
        cloud = data["current"]["cloud"]
        gust_speed = data["current"]["gust_kph"]

        output = f"{str(city).upper(), str(country).capitalize()}\n\n"
        output += f"status : {status}\n\n"
        output += f"Temperature : {temperature}°C   Feels_like  : {feels_like}°C\n"
        output += f"Humidity : {humidity} %        Cloud : {cloud} %\n"
        output += f"Wind_speed : {wind_speed }kph    Gust  : {gust_speed} kph\n\n"
        output += f"(last_updated : {(last_updated)})"
        return output
    
    def move_to_favorites(self):
        # Added Add_To_Favorites Functionality
        try:
            choice = int(input(chalk.cyan("Enter '1' , if you want to Enter the favorites_section, else Enter 'any number': ")))
            if choice == 1:
                sub.run(['python','favourites.py'])
        except Exception as e:
            print(chalk.red("Wrong Input  ! , "),e)

    def run_app(self,choice,timer):
        #checking for API connection
        res = self.initialize() 
        if res.status_code != 200:
            print(chalk.red("ERROR! : City/Country Not Found"))
            exit()
        
        #Parsing the JSON response from the API
        data = res.json()
        output = self.execute(data)
        
        #Displaying the results
        if (output):
            print("\n\n")
            print(chalk.yellowBright(output))
        else:
            print(chalk.red("Some Unexpected Error Occured ..."))
            exit()
        
        # checking for auto_update
        while True:
            choice = input("\n Enter '0' to quit , else press 'Enter_key' to continue the Weather App : ")
            if choice == 0 or str(choice) == "0" :
                print("Exiting the Program ...")
                exit()            
            else:
                print(chalk.greenBright(" Program Status : Running ..."))
                print("Interval: ",timer," second(s)")
                tm.sleep(timer)
                self.run_app(choice,timer)
            

if __name__ == '__main__':
    key = "45bc75ebb89f418399745133242802"
    city = input("\nEnter the name of City/Country :: ")
    
    c1 = Weather(city,key)
    
    
