 #made by jordy seders
#The goal of this scrip is to do a health check. Ask inputs to the user and with the help of a function determine if it is unhealty or healty.

#dingen te doen
# Een systeem maken wanneer iemand gezond is of ongezond.
#import info van een csv file automatiseren
#modules
from ast import While
from asyncio.windows_events import NULL
import math
from pickle import TRUE
from time import sleep
import csv
from tkinter import N, W


#functions

def manual_data():
    heart_Beat = int(input('Wat is je hartslag?\n')) 
    body_temp = float(input('Wat is je lichaamstemperatuur?\n'))
    blood_pressure = int(input('Wat is je bloed druk?\n'))
    weight_value = float(input('Hoeveel weeg je in kilogram?\n'))
    length_cm = int(input('Wat is jouw lengte in centimeters?\n'))
    lengte_m = float(length_cm/100)
    bmi_value = weight_value / math.pow(lengte_m,2)

    is_between(name=name_user, value_heart=heart_Beat, value_temp=body_temp, value_blood=blood_pressure, value_bmi=bmi_value)
    



def automatic_data():
    f = open ('raw_Data.csv', 'r')
    csv_data = list(csv.reader(f))

    for item in csv_data:
        #print(item[0], item[1], item[2], item[3], item[4], item[5]) 
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
#This function will determine if it is in between the health paramters. Ouput is True / False
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
    



#Begin van het script
print('Welkom bij de health check!')
name_user = str(input('Wat is jouw naam?\n'))
sleep(1)
print(f'Welkom! {name_user}, Het is de bedoeling dat je informatie geeft over jouw lichaam en dan zal het systeem uitrekenen of je gezond bent.')
sleep(2)


#while / inputs Vars
# A while loop to ask the appropiate number. if they are all numbers there is a break to break out of the while loop.
#main loop
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
            if end_script == 'n':
                print(f'Tot ziens {name_user}')
                break

            else:
                continue
            
        except ValueError:
            print('Niet de gewenste input')
    else:
        print('Niet de gewenste input')
        continue









