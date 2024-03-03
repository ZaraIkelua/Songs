# Artist - Album list application
- this application shows the list of all the artists availbale in our database.
- then you can see the list of all the songs and their detils into the page next to it by clicking on the link

## Design - 
1. system has two tables - `artist` and `album`
2. `album` is dependent on `artist`

![ER Diagram](https://github.com/ZaraIkelua/Songs/assets/160255109/4476a8f7-2dac-4e6e-83a1-000ed7b022cf)

## Development - 
1. Used python to read the data from csv file and then write it into sqite3 database
2. Flask framework is used to make visual represtation and backend
3. There are total `2 endpoints` in the system
   - `/` to get the list of all the available artists in our system.
   - `/show/<id>` to show the list of albums available for that artist
4. there the `templates` that are used by these endpoints
5. Working directory structure
 ```terminal
   ├───data
   |   └───albums_csv.csv
   ├───templates
   |   └───index.html
   |   └───show.html
   |───parse_csv.py
   |───app.py
   |─── songs.db
   |─── requirements.txt
```

## Implementation 
1. `artist` tables holds the name of each artists name in a seperate table
2. `album` tables has an attribute of `INTEGER` type named `artist` which hold the `id` of corresponding artist present into `artist` table
3. In `/` endpoint we show the list of all the artists

![image](https://github.com/ZaraIkelua/Songs/assets/160255109/4e634b51-eca8-41c7-88db-2a919589ba44)
4. click on the name of artist to show the list of albums from that artist and other details. 

![image](https://github.com/ZaraIkelua/Songs/assets/160255109/895222f4-f09a-4132-8f6f-854518e2edc9)

5. If any artist have no albums then it shows bellow output.

![image](https://github.com/ZaraIkelua/Songs/assets/160255109/bb86cd3e-c424-4b87-81ac-3f9e525437f2)

     
## Installation
1. Clone the repository
2. install flask
   ```terminal
   pip install flask
   ```
3. move to the root directory of the project
4. run `parse_csv.py` file
   ```terminal
   python ./parse_csv.py
   ```
   it will take some time to load the data into the database.
5. then run the flask application
  ```terminal
  flask run
  ```
