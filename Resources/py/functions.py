def valid_manifest(manifest):
    
<<<<<<< HEAD
    
=======

>>>>>>> b59158fc1d86ffb23b76ecd0cd798711c29cb996
    return True

def format_manifest(manifest_string):
    assert valid_manifest(manifest_string)
<<<<<<< HEAD
    
=======

>>>>>>> b59158fc1d86ffb23b76ecd0cd798711c29cb996
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

<<<<<<< HEAD
def choose_TEU(manifest, pos):
    
    return 0

def remove_boxes(manifest, desiredBoxPos):
    assert len(desiredBoxPos) == 2, "The position is invalid"

    d_x = ord(desiredBoxPos[0])-65
    d_y = desiredBoxPos[1]-1
    
=======
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
        
>>>>>>> b59158fc1d86ffb23b76ecd0cd798711c29cb996
    rtrn = list(manifest)
    
    assert (d_x < 10) & (d_x >= 0), "Position out of scope"
    assert (d_y < 6) & (d_y >= 0), "Position out of scope"

    if (rtrn[d_x][d_y] == "unoccupied"):
        print "Position unoccupied"
        return rtrn
    
    #this line below will be removed in the final code
    rtrn[d_x][d_y]="unoccupied"

    #movelist is appended with the proper steps after running A*
    #and rtrn is updated with the new manifest after the executed moves
    #---------
    #movelist = aStarFunction1(BoxPosNum)
    
    return rtrn#, "stuff"


def insert_box(manifest, label):
    pos_x = 0
    pos_y = 0

    rtrn = list(manifest)
    
    assert len(label) > 5, "The TEU label has too few characters"
    
    #perform A* to find best position for new crate
    #the position is assigned to pos_x and pos_y
    #----------
    #aStarFunction2(manifest,pos_x,pos_y)

    rtrn[pos_x][pos_y] = label
    return rtrn

def move_box(manifest, startpos, endpos):
    assert len(startpos) == 2, "The start position is invalid"
    assert len(endpos) == 2, "The end position is invalid"
    
    rtrn = list(manifest)

    s_x = ord(startpos[0])-65
    s_y = startpos[1]-1
    e_x = ord(endpos[0])-65
    e_y = endpos[1]-1

    assert (s_x < 10 and s_x >= 0),"Starting position out of scope"
    assert (s_y < 6 and s_y >= 0),"Starting position out of scope"
    assert (e_x < 10 and e_x >= 0),"Ending position out of scope"
    assert (e_y < 6 and e_y >= 0),"Ending position out of scope"

    temp = rtrn[s_x][s_y]
    rtrn[s_x][s_y] = rtrn[e_x][e_y]
    rtrn[e_x][e_y] = temp
    
    return rtrn


#This is just the body of the code to test individual functions:
w=10
h=6
v="unoccupied"
man = [[v]*h for x in xrange(w)]
man[0][0]="Bycicles"
man[0][1]="Walmart Junk"
man[1][0]="The Good Stuff"

for x in xrange(w):
    print man[x]
print '\n'

input0 = ["A",2]
input1 = ["C",1]
input2 = ["B",1]

man2 = move_box(man,input0,input1)

for x in xrange(w):
    print man2[x]
print '\n'

removelist = [input2]

man2 = remove_boxes(man,input2)

for x in xrange(w):
    print man2[x]
print '\n'


man2 = insert_box(man,"poop-poop")

for x in xrange(w):
    print man2[x]
print '\n'
