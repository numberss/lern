with open("D:\Code\Github Repos\\foundation-update\maps_surf.txt", encoding="utf-8") as surfMaps:
    for line in surfMaps:
        line = line.split()
        del line[0:2]
        mapName = " ".join(line)
        print(mapName)