import os
import random

sixtant_value = dict()
pos_sixtant = dict()
item_info = []

DIV2CHAOS = 180
DIV2SIXTANT = 51

sixtant_value_txt = os.path.join(os.path.dirname(__file__), 'sixtant_value.txt')
item_info_txt = os.path.join(os.path.dirname(__file__), 'item_info')
with open(item_info_txt, 'r', encoding='utf-8') as f:
    for line in f:
        key = line.strip()
        item_info.append(key)
        sixtant_value[key] = -1
                
def init():
    with open(sixtant_value_txt, 'r', encoding='utf-8') as f:
        for line in f:
            sixtant = line.split(':')[0].strip()
            value = line.split(':')[1].strip()
            if value == '-1' :
                value = input(f'need to set value {line}').strip()
            sixtant_value[sixtant] = '-1'
            # sixtant_value[sixtant] = str(random.randint(3,10))

    with open(sixtant_value_txt, 'w', encoding='utf-8') as f:
        # print(sixtant_value)
        for sixtant, value in sixtant_value.items():
            line = f'{sixtant}:{value}'
            f.write(line + '\n')

def cal_profits(ignore=0):
    total_value = 0
    sixtant_chaos_cost = len(item_info) * DIV2CHAOS/DIV2SIXTANT
    compass_chaos_cost = 0
    count = 0
    for sixtant in item_info:
        value = int(sixtant_value[sixtant])
        if value < ignore:
            continue
        compass_chaos_cost = compass_chaos_cost + 1
        total_value += value
        count = count + 1
    if not count:
        print(f'No get.')
        return
    total_chaos_cost = sixtant_chaos_cost + compass_chaos_cost
    profits = (total_value - total_chaos_cost) / DIV2CHAOS
    print('Total profits: {:.2f}Divs, Per profits: {:.2f}Chaos'.format(profits, profits/count*DIV2CHAOS))
    
    
if __name__ == '__main__':
    init()
    # print(len(sixtant_value))
    # for i in range (0,20):
    #     print(f'ignore = {i}')
    #     cal_profits(ignore=i) 
    