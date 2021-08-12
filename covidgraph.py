import requests
import plotly.express as px
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import *
import os

def master(choice, choice2):
    if choice == 'dataset1':
        graph(choice2)
    elif choice == 'dataset2':
        graph2(choice2)
def graph(Animation):
    r = requests.get("https://data.cdc.gov/resource/3apk-4u4f.json")
    thing = r.json()
    tdeaths = []
    cdeaths = []
    edates = []
    sexes = []
    ages = []
    ages2 = []
    for i in range(1, 172):
        tdeaths.append((int)(thing[i]['total_deaths']))
        cdeaths.append((int)(thing[i]['covid19_deaths']))
        edates.append(thing[i]['end_date'])
        sexes.append(thing[i]['sex'])
        ages.append((thing[i]['age_years']))
    for i in range(1, 172):
        if thing[i]['age_years'][0:2] != '<1':
            ages2.append((int)(thing[i]['age_years'][0:2]))
    ages2.append(87)
    df = pd.DataFrame({'total_deaths': tdeaths, 'covid19_deaths': cdeaths, 'end_date': edates, 
    'Death-Count': "Death Count", 'Age Years': ages, 'Age Ints': ages2, 'Sex': sexes})
    if (Animation == 'Animation On'):
        fig = px.scatter(df, x='total_deaths', y='covid19_deaths', size = 'covid19_deaths',
                hover_name='Death-Count', hover_data= ['Age Years', 'Sex', 'total_deaths', 
                'covid19_deaths'], color= 'Age Years', size_max= 210, animation_frame= 'covid19_deaths',
                range_x=[0,76000], range_y=[-1000,12000], range_color= [1,100])
    else:
        fig = px.scatter(df, x='total_deaths', y='covid19_deaths', size = 'covid19_deaths',
        hover_name='Death-Count', hover_data= ['Age Years', 'Sex', 'total_deaths', 
        'covid19_deaths'], color= 'Age Years', size_max= 210, range_x=[0,76000], 
        range_y=[-1000,12000], range_color= [1,100])
    fig.show()
def graph2(Animation):
    r = requests.get("https://data.cdc.gov/resource/hkhc-f7hg.json")
    thing = r.json()
    print(thing[1])
    sdates = []
    edates = []
    cdeaths = []
    tdeaths = []
    for i in range(1,250):
        if i > 1 and thing[i]['mmwr_week'] == thing[i-1]['mmwr_week'] and thing[i]['mmwr_week'] == thing[i+1]['mmwr_week']:
            sdates.append(thing[i]['start_date'])
            edates.append(thing[i]['end_date'])
            try: 
                cdeaths.append(thing[i]['covid_19_deaths'])
            except KeyError:
                cdeaths.append(0)
            tdeaths.append((int)(thing[i]['total_deaths']))
    df = pd.DataFrame({'total_deaths': tdeaths, 'covid19_deaths': cdeaths, 'end_date': edates, 
    'death': "US Metropolitan Covid Deaths", 'start_date': sdates})
    if (Animation == 'Animation On'):
        fig = px.scatter(df, x='total_deaths', y='covid19_deaths', size = 'total_deaths',
                hover_name='death', hover_data= ['start_date', 'end_date', 'total_deaths', 
                'covid19_deaths'], color= 'start_date', size_max=40)
    else:
        fig = px.scatter(df, x='total_deaths', y='covid19_deaths', size = 'total_deaths',
        hover_name='death', hover_data= ['start_date', 'end_date', 'total_deaths', 
        'covid19_deaths'], color= 'start_date', size_max=40)
    fig.show()
root = tk.Tk()
root.title('Covid Graph Program')
paddings = {'padx': 5, 'pady': 5}
root.tk.call("source", "sun-valley.tcl")
root.tk.call("set_theme", "light")


canvas = tk.Canvas(root, width=300, height=200, bg = 'SteelBlue3')
canvas.pack()

o_frame = ttk.LabelFrame(canvas, text="Options", padding=(30, 20))
o_frame.grid(row=0, column=0, padx=60, pady=40, sticky="nsew")

frame = ttk.Frame(o_frame)
frame.grid(column=6, row=6)

frame2 = ttk.Frame(o_frame)
frame2.grid(column=6, row=10)
options =  ['dataset1', 'dataset2']

var = StringVar(frame)
var.set(options[0])

w = tk.OptionMenu(frame, var, *options)
w.pack()

options2 =  ['Animation On', 'Animation Off']

var2 = StringVar(frame2)
var2.set(options2[1])

w2 = tk.OptionMenu(frame2, var2, *options2)
w2.pack()

graphB = ttk.Button(root, text = 'Graph', style='Accent.TButton', 
        command=lambda : master(var.get(), var2.get()))
graphB.pack()
root.mainloop()
