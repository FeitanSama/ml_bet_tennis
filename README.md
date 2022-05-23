# ml_bet_tennis

## Explination of the project

The Project consists in creating an application data in the form of data storytelling with **Python** !

The Project started on 21/03/2022, and the submission date was set for on 23/05/2022.

My colleague and I chose to do your a Machine Learning predict bet for tennis pro tournament

## Tarteged training objectives

**Front-End*** :
* PRINCIPLES OF DATA EXPLORATION & ANALYSIS

**Back-End** :
* MATHEMATICS FOR DATA SCIENCE
* MACHINE LEARNING
* PYTHON FOR DATA SCIENCE

> **Note :** **Objectives** can be found in the specification directory.

## How to install and run the program ?

In order to use our program, you have to clone the repo :
```console
git clone https://github.com/FeitanSama/ml_bet_tennis.git
```

Then :
```console
pip install streamlit sklearn pymongo plotly numpy beautifulsoup4 wordcloud watchdog "pymongo[srv]" matplotlib pandas streamlit-aggrid requests
```

The database is host on Mongodb Cloud so you are already connected to it

But you can have the database in localhost :
- You must uncomment line 5 to connect to your Mongodb environment

- Moreover, to import the data to your Mongodb environment, you must run the programs in order : 

1. Launch aggregate/aggregate.py (to aggregate datas)
2. Launch preprocessing/preprocessing.py (Convert to prep csv)
3. Launch database/mongo.py (database alimentation)

Finally, you have to run this command to run the streamlit

```console
cd app/
streamlit run app.py
```

But, you can see the result of this run on the IP Address because the app data is host online. ou just have to click on this IP 

#### Host :
    Ip Address : http://217.182.70.26:180/

## Visuals
### Screenshots

#### HomePage
![image](https://user-images.githubusercontent.com/56391911/169861639-a3c73fdf-62c8-4cd5-9534-c05944ed3441.png)

#### Page Player
![image](https://user-images.githubusercontent.com/56391911/169861750-b6fa7f89-0de8-4a0f-b676-22ca7c54cbc1.png)

#### Page Player Graphs
![image](https://user-images.githubusercontent.com/56391911/169861896-91085257-cc5f-4f93-9e58-f9e2f3687cdb.png)

#### Page Player Stats
![image](https://user-images.githubusercontent.com/56391911/169862035-d025aa7f-1689-4468-8664-38666eccbb3e.png)

#### Wordcloud Player Name
![image](https://user-images.githubusercontent.com/56391911/169864353-bc516b87-9f2d-4f46-a723-5ce02f09942e.png)



