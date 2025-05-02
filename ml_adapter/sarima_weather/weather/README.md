1. Create a new empty resource on the Waylay console
2. Run `weatherHistory.ipynb`: as indicated in the first cell, you will need to 
    * set the ResourceId parameter
    * download the CSV file containing historic weather data (link in notebook) and store it as `weatherHistory.csv`
3. Upload the provided sensor `sensors-GetWeatherAdjusted-1.0.3.json` if it does not exist already
4. Upload the provided rule template `HourlyWeather.json`
5. Create a task for this template and resource, with the desired period