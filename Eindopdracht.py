 #made by jordy seders
#The goal of this scrip is to do a health check. There is an option to import data from a csv file, an example file will be submited.
#After that the system will calculate if you are healty or not.


#imports
from ast import While
from asyncio.windows_events import NULL
import math
from pickle import TRUE
from time import sleep
import csv
from tkinter import N, W


#functions

def manual_data():
#The user choose if he wants to import from a CSV file or to manually input data. In this function there will be multiple inputs for the data and then we call the is_between function
    heart_Beat = int(input('Wat is je hartslag?\n')) 
    body_temp = float(input('Wat is je lichaamstemperatuur?\n'))
    blood_pressure = int(input('Wat is je bloed druk?\n'))
    weight_value = float(input('Hoeveel weeg je in kilogram?\n'))
    length_cm = int(input('Wat is jouw lengte in centimeters?\n'))
    lengte_m = float(length_cm/100)
    bmi_value = weight_value / math.pow(lengte_m,2)

    is_between(name=name_user, value_heart=heart_Beat, value_temp=body_temp, value_blood=blood_pressure, value_bmi=bmi_value)
    



def automatic_data():
#The user choose if he wants to import from a CSV file or to manually input data. in this function we import the CSV file, the data we store in a list. and then we use a for loop so that all items will be send to the is_between function.
    f = open ('raw_Data.csv', 'r')
    csv_data = list(csv.reader(f))

    for item in csv_data:
        name_user = str(item[0])
        heart_Beat = int(item[1])
        body_temp = float(item[2])
        blood_pressure = int(item[3])
        weight_value = float(item[4])
        length_cm = int(item[5])
        lengte_m = float(length_cm/100)
        bmi_value = weight_value / math.pow(lengte_m,2)

        is_between(name=name_user, value_heart=heart_Beat, value_temp=body_temp, value_blood=blood_pressure, value_bmi=bmi_value)
    
def is_between(name, value_heart, value_temp, value_blood, value_bmi):
#This function will determine if it is in between the health paramters. Ouput is Healty / Unhealty
    print(f'Hoi {name} Dit zijn jouw resultaten:')
    if value_heart >=55 and value_heart <= 90 and value_temp >=36.3 and value_temp <= 37.5 and value_blood >=100 and value_blood <= 140 and value_bmi >=18.5 and value_bmi <= 25:
        print(f'Hartslag: {value_heart} BPM')
        print(f'Lichaamstemperatuur: {value_temp} Graden')
        print(f'Bloedruk: {value_blood} mmHg')
        print(f'BMI: {value_bmi:.2f}')

        print ('Je bent helemaal gezond!\n')
    
    else:
        print(f'Hartslag: {value_heart} BPM')
        print(f'Lichaamstemperatuur: {value_temp} Graden')
        print(f'Bloedruk: {value_blood} mmHg')
        print(f'BMI: {value_bmi:.2f}')

        print ('Je bent niet helemaal gezond!\n')
    



#Begin of the script
print('Welkom bij de health check!')
name_user = str(input('Wat is jouw naam?\n'))
sleep(1)
print(f'Welkom! {name_user}, Het is de bedoeling dat je informatie geeft over jouw lichaam en dan zal het systeem uitrekenen of je gezond bent.')
sleep(2)


#Main loop
#We keep asking for input untill we ask for the right datatypes and the right input. 
#Aftert the input data is correct we call the functions.
#after the script ran the calculations than the system asks if you want to contiune or if you are done.
while True:
    user_choice= str(input('Zou je jouw input data van een csv bestand willen importeren? true or false\n')) 
    if user_choice == 'true':
        automatic_data()
        end_script=NULL
        end_script= input('Wil je nog meer gegevens verwerken? y/n\n')
        if end_script == 'n':
            print(f'Tot Ziens {name_user}')
            break
        else:
            continue

    elif user_choice == 'false':
        print(f'Oke {name_user}, dan gaan we handmatig de data invoeren!')
        sleep(2)
        try:
            manual_data()
            end_script=NULL
            end_script= input('Wil je nog meer gegevens verwerken? y/n')
            if end_script == 'n' or end_script == 'N':
                print(f'Tot ziens {name_user}')
                break

            else:
                continue
            
        except ValueError:
            print('Niet de gewenste input')
    else:
        print('Niet de gewenste input')
        continue









