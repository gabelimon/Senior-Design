def valid_manifest(manifest):
    

    return True

def format_manifest(manifest_string):
    assert valid_manifest(manifest_string)

    manifest = {
        'A': [""]*6,
        'B': [""]*6,
        'C': [""]*6,
        'D': [""]*6,
        'E': [""]*6,
        'F': [""]*6,
        'G': [""]*6,
        'H': [""]*6,
        'I': [""]*6,
        'J': [""]*6,
        'K': [""]*6,
        'buffer':[]
        }
    for TEU in manifest_string.split('\n'):
        cargo = manifest[2:].strip()
        if cargo != 'Unoccupied':
            manifest[TEU[0]][int(TEU[1])] = cargo

    return manifest

# A function needs to be written to take a matrix representing TEUs and boxes 
# to be removed. The last array should be the buffer zone.
# Said function needs to return a list of instructions represented as starting
# positions and ending positions.
def remove_box(manifest, desiredBoxPos):
    #T This block does nothing at all ever. Use assertions prolly
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
