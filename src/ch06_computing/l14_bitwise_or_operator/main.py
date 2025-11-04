def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    return glorfindel | galadriel | elendil | elrond

print(calculate_guild_perms(0b0001, 0b0010, 0b0100, 0b1000))