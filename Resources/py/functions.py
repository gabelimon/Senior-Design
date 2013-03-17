import sys
sys.setrecursionlimit(10000)

vert_cost = 42
horz_cost = 6
grab_cost = 4
letg_cost = 1
stack = []
#truck position in index
t_pos = ["T",1]
#buffer position in index
b_pos = ["K",4]

class node:
    def __init__(self):
        self.parent = 0
        self.heights = []
        self.gn = 0
        self.move = [[]*2 for x in xrange(2)]

def valid_manifest(manifest):
    
    
    return True

#GL
# Next time please notify me before changing the layout. Also I feel like
# this is harder to read
#GL
# BIG CLARIFICATION. I DON'T INSERT UNOCCUPIED SPACES.
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
        #'K': []
        'K': [""]*6,
        'buffer':[]
        }
    for TEU in manifest_string.split('\n'):
        cargo = manifest[2:].strip()
        # If it's not Unoccupied insert it
        if cargo != 'Unoccupied':
            manifest[TEU[0]][int(TEU[1])] = cargo

    return manifest

def move_box(manifest, startpos, endpos):
    assert len(startpos) == 2, "The start position is invalid"
    assert len(endpos) == 2, "The end position is invalid"
    
    rtrn = list(manifest)

    s_x = ord(startpos[0])-65
    s_y = startpos[1]-1
    e_x = ord(endpos[0])-65
    e_y = endpos[1]-1

    print "SY", s_y

    assert (s_x < 10 and s_x >= 0),"Starting position out of scope"
    assert (s_y < 6 and s_y >= 0),"Starting position out of scope"
    assert (e_x < 11 and e_x >= 0),"Ending position out of scope"
    assert (e_y < 6 and e_y >= 0),"Ending position out of scope"

    temp = rtrn[s_x][s_y]
    if (e_x == 10):
        rtrn[s_x][s_y] = "Unoccupied"
        rtrn[10].append(temp)
    else:
        rtrn[s_x][s_y] = rtrn[e_x][e_y]
        rtrn[e_x][e_y] = temp
    
    return rtrn

def buff_cost(heights, x, y):
    max_h = y

    for a in xrange(x, 10):
       max_h = max(heights[a],max_h)
                         #upward lift cost        +  horizontal cost     + downward cost
    if max_h < 4: return ((4- max_h) * vert_cost) + ((13-x) * horz_cost)
    elif max_h == 4: return (2*vert_cost) + ((13-x) * horz_cost)
    else: return (2 * (max_h - 4) * vert_cost) + ((13-x) * horz_cost)
  
    

    
def get_height(manifest, column):
    top = 0;    
    while (top < 5):
        if (manifest[column][top] == "Unoccupied"):
            return top
        top = top + 1
    return top    


#STILL IN PROGRESS
#PLEASE REVIEW

#GL IMPORTANT
# Make this more readable and it'll be clear what you're missing.
# All this currently calculates is how many are on the top and not what's in
# the buffer and the REAL flaw here is that you're not adding in what it costs
# to move everything from on top of you. You'd think this would be negligible
# but the priority queue needs some way of knowing that's it's closer to the
# solution.
def h_n(manifest,y):
    #lifting TEU and moving over one    moving the crane back into position
    #(4 + 42 + 6 + 42 + 1)             + (42 + 6 + 42 + 42)
    
    count = 0

    # A more legible alternative using list splicing:
    #
    # for column_height in manifest[:-1]: #everything exept the last
    #     if column_height == 6:
    #         count += 1
    #
    # Or even better yet (using only the first ten in cast that's better):
    #
    # countInSixthRow = manifest[:10].count(6)
    for x in xrange(10):
        if manifest[x]==6:
            count+=1
    
    return 227*(y-1+count)

#should be added to h_n when calculating the h(n)
#this is also the g(n) of the goal state
def truck_cost(heights, x, y):
    max_h = y

    for a in xrange(x):
       max_h = max(heights[a],max_h)
                         #upward lift cost        +  horizontal cost     + downward cost
    if max_h < 5: return ((5- max_h) * vert_cost) + (65 +(x * horz_cost)) + (168)
    elif max_h == 5: return (2*vert_cost) + (65 +(x * horz_cost)) + (168)
    else: return (2 * (max_h - 5) * vert_cost) + (65 +(x * horz_cost)) + (168)
#        max_h = max_h-y+1
#    else 
#    heights[x]-=1
#    
#    c = 0
#    if(y==0):
#        c=-42

    #adding the cost of all movemments and grabs and releases
#    return 84*max_h+x*6+c+65

