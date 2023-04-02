# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 10:22:44 2023
@author: lucas
"""
quimicos = ['Actinium', 'Aluminum', 'Americium', 'Antimony', 'Argon', 'Arsenic', 'Astatine', 'Barium', 'Berkelium', 'Beryllium', 'Bismuth', 'Bohrium', 'Boron', 'Bromine', 'Cadmium', 'Calcium', 'Californium', 'Carbon', 'Cerium', 'Cesium', 'Chlorine', 'Chromium', 'Cobalt', 'Copernicium', 'Copper', 'Curium', 'Darmstadtium', 'Dubnium', 'Dysprosium', 'Einsteinium', 'Erbium', 'Europium', 'Fermium', 'Flerovium', 'Fluorine', 'Francium', 'Gadolinium', 'Gallium', 'Germanium', 'Gold', 'Hafnium', 'Hassium', 'Helium', 'Holmium', 'Hydrogen', 'Indium', 'Iodine', 'Iridium', 'Iron', 'Krypton', 'Lanthanum', 'Lawrencium', 'Lead', 'Lithium', 'Livermorium', 'Lutetium', 'Magnesium', 'Manganese', 'Meitnerium', 'Mendelevium', 'Mercury', 'Molybdenum', 'Moscovium', 'Neodymium', 'Neon', 'Neptunium', 'Nickel', 'Nihonium', 'Niobium', 'Nitrogen', 'Nobelium', 'Oganesson', 'Osmium', 'Oxygen', 'Palladium', 'Phosphorus', 'Platinum', 'Plutonium', 'Polonium', 'Potassium', 'Praseodymium', 'Promethium', 'Protactinium', 'Radium', 'Radon', 'Rhenium', 'Rhodium', 'Roentgenium', 'Rubidium', 'Ruthenium', 'Rutherfordium', 'Samarium', 'Scandium', 'Seaborgium', 'Selenium', 'Silicon', 'Silver', 'Sodium', 'Strontium', 'Sulfur', 'Tantalum', 'Technetium', 'Tellurium', 'Tennessine', 'Terbium', 'Thallium', 'Thorium', 'Thulium', 'Tin', 'Titanium', 'Tungsten', 'Uranium', 'Vanadium', 'Xenon', 'Ytterbium', 'Yttrium', 'Zinc', 'Zirconium']

def dic_quimicos(quimicos):
    total = {}
    for quimico in quimicos:
        total[quimico] = quimico[0]
    return total #Creo el diccionario con la palabra y su primer y ult letra
    
def sucesoras(quimicos, elemento):
    total = []
    for key, value in quimicos.items():
        if key == elemento:
            continue
        elif value[0].lower() == elemento[-1]:
            total.append(key)
            #Crea una lista con las palabras sucesoras
    return total

def juego(quimicos, elemento):
    total = []
    sucesora = sucesoras(quimicos, elemento)
    #quimicos.pop(quimico)
    if len(sucesora) == 0:
        return total
    else:
        quimicos.pop(elemento)
        total.append(sucesora[0])
        total += juego(quimicos, sucesora[0])
    return total
    
a = dic_quimicos(quimicos)
b = juego(a, "Lead")

