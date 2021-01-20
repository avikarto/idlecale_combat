from math import floor
import pandas as pd

# -----------------------------------
# ------- EDIT THIS PART ONLY -------
# -----------------------------------
# character and gear stats go here
my_stats = {
    'strstat': 57,
    'atkstat': 57,
    'defstat': 57,
    'strbonus': 28,
    'accbonus': 35,
    'attack_type': 'slash',
    'atk_speed': 2.4,
    'defbonus': {
        'stab': 129,
        'slash': 133,
        'crush': 121
    }
}

# -----------------------------------
# --------- STOP EDITS HERE ---------
# -----------------------------------

def hitcalc(attacker_stats, defender_stats, nimbleBonus=0):
    '''
    nimbleBonus is 0, or 6 if buffed with nimble (food buff)
    '''
    attackRoll = attacker_stats['atkstat'] * ( attacker_stats['accbonus'] + 64)
    def_defbonus = defender_stats['defbonus'][attacker_stats['attack_type']]
    defenseRoll = defender_stats['defstat'] * (def_defbonus + 64 + nimbleBonus)
    if attackRoll > defenseRoll:
        hit_chance = (1 - 0.5 * defenseRoll / attackRoll) * 100
    else:
        hit_chance = (0.5 * attackRoll / defenseRoll) * 100

    str = attacker_stats['strstat']
    str_bonus = attacker_stats['strbonus']
    max_hit = floor(1.3 + str/10 + str_bonus/80 + str*str_bonus/640)
    dps = (1 + max_hit) / 2 * attacker_stats['atk_speed'] * hit_chance/100

    return round(hit_chance, 2), round(dps, 2)
# def hitcalc

# -----------------------------------
# ----------- ENEMY STATS -----------
# -----------------------------------
enemy_stats = {}

black_knight = {
    'strstat': 25,
    'atkstat': 25,
    'defstat': 25,
    'strbonus': 16,
    'accbonus': 10,
    'attack_type': 'slash',
    'atk_speed': 3.0,
    'defbonus': {
        'stab': 73,
        'slash': 76,
        'crush': 70
    }
}
enemy_stats['Black Knight'] = black_knight

deadly_red_spider = {
    'strstat': 25,
    'atkstat': 30,
    'defstat': 30,
    'strbonus': 0,
    'accbonus': 10,
    'attack_type': 'slash',
    'atk_speed': 3.6,
    'defbonus': {
        'stab': 15,
        'slash': 16,
        'crush': 7
    }
}
enemy_stats['Deadly Red Spider'] = deadly_red_spider

fire_giant = {
    'strstat': 67,
    'atkstat': 77,
    'defstat': 115,
    'strbonus': 20,
    'accbonus': 25,
    'attack_type': 'slash',
    'atk_speed': 3.0,
    'defbonus': {
        'stab': 0,
        'slash': 0,
        'crush': -50
    }
}
enemy_stats['Fire Giant'] = fire_giant

ice_giant = {
    'strstat': 95,
    'atkstat': 107,
    'defstat': 128,
    'strbonus': 20,
    'accbonus': 50,
    'attack_type': 'stab',
    'atk_speed': 3.0,
    'defbonus': {
        'stab': 0,
        'slash': 0,
        'crush': -50
    }
}
enemy_stats['Ice Giant'] = ice_giant

lesser_demon = {
    'strstat': 70,
    'atkstat': 68,
    'defstat': 71,
    'strbonus': 0,
    'accbonus': 25,
    'attack_type': 'slash',
    'atk_speed': 2.4,
    'defbonus': {
        'stab': 0,
        'slash': 0,
        'crush': 0
    }
}
enemy_stats['Lesser Demon'] = lesser_demon

moss_giant = {
    'strstat': 85,
    'atkstat': 97,
    'defstat': 135,
    'strbonus': 85,
    'accbonus': 50,
    'attack_type': 'crush',
    'atk_speed': 3.6,
    'defbonus': {
        'stab': 0,
        'slash': 0,
        'crush': -50
    }
}
enemy_stats['Moss Giant'] = moss_giant

spriggan = {
    'strstat': 78,
    'atkstat': 85,
    'defstat': 110,
    'strbonus': 0,
    'accbonus': 40,
    'attack_type': 'crush',
    'atk_speed': 2.8,
    'defbonus': {
        'stab': 50,
        'slash': 50,
        'crush': 50
    }
}
enemy_stats['Spriggan'] = spriggan
# -----------------------------------
# -----------------------------------
# -----------------------------------

results = []
for enemy_name in enemy_stats:
    my_hit, my_dps = hitcalc(my_stats, enemy_stats[enemy_name])
    enemy_hit, enemy_dps = hitcalc(enemy_stats[enemy_name], my_stats)
    results.append([enemy_name, my_hit, enemy_hit, my_dps, enemy_dps])

df = pd.DataFrame(results, columns=['Enemy','Hit %','Dodge %','DPS out','DPS in'])
df.set_index('Enemy', inplace=True)
df.sort_values('DPS in', inplace=True)
print(df)
