with open("D:\Code\Github Repos\\foundation-update\maps_surf.txt", encoding="utf-8") as maps:
    for line in maps:
        line = line.split()
        del line[0:2]
        mapName = " ".join(line)
        print(mapName)
        