def compute_g(m, startpos, endpos):
    #assert len(startpos) == 2, "The start position is invalid"
    #assert len(endpos) == 2, "The end position is invalid"
    
    #m = list(manifest)
    #m is manifest

    #s_x = ord(startpos[0])-65
    #s_y = startpos[1]-1
    #e_x = ord(endpos[0])-65
    #e_y = endpos[1]-1

    s_x = startpos
    e_x = endpos
    if s_x == e_x: return 5000
    if m[e_x] == 6: return 5000
    if e_x == 10: return buff_cost(m, startpos, m[startpos])
    assert (s_x < 10 and s_x >= 0),"Starting position out of scope"
    #assert (s_y < 6 and s_y >= 0),"Starting position out of scope"
    assert (e_x < 11 and e_x >= 0),"Ending position out of scope"
    #assert (e_y < 6 and e_y >= 0),"Ending position out of scope"
    
    #s_top = get_height(rtrn,s_x)
    #e_top = get_height(rtrn,e_x)
    s_top = m[s_x]
    e_top = m[e_x]

    h = max(s_top,e_top)
 
    if s_x < e_x:
        for a in xrange(s_x,e_x):
            #h = max(h, get_height(m,a))
            h = max(h,m[a])
    if e_x > s_x:
        for a in xrange(e_x,s_x):
            #h = max(h, get_height(m,a))
            h = max(h,m[a])
      
    h+=1
    if e_x == 10:
        e_x = 13

    m[s_x]-=1
    m[e_x]+=1
        
    return (h-s_top)*vert_cost + abs(s_x-e_x)*horz_cost + (h-1-e_top)*vert_cost

#parent is the node being passed in which branches to the child that will be made
#position marks the column that we are moving from, equivelent to x value
#goal marks the height of the TEU we intend to move, equivelent to y value
#stack is the list of nodes that have yet to be expanded, it should always be sorted
#depth is the record of the recursion in the A_Star function
def A_Star(parent, position, goal, stack, depth):
    #increment depth 
    depth += 1

    #setup child node to point to the parent node and copy the list of heights from parent node
    child = node()
    child.parent = parent
    child.heights = parent.heights[:]

    #while the depth is no greater than 6
    if depth < 7:
        #if the goal TEU is the top TEU in the column at 'position' than set the 'gn' and 'move' to moving it to the truck, ['T',1], and return that child node
        if parent.heights[position] == goal:
            child.gn = truck_cost(child.heights,position,goal)
            child.move = [[chr(position+65),child.heights[position]],list(t_pos)]
            return child
        #if the goal is not reached, move the top TEU in the column at 'position' to each of the ten possible locations it could be moved to, including the buffer
        else:
            for x in xrange(11):
                if x != position:
                    #if x == 10, move TEU to the buffer
                    if x == 10:
                        h = h_n(child.heights, child.heights[position])
                        child.gn = compute_g(child.heights, position, 10)
                        child.move = [[chr(position+65),child.heights[position]], list(b_pos)]
                        f_n = child.gn + h
                        stack.append([child, f_n])
                    #otherwise, move TEU to the column at 'x'
                    else:
                        h = h_n(child.heights, child.heights[position])
                        child.gn = compute_g(child.heights,position, x)
                        child.move = [[chr(position+65),child.heights[position]], [chr(x + 65), child.heights[x]]]
                        f_n = child.gn + h

                    # append the new child to the stack and sort the stack based on it's f_n value
                    # pop the top off the stack and 
                    stack.append([child, f_n])
                    stack = sorted(stack, key = lambda tup: tup[1])
                    poppers = node()
                    poppers = stack.pop(0)
                    popped = poppers[0]
                    return A_Star(popped,position,goal,stack,depth)
    else:
        h = h_n(child.heights, child.heights[position])
        child.gn = 5000
        f_n = child.gn+h
        stack.append([child, f_n])
        stack = sorted(stack, key = lambda tup: tup[1])
        poppers = node()
        poppers = stack.pop(0)
        popped = poppers[0]
        return A_Star(popped,position,goal,stack,depth)
    
def remove_boxes(manifest, desiredBoxPos):
    assert len(desiredBoxPos) == 2, "The position is invalid"

    d_x = ord(desiredBoxPos[0])-65
    d_y = desiredBoxPos[1]-1
    
    rtrn = list(manifest)
    
    assert (d_x < 10) & (d_x >= 0), "Position out of scope"
    assert (d_y < 6) & (d_y >= 0), "Position out of scope"

    if (rtrn[d_x][d_y] == "unoccupied"):
        print "Position already unoccupied"
        return rtrn
    
    #this line below will be removed in the final code
    rtrn[d_x][d_y]="Unoccupied"

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



w=10
h=6
v="Unoccupied"
man = [[v]*h for x in xrange(w)]
man.append([])
man[0][0]="Bicycles"
man[0][1]="Walmart Junk"
man[1][0]="The Good Stuff"
man[0][2]="Tardis"
man[0][3]="BAMF"
for x in xrange(w+1):
    print man[x]
print '\n'

man2 = [4,1,0,0,0,0,0,0,0,0,4]

input0 = ["A",4]
input1 = ["C",1]
input2 = ["B",2]
input3 = ["B",1]


#print buff_cost(man2, 0, 5)
print man2
a = node()
a.heights = list(man2)
b = A_Star(a, 0, 3, stack, 0)
print b.heights, b.move
man2 = list(b.heights)
b = A_Star(a, 0, 2, stack, 0)
print b.heights, b.move
