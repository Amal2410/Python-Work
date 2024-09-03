placements={"testing":45,"python":39,"bigdata":32,"asp":32,"java":60}

# def get_value(key):

#     return placements.get(key)

# srt=sorted(placements,key=get_value,reverse=True)

# print(srt)

srt=sorted(placements,key=lambda key:placements.get(key),reverse=True)

print(srt)