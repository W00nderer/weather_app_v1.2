The program uses free AccuWeather API to get the weather for any city inputted in English or the language of its country.

The user is greeted with 5 options to choose from: current weather, weather for the next hour, weather for the next 12 hours, today's weather, and weather for the next 5 days, providing broad range of available forecasts.

![Screenshot 2025-05-05 104910](https://github.com/user-attachments/assets/edc97dae-2880-45ab-9702-4b2a278affaa)


When selecting any option (Option 1 on the screenshot below), the user is asked to input the city to search the forecast for.

![Screenshot 2025-05-05 104938](https://github.com/user-attachments/assets/8fba156d-4a8e-43a2-bb4d-c73c3fdcd3e8)

Each time the program encounters a new city that has not been requested before, it must first look up the city's code, which reduces the number of available requests by half.

To give us greater room for testing and using the program, after a successful request, the program will save the name and code of the city that has been inputted for the first time in a JSON file and load it at the start of the program:


![Screenshot 2025-05-05 105011](https://github.com/user-attachments/assets/f285a41a-06dd-4ad9-a3ca-a9d3568380e9)

In case of a wrong input, the program gives an error and returns to the main screen:

![image](https://github.com/user-attachments/assets/5f078697-c787-4407-b5ec-fb48ed709993)

The program also catches error status codes given by the API, like 503: exceeding the number of requests:

![image](https://github.com/user-attachments/assets/355c7eeb-a1a3-4773-bffc-23944415c01e)

The program accepts any city present in AccuWeather data base in English, but can only recognize the cities written in different language if it's the language of a country where the city is located:

![Screenshot 2025-05-05 114102](https://github.com/user-attachments/assets/86b579c1-34fa-474e-957f-d664d7f1d52c)

![Screenshot 2025-05-05 114128](https://github.com/user-attachments/assets/6bdbac45-c17c-44fd-9170-f34d2189423b)

![Screenshot 2025-05-05 114145](https://github.com/user-attachments/assets/0d5c7757-d13c-4803-bc68-3f8355fadb7e)

(In the example above: program has no problem returning the current weather for Seoul written in Korean(서울) but has a problem when Seoul is written in Russin(Сеул). Yet, the program returns Moscow written in Russian(Москва).)

The API key I use is stored in a .env file not visible to GitHub for privacy.

Example of 5 day forecast:

![Screenshot 2025-05-05 105205](https://github.com/user-attachments/assets/ae15e3ca-017c-46fc-8fff-8200ce72abb0)
![Screenshot 2025-05-05 105212](https://github.com/user-attachments/assets/8367b9ac-d78e-4a1e-82c6-9dd48e1dedfe)

The program is divided into 3 parts: main function, weather functions, and help functions to improve readability. All files are provided with comments explaining each section.

Possible improvements for the program:
1. Including the option to show fahrenheit units
2. Showing extended information such as real feel temperature, wind speed and direction, UV index, etc.
3. Providing analysis for average daily temperature for a certain month, comparing with other years.

This was my first experience with APIs, I had a lot of fun making this program, I appreciate any feedback and suggestions that could help me improve my skills working with APIs!

Thank you


