# CBI_Code Repository

This repository contains the code for the Course Based in Innovation (CBI). The primary focus of this course is to develop all necessary code used to implement the sofware part of the solution of our project.

# Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Dashboard Visualization](#dashboard-visualization)
- [Acknowledgments](#acknowledgments)
- [Authors](#authors)
- [Contact](#contact)

# Project Overview
CBI is a course where multidisciplinary teams collaborate to present innovative solutions based on the Sustainable Development Goals (SDGs). In our case, Aigües de Barcelona was in charge of giving us a mission.

This code is a collaboration between some of the engineering members in two different teams.
Both teams decided to collaborate since their solutions might have a very similar software part.
The collaboration can be summarized in the following two tasks:

1. Develop the software to show though a Dashboard informations about water consumption associated to a user (p.e., Gym owner, Hotel owners, and so on). See [Dashboard Visualization](#dashboard-visualization)
2. Develop the software for a Web/App which informs clients (users) and gives then tricks, extra informations, maybe gamification and incenties. See [Web/App github repository](https://github.com/ainamartinez/CBI_Web)

## Team 2 Focus on hospitality sector
Team 2 is focusing mainly on the hospitality sector, specifically hotels. The solution is a dual approach aimed at encouraging tourists to consume less water during their stay and reducing costs while improving water savings for hotels.

To achieve this, we've thought about implementing a metering system that allows us to measure water consumption in each room. This system will help motivate guests by creating a ranking based on their water usage and providing rewards depending on their behavior.

## Team 4 Focus on gyms (to be written)

# Getting Started
If you want to download this repository you must follow this steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/CBI_Code.git
    ```
2. Navigate to the project directory:
    ```bash
    cd CBI_Code
    ```
Note that you must be able to run files that need `python3`or `SQL`.
# Dashboard Visualization
The main objective of the Dashboard Visualization is to provide detailed information about water consumption of clients, such as gym members or hotel rooms, to the respective owners like hotel chief executives, gym owners, or others who might be interested in monitoring their consumption. This visualization helps in understanding usage patterns and identifying areas for potential water savings.

To do it, we will start by using [Grafana](https://grafana.com/) and visualize an `.csv` file with data provided by `Aigües de Barcelona`and 
computed by us through a python program.

## Data Base
- ### [AB Data Challenge](./files/dades_dataChallenge.csv): 
Thanks to Aigües de Barcelona (AGBAR), we can have our first touch with a CSV file containing data about water consumption through their program ABData Challenge.

This program provides us with information about the consumption of a regular home from January 1, 2023, to October 1, 2023. It's a substantial file that gives us an idea about the consumption patterns. 

Due to the vast amount of data and in order to process it faster, we'll take first `15000 lines` to visualize information on Grafana. During the process, we've realized that it's not our type of consumption, we won't keep with this data. You might find the data visualization [here]().

- ### [Our provisional Data](./files/dataCons.csv): 
Since we depend on hardware and software construction to get our prototype's data and it's not ready yet, we've created some [Python programs](./src/dataBase_creator.py) that provide a `CSV` with data about 10 rooms. The data is based on hourly probabilities to add water consumption. It measures water usage from June 1, 2024, to June 18, 2024, and records measurements every 15 minutes to better fit our interests. You can find the data visualization depending on the aplication:
1. [For hotel rooms](https://ainamartinez.grafana.net/public-dashboards/06d7f1a2a7474070bc641f70e3ad5eb2) and it's [data in CSV](./files/dataCons_Hotel.csv) *Note that you must set data as you desire but inside the range of time between 1st June 2024 to 18th June 2024
2. [For gym users]()

- ### Our real data: 
Due to lack of time, we won't be able to implement the software to get real data from prorotypes. However, we will try to work with InfluxDB and get "real time" self-generated data so the experience is more inmersive

# Next Steps (updated 19 November)
We are already getting used to Grafana to visualize data from a CSV, but we would like to improve our knowledge about it. Since the real idea is to get real-time information and we are not sure if we will have the possibility, we will look for a way to do it (likely with InfluxDB). 

Next steps include:

1. **Design the Interface and Dashboard Visualization**: 
    - Create a user-friendly interface for the Dashboard.
    - Ensure the Dashboard provides clear and actionable insights.

2. **Improve Grafana Skills**:
    - Explore advanced features of Grafana.
    - Learn to create more complex and informative visualizations.

3. **Real-Time Data Integration**:
    - Investigate methods to achieve real-time data monitoring.
    - Implement InfluxDB for real-time data storage and retrieval.

4. **Develop the Web/App for Clients**:
    - Integrate processed data from Grafana into the app.
    - Display water consumption and position among other clients as a top saver.
    - Create an interface for gamification and progress tracking. We are thinking about hiring services from 
    - Implement a system to manage incentives. We might consideer [Factual Consulting](https://factual-consulting.com/microincentives-sustainable-mobility-europe) to manage it.
    - Provide information about the project, water-saving tips, and important updates within the app.
5. **From checkpoint presentation feedback**
    - Try to figure out the "story" from the user point of view
    - Verify reward system
    - Describe `what` data will be shown on hotel monitors
    - Think about prediction on leakage
    - Sell it to the end user

# How will both projects collaborate?

We have brainstormed new ideas to find common ground where both projects can align and offer mutual benefits:

1. **Gamification and Rewards**:
    - Gym members could earn rewards such as breakfast or dinner at participating hotels.
    - Hotel guests could access gym facilities, such as pools or saunas, if their hotel lacks these amenities. They could also use other facilities like bathrooms or drinkable water stations.
    - Maybe we should think about a new "way" gamification and implement some live "now" rewards. Something that's done at the moment. Also, consider the idea of internal competition.

2. **Web/App Integration**:
    - The Web/App will feature a map where users can find places to earn rewards, helping them understand exactly what benefits they can receive.:

        - For gym member: It's beneficial to have an accessible way to know what rewards are available nearby. For instance, gym members could easily find out if they can get a free breakfast at a nearby hotel or access to a hotel's swimming pool.
        - For Tourists: Upon checking in, tourists could receive suggestions such as:
            1. Enjoy a free breakfast on your last day.
            2. Access the gym's swimming pool with a view of the sea tomorrow morning.
            3. Get a complimentary dinner at a partner restaurant during your stay.
    - Users can invite friends to participate, enhancing the experience and increasing engagement. For example, gym members could invite (foreing) firends or family to stay at partner hotels, and hotel guests could be encouraged to use nearby gym facilities.

These initiatives aim to create a seamless experience for users, encouraging water-saving behaviors while providing tangible benefits and fostering collaboration between gyms and hotels.
# Acknowledgments

- Aigües de Barcelona for providing the data and challenge.
- Course instructors and coaches for their support and collaboration.
# Authors

- Aina Martinez [GitHub Profile](https://github.com/ainamartinez)
- Judit Lacort [GitHub Profile](https://github.com/Laacort)
- Collaborators [GitHub Profile](https://github.com/collaboratorusername)

# Contact

For any questions or feedback, please contact us at [aina.lizhuo.martinez@estudiantat.upc.edu](mailto:aina.lizhuo.martinez@estudiantat.upc.edu).