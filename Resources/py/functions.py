
vert_cost = 42
horz_cost = 6
grab_cost = 4
letg_cost = 1

class node:
    def __init__(self):
        self.parent = 0
        self.start = []
        self.end = []
        self.man = []
        self.gn = 0
        self.hn = 0
        

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
        #'K': [""]*6,
        'buffer':[]
        }
    for TEU in manifest_string.split('\n'):
        cargo = manifest[2:].strip()
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

def get_height(manifest, column):
    top = 0;    
    while (top < 5):
        if (manifest[column][top] == "Unoccupied"):
            return top
        top = top + 1
    return top    

#STILL IN PROGRESS
#PLEASE REVIEW

def h_n(y):
    #lifting TEU and moving over one    moving the crane back into position
    #(4 + 42 + 6 + 42 + 1)             + (42 + 6 + 42 + 42)
    return 227*(y-1)

#should be added to h_n when calculating the h(n)
#this is also the g(n) of the goal state
def truck_cost(heights, x, y):
    max_h = max(3,y)

    for a in xrange(a,x):
       max_h = max(a,max_h)

    max_h = max_h-y+1

    c = 0
    if(y==0):
        c=-42

    #adding the cost of all movemments and grabs and releases
    return 84*max_h+x*6+c+1+4


def g_n(manifest, position):
    #set the position to two integer values
    p_x = ord(position[0])-65
    p_y = position[1]-1

    #record the height of every column of TEUs within 'height'
    height=[]
    for a in xrange(10):
        height.append(get_height(manifest,a))
        
    #set top to the hieght of the column where 'position' is located
    top = height[p_x]
    print top," ",p_y
    
    #if 'position' is the top of it's own column, remove it and be done
    if(top-1 == p_y):
        manifest[p_x][top-1]="Unoccupied"
        return manifest

    min_cost = 5000
    min_loc = 0
    max_r = 4
    
    #This loop find the cheapest location to move a TEU above 'position'
    for a in xrange(10):
        cost = 0
        temp_h = 0
        cost = abs(p_x-a)*horz_cost # add cost of horizontal movement
        
        if(a != p_x):            
            #if the location we are checking is to the left of 'position' column
            if(a < p_x):
                #find the highest column between the 'position' column and the location being checked
                for b in xrange(a,p_x):
                    temp_h = max(temp_h,height[b])
            #if the location we are checking is to the right of 'position' column
            elif(a > p_x):
                #find the highest column between the 'position' column and the location being checked
                for b in xrange(p_x,a):
                    temp_h = max(temp_h,height[b])
                    max_r = max(max_r,height[b])
                    

            #if the highest point between 'position' column and the location is
            #less than the hight of 'position' column then set the temp_h to top 
            if(temp_h < top):
                temp_h=top
            temp_h += 1
            
            print "TEMP: ",temp_h, " top: ", top, "Height[", a, "]: ", height[a]
            #add the cost of lifting and lowering the TEU
            cost += (temp_h - top)*vert_cost + (temp_h - (height[a]+1))*vert_cost
            print "COST: ",cost

            #record the location with the minimum cost
            if(cost < min_cost):
                min_cost = cost
                min_loc = a

    if(max_r < top):
        max_r = top
    max_r += 1    
    cost = (max_r-top)*vert_cost + (13-p_x)*horz_cost + (max_r-4)*vert_cost

    print "TEMP: ",max_r, " top: ", top,
    print "COST: ",cost
    
    start_pos = [chr(p_x+65), top]
    #set end position to the location with the minimum cost
    if(cost < min_cost):
        min_cost = cost
        end_pos = ["K",1]
    else:     
        end_pos = [chr(min_loc+65), height[min_loc]+1]

    print start_pos,"->",end_pos," : ",min_cost
    
    #update manifest with the single crate moved
    manifest = move_box(manifest,start_pos,end_pos)   
    
    return manifest

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

input0 = ["A",2]
input1 = ["C",1]
input2 = ["B",2]
input3 = ["A",1]

man2 = g_n(man, input0)
man2 = g_n(man, input0)
man2 = g_n(man, input0)

for x in xrange(w+1):
    print man2[x]
print '\n'
