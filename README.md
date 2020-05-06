# CourseParser

Python script scrapes and parses the course information of every course offered at all three campuses of the University of Toronto.

## Getting Started 
1. Create a venv 
```bash 
> python3 -m venv ./env 
```

2. Activate the venv 
```bash 
> source ./env/bin/activate 
```

3. Install the required packages 
```bash 
(env) > pip3 install requests 
(env) > pip3 install beautifulsoup4
```
4. Run the scraper 
```bash 
(env) > python3 Main.py
```

#
Below is the course information of course ```AER373H1S``` outputted by the script in a JSON file. 

```JSON
...
{
            "breadth requirements":null,
            "campus":"UTSG",
            "course code":"AER373H1S",
            "course department":"Division of Engineering Science",
            "course division":"Faculty of Applied Science & Engineering",
            "course exclusion":null,
            "course level":"300/C",
            "course name":"Mechanics of Solids and Structures",
            "course prerequisites":[
                "CIV102H1"
            ],
            "sections":[
                {
                    "Activity":"Lec 0101",
                    "Class Size":"40",
                    "Day and Time":"TUESDAY 16:00-18:00 WEDNESDAY 15:00-16:00",
                    "Instructor":"C Steeves",
                    "Location":"SS 2135 RS 310"
                },
                {
                    "Activity":"Tut 0101",
                    "Class Size":"40",
                    "Day and Time":"WEDNESDAY 16:00-17:00",
                    "Instructor":"",
                    "Location":"RS 310"
                }
            ],
            "term":"2017 Winter"
        }
...
```
