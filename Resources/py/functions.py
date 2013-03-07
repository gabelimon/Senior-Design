# A function needs to be written to take a matrix representing TEUs and boxes 
# to be removed. The last array should be the buffer zone.
# Said function needs to return a list of instructions represented as starting
# positions and ending positions.
def remove_boxes(manifest, desiredBoxPos):
    try:
        1/(1-(1*(len(desiredBoxPos)-2)))
    except:
        print "ERROR: start position invalid"
        
    rtrn = list(manifest)
    
    b_x = ord(desiredBoxPos[0])-65
    b_y = ord(desiredBoxPos[1])-49
    
    try:
        rtrn[b_x][b_y]
    except:
        print "ERROR: position out of scope"
        
    #this line below will be removed in the final code
    rtrn[b_x][b_y]="unoccupied"

    #movelist is appended with the proper steps after running A*
    #and rtrn is updated with the new manifest after the executed moves
    #---------
    #movelist = aStarFunction1(BoxPosNum)
    
    return rtrn#, "stuff"

def insert_box(manifest, label):
    pos_x = 0
    pox_y = 0

    rtrn = list(manifest)

    #perform A* to find best position for new crate
    #the position is assigned to pos_x and pos_y
    #----------
    #aStarFunction2(manifest,pos_x,pos_y)

    rtrn[pos_x][pos_y] = label
    return rtrn

def move_box(manifest, startpos,endpos):
    try:
        1/(1-(1*(len(startpos)-2)))
    except:
        print "ERROR: start position invalid"
    try:
        1/(1-(1*(len(endpos)-2)))
    except:
        print "ERROR: end position invalid"
    
    rtrn = list(manifest)
    
    s_x = ord(startpos[0])-65
    s_y = ord(startpos[1])-49
    
    e_x = ord(endpos[0])-65
    e_y = ord(endpos[1])-49

    try:
        rtrn[s_x][s_y]
    except:
        print "ERROR: start position out of scope"
    try:
        rtrn[e_x][e_y]
    except:
        print "ERROR: end position out of scope"
    
    temp = rtrn[s_x][s_y]
    rtrn[s_x][s_y] = rtrn[e_x][e_y]
    rtrn[e_x][e_y] = temp
    
    return rtrn
