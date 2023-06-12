import os

sixtant_value = dict()
pos_sixtant = dict()

with open('sixtant_value', 'r', encoding='utf-8') as f:
    for line in f:
        sixtant = line.split(':')[0]
        value = line.split(':')[1]
        sixtant_value[sixtant] = int(value)
        
with open('pos_sixtant', 'r', encoding='utf-8') as f:
    for line in f:
        pos = line.split(':')[0]
        sixtant = line.split(':')[1]
        pos_sixtant[pos] = sixtant