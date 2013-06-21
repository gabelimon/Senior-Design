import sys
sys.setrecursionlimit(100000)

unoccupied = "Unoccupied"
buff = []
char_conv = 65
const_w = 10
const_h = 5
vert_cost = 42
horz_cost = 6
grab_cost = 4
letg_cost = 1
stack = []
#truck position in index
t_pos = ["T",1]
#buffer position in index
b_pos = ["buffer",4]

class node:
    def __init__(self):
        self.parent = 0
        self.heights = []
        self.gn = 0
        self.move = [[]*2 for x in xrange(2)]

def valid_manifest(manifest):
    
    
    return True

def format_manifest(manifest_string):
    assert valid_manifest(manifest_string)
    # unnocupied is a placeholder string
    manifest = {
        'A': [unoccupied]*6,
        'B': [unoccupied]*6,
        'C': [unoccupied]*6,
        'D': [unoccupied]*6,
        'E': [unoccupied]*6,
        'F': [unoccupied]*6,
        'G': [unoccupied]*6,
        'H': [unoccupied]*6,
        'I': [unoccupied]*6,
        'J': [unoccupied]*6,
        'buffer': []#,
        #'T': []
        }
    for TEU in manifest_string.splitlines():
        cargo = TEU[2:].strip()
        if cargo != "Unoccupied":
            manifest[TEU[0]][int(TEU[1])-1] = cargo

    return manifest
    
def get_height(manifest, column):
    top = 0;    
    while (top < 5):
        if (manifest[column][top] == unoccupied):
            return top
        top = top + 1
    return top    

def h_n(manifest,y):
    #lifting TEU and moving over one 
    #(4 + 42 + 6 + 42 + 1)         
    assert y>=0, "h_n input out of scope"
    six_count = manifest.count(6)    
    return 95 * (y - 1 + six_count)

def buff_cost(heights, x, y):
    max_h = y
    for a in xrange(x, 10):
       max_h = max(heights[a],max_h)
       
               #upward & downward cost  +  horizontal cost
    if max_h < 4:
        return ((4- y) * vert_cost) + ((13-x) * horz_cost)
    elif x == 9:
        return (max_h-2)*vert_cost + ((13-x) * horz_cost)
    else:
        return (2*max_h-y)*vert_cost + ((13-x) * horz_cost)
  
#should be added to h_n when calculating the h(n)
#this is also the g(n) of the goal state
def truck_cost(heights, x, y):
    max_h = y

    for a in xrange(x):
       max_h = max(heights[a],max_h)
     #upward lift cost        +  horizontal cost     + downward cost
    if max_h < 5:
        return ((5-y)*vert_cost) + (65 +(x * horz_cost)) + (168)
    elif x == 0:
        return (max_h-3)*vert_cost + (65 +(x * horz_cost)) + (168)
    else:
        return (2*max_h - (y+1))*vert_cost + (65 +(x * horz_cost)) + (168)


def compute_g(m, startpos, endpos):
    s_x = startpos
    e_x = endpos
    assert (s_x < 10 and s_x >= 0),"Starting position out of scope"
    assert (e_x < 11 and e_x >= 0),"Ending position out of scope"
    assert (m[s_x] > 0), "Starting position is unoccupied"
    
    if s_x == e_x: return 5000
    if m[e_x] == 6: return 5000
    if e_x == 10: return buff_cost(m, startpos, m[startpos])
    
    s_top = m[s_x]
    e_top = m[e_x]

    h = max(m[s_x],m[e_x])
 
    if s_x < e_x:
        for a in xrange(s_x,e_x):
            h = max(h,m[a])
    if e_x > s_x:
        for a in xrange(e_x,s_x):
            h = max(h,m[a])
      
    h+=1
    if e_x == 10:
        e_x = 13

        
    return (h-s_top)*vert_cost + abs(s_x-e_x)*horz_cost + (h-1-e_top)*vert_cost

#parent is the node being passed in which branches to the child that will be made
#position marks the column that we are moving from, equivelent to x value
#goal marks the height of the TEU we intend to move, equivelent to y value
#stack is the list of nodes that have yet to be expanded, it should always be sorted
def A_Star(parent, position, goal, stack):
    #setup child node to point to the parent node and copy the list of heights from parent node
    child = node()
    child.parent = parent
    child.heights = parent.heights[:]
    child.gn = parent.gn

    #a temporary value for child.heights so that child.heights can be reverted for every new movement
    h_temp = child.heights[:]
    
    #if the goal TEU is the top TEU in the column at 'position' than set the 'gn' and 'move' to moving it to the truck, ['T',1], and return that child node
   
    if parent.heights[position] == goal:    
        child.gn = truck_cost(child.heights,position,goal)
        child.move = [[chr(position+char_conv),child.heights[position]],list(t_pos)]
        child.heights[position] -= 1
        return child
        #if the goal is not reached, move the top TEU in the column at 'position' to each of the ten possible locations it could be moved to, including the buffer
    else:
        for x in xrange(11):
            if x != position:
                h = h_n(child.heights, child.heights[position])
                
                #if x == 10, move TEU to the buffer
                if x == 10:
                    child.move = [[chr(position+char_conv),child.heights[position]], list(b_pos)]
                #otherwise, move TEU to the column at 'x'
                else:
                    child.move = [[chr(position+char_conv),child.heights[position]], [chr(x + char_conv), child.heights[x]+1]]

                gn_to_add = compute_g(child.heights,position, x)
                child.heights[position] -=1
                child.heights[x] += 1
                # append the new child to the stack
                # use stack_child so as not to overwrite child in the for loop
                stack_child = node()
                stack_child.parent = child.parent
                stack_child.heights = child.heights[:]
                stack_child.gn = child.gn + gn_to_add
                stack_child.move = child.move[:]
                f_n = stack_child.gn + h
                stack.append([stack_child, f_n])
                child.heights = h_temp[:]
        #sort the stack based on it's f_n value
        # and pop the top off the stack
        stack = sorted(stack, key = lambda tup: tup[1])
        poppers = node()
        poppers = stack.pop(0)
        popped = poppers[0]
        return A_Star(popped,position,goal,stack)

def list_moves(child):
    if child.parent == 0: 
        thing =[]
        thing.append(list(child.move))
        thing.pop()
        return thing
    else:
        thing = list_moves(child.parent) 
        thing.append(list(child.move))
        return thing
    
def manifest_to_heights(manifest):
    h = []
    for x in manifest:
        if manifest[x]:
            for y in xrange(len(manifest[x])):
                 if manifest[x][y] == unoccupied:
                     h.append(y)
                     break 
    h.append(0)
    return h
    

def remove_box(manifest, TEU_to_pull):
    s_x = ord(TEU_to_pull[0])-65   
    s_y = TEU_to_pull[1]
    manifest_heights = manifest_to_heights(manifest)
    problem = node()
    problem.heights = list(manifest_heights)
    solution = A_Star(problem, s_x, s_y, stack)
    list_of_moves = list_moves(solution)
    cost = 0
    ran = solution.heights[10]
    for x in xrange (ran):
        best = 5000
        z = 11
        for y in xrange(10):
            cost = buff_cost(solution.heights, y, solution.heights[y])
            if cost < best:
                best = cost
                z = y
        solution.heights[z] += 1
        solution.heights[10] -= 1
        move_to_add = [list(b_pos), [chr(z+char_conv),solution.heights[z]]]
        list_of_moves.append(move_to_add)
    for x in xrange(10):
        if solution.heights[x] > 5:
            best = 5000
            z = 11
            for y in range(10):
                if solution.heights[y] < 5:
                    cost = compute_g(solution.heights, x, y)
                    if best > cost: 
                        best = cost
                        z = y
         
            move_to_add = [[chr(x+char_conv),solution.heights[x]], [chr(z + char_conv), solution.heights[z]+1]]
            solution.heights[z] += 1
            solution.heights[x] -= 1
            list_of_moves.append(move_to_add)
      
      
    return list_of_moves

#Pass in a manifest dictionary
#a startpos, which is a letter representing the column
#and an endtpos, which is a letter representing the column
def move_box(manifest, startpos, endpos):
    assert startpos != endpos, "The start and end positions are identical"
    rtrn = manifest

    s_x = startpos
    e_x = endpos
    s_y = 0
    e_y = 0

    if(s_x != 'buffer'):    
        s_y = get_height(manifest,startpos)
        if(manifest[s_x][s_y] == unoccupied):
            s_y -= 1
    
    if(e_x == 'T'):
        rtrn[s_x][s_y]=unoccupied
        return rtrn
     
    if(e_x != 'buffer'):
        e_y = get_height(manifest,endpos)

    if (s_x == 'buffer'):
        rtrn[e_x][e_y] = rtrn[s_x].pop();
    elif (e_x == 'buffer'):
        temp = rtrn[s_x][s_y]
        rtrn[s_x][s_y] = unoccupied
        rtrn[e_x].append(temp)
    else:
        temp = rtrn[s_x][s_y]
        rtrn[s_x][s_y] = rtrn[e_x][e_y]
        rtrn[e_x][e_y] = temp
    
    return rtrn


def insert_box(manifest):
    pos_x = -1
    pos_y = -1
    
    for x in xrange(10):
        for y in xrange(6):
            if(manifest[chr(x+65)][y+1] == unoccupied):
                pos_x = chr(x+65)
                pos_y = y+1
                break
        if(pos_x > -1):
            break

    assert pos_x > -1, "No free space on ship to add TEU"
    rtrn = [pos_x,pos_y]
    return rtrn
