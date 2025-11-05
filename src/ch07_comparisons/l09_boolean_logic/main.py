def does_attack_hit(attack_roll, armor_class):
    case1 = attack_roll != 1 and attack_roll >= armor_class
    case2 = attack_roll == 20
    return case1 or case2