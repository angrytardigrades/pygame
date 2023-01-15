import numpy as np

def map_creator():
    map = np.random.randint(1,3,(100,100),dtype=int)
    chance = 0
    for i in range (0,2):
        for j in range(map.shape[1]):
            map[i][j] = 0
    
    for i in range (map.shape[0]):
        for j in range(0,2):
            map[i][j] = 0

    for i in range (map.shape[0]-2,map.shape[0]):
        for j in range(map.shape[1]):
            map[i][j] = 0
    
    for i in range (map.shape[0]):
        for j in range(map.shape[1]-2,map.shape[1]):
            map[i][j] = 0
    
    for i in range (3,map.shape[0]-3):
        for j in range(3,map.shape[1]-3):
            if map[i][j] == 1:
                if map[i-1][j-1]==1:
                    chance +=1
                if map[i-1][j]==1:
                    chance +=1
                if map[i-1][j+1]==1:
                    chance +=1
                if map[i][j-1]==1:
                    chance +=1
                if map[i][j+1]==1:
                    chance +=1
                if map[i+1][j-1]==1:
                    chance +=1
                if map[i+1][j]==1:
                    chance +=1
                if map[i-1][j+1]==1:
                    chance +=1
                
                map[i][j] = np.random.choice(np.arange(1, 3), p=[(chance/16),1-(chance/16)])
                chance = 0
     
    
    #print(map)
    return(map)
#map_creations()