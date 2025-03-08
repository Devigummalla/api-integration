# api-integration
company: codetech it solutions

name:G.J.V.N.Devi


Intern id:CT08SYG


Domain:python


Duration:4 weeks


Mentor:Neela Santhosh

This project is designed to integrate the OpenWeatherMap API to fetch real-time weather forecast data for a user-specified city and visualize temperature and humidity trends over five days. By leveraging Python’s capabilities in API handling, data extraction, and visualization, the project provides users with an intuitive and informative weather analysis tool. The script begins by prompting the user to enter the name of a city for which they wish to retrieve weather data. This city name is then used to construct a request URL that is sent to the OpenWeatherMap API, along with an API key, to obtain weather forecast details. The API returns a JSON response containing a wealth of weather-related data, including temperature, humidity, wind speed, and timestamps for different forecast intervals.

The script processes the received JSON data, extracting relevant fields such as timestamps, temperature readings, and humidity levels. These values are stored in lists, which are later used for visualization. The timestamps are converted into readable date-time formats using Python’s datetime module to enhance clarity. The extracted data is then visualized using Matplotlib and Seaborn, two powerful libraries for data representation. The program employs a dual-axis approach, where one axis represents temperature trends while the other shows humidity variations over time. This allows users to compare both parameters simultaneously, making the visualization highly informative.

To improve readability, Seaborn’s whitegrid style is applied to the plot, ensuring a clean and visually appealing presentation. The temperature trend is represented by a solid red line with circular markers, while the humidity trend is displayed as a dashed blue line with square markers. The x-axis is labeled with formatted timestamps, and both y-axes are clearly labeled to distinguish between temperature (in degrees Celsius) and humidity (in percentage). The graph is further enhanced by adding legends that indicate which line corresponds to which parameter, helping users interpret the data more effectively.

Error handling is a crucial aspect of this project. If the API request fails due to an incorrect city name, invalid API key, or network issues, the script gracefully handles the error and provides a user-friendly message indicating the problem. This ensures a smooth user experience and prevents unexpected crashes. Additionally, the project could be extended in several ways. Future enhancements could include adding wind speed and atmospheric pressure to the visualization, implementing an interactive graphical user interface (GUI) using Tkinter or Streamlit, allowing users to compare weather data for multiple cities, or even storing historical data in a database for long-term analysis.

In conclusion, this project demonstrates how Python can be used to integrate external APIs, process JSON responses, and visualize time-series data effectively. By utilizing OpenWeatherMap’s forecast API, users can gain valuable insights into upcoming weather conditions for their chosen location. The combination of API interaction, data processing, and visualization techniques makes this project a practical example of real-world Python programming. Whether used for personal weather tracking or as a foundation for more complex weather analysis applications, this project serves as an excellent learning experience for those interested in API integration and data visualization in Python.
