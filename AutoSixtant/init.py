import os

sixtant_value = dict()
pos_sixtant = dict()
have_sixtants = set()
item_info = []

DIV2CHAOS = 180
DIV2SIXTANT = 51

sixtant_value_txt = os.path.join(os.path.dirname(__file__), 'sixtant_value.txt')
item_info_txt = os.path.join(os.path.dirname(__file__), 'item_info')
with open(item_info_txt, 'r', encoding='utf-8') as f:
    for line in f:
        item_info.append(line)

with open(sixtant_value_txt, 'r', encoding='utf-8') as f:
    for line in f:
        sixtant = line.split(':')[0].replace('\n', '')
        have_sixtants.add(sixtant)
        if not (':' in line):
            value = input(f'need to set value {line}')
            sixtant_value[sixtant] = value
            break
            continue
        value = line.split(':')[1]
        sixtant_value[sixtant] = int(value)

with open(sixtant_value_txt + '.new', 'w', encoding='utf-8') as f:
    # print(sixtant_value)
    for sixtant, value in sixtant_value.items():
        line = sixtant + ':' + value
        print(line)
        

with open(sixtant_value_txt, 'w', encoding='utf-8') as f:
    for sixtant in have_sixtants:
        f.write(sixtant)        
# with open('pos_sixtant', 'r', encoding='utf-8') as f:
#     for line in f:
#         pos = line.split(':')[0]
#         sixtant = line.split(':')[1]
#         pos_sixtant[pos] = sixtant

def cal_profits(ignore=0):
    sixtant_cost = len(item_info)
    
    print('Total cost: {:.2f}Divs, {:.2f}Chaos.'.format(nums/DIV2SIXTANT, nums/DIV2SIXTANT*DIV2CHAOS))