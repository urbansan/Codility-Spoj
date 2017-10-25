#!/usr/bin/python3

import sys
def triangle_compare():
	
    num_tests = int(sys.stdin.readline().split()[0])

    for i in range(num_tests):
        
        line_in = sys.stdin.readline().split()
        x1 = int(line_in[0])
        y1 = int(line_in[1])
        x2 = int(line_in[2])
        y2 = int(line_in[3])
        x3 = int(line_in[4])
        y3 = int(line_in[5])
        
        tri1 = []
        

        tri1.append([abs(x1 - x2), abs(y1 - y2)])
        tri1.append([abs(x1 - x3), abs(y1 - y3)])
        tri1.append([abs(x2 - x3), abs(y2 - y3)])

        
        line_in = sys.stdin.readline().split()
        x1 = int(line_in[0])
        y1 = int(line_in[1])
        x2 = int(line_in[2])
        y2 = int(line_in[3])
        x3 = int(line_in[4])
        y3 = int(line_in[5])
        
        tri2 = []
        
        
        tri2.append([abs(x1 - x2), abs(y1 - y2)])
        tri2.append([abs(x1 - x3), abs(y1 - y3)])
        tri2.append([abs(x2 - x3), abs(y2 - y3)])
        
        
        for j in range(3):
            tri1[j].sort()
            tri2[j].sort()

        tri1.sort()
        tri2.sort()
        print(tri1, tri2)
        counter = 0
        for j in range(3):
            if tri1[j][0] == tri2[j][0] and tri1[j][1] == tri2[j][1]:
                print(tri1[j][0], tri2[j][0])
                print(tri1[j][1], tri2[j][1])
                counter += 1
        
        if counter == 3:
            print('TAK')
        else:
            print('NIE')
    


from math import sqrt
import random
def triangle_compare_long():
    
    how_true = 0
    how_false = 0
    # for i in range(random.randint(1, 100000)):
    for i in range(1000000):
        # print(i)
        x1 = random.randint(-5, 5)
        y1 = random.randint(-5, 5)
        x2 = random.randint(-5, 5)
        y2 = random.randint(-5, 5)
        x3 = random.randint(-5, 5)
        y3 = random.randint(-5, 5)
        first_tri = [[x1, y1], [x2, y2], [x3, y3]]
        tri1_long = []
        tri1_short = []
        
        tri1_long.append(sqrt((x1 - x2)*(x1 - x2) +  (y1 - y2)*(y1 - y2)))
        tri1_long.append(sqrt((x1 - x3)*(x1 - x3) +  (y1 - y3)*(y1 - y3)))
        tri1_long.append(sqrt((x2 - x3)*(x2 - x3) +  (y2 - y3)*(y2 - y3)))

        tri1_short.append([abs(x1 - x2), abs(y1 - y2)])
        tri1_short.append([abs(x1 - x3), abs(y1 - y3)])
        tri1_short.append([abs(x2 - x3), abs(y2 - y3)])

        
        x1 = random.randint(-5, 5)
        y1 = random.randint(-5, 5)
        x2 = random.randint(-5, 5)
        y2 = random.randint(-5, 5)
        x3 = random.randint(-5, 5)
        y3 = random.randint(-5, 5)
        second_tri = [[x1, y1], [x2, y2], [x3, y3]]
        tri2_long = []
        tri2_short = []
        
        tri2_long.append(sqrt((x1 - x2)*(x1 - x2) +  (y1 - y2)*(y1 - y2)))
        tri2_long.append(sqrt((x1 - x3)*(x1 - x3) +  (y1 - y3)*(y1 - y3)))
        tri2_long.append(sqrt((x2 - x3)*(x2 - x3) +  (y2 - y3)*(y2 - y3)))

        tri2_short.append([abs(x1 - x2), abs(y1 - y2)])
        tri2_short.append([abs(x1 - x3), abs(y1 - y3)])
        tri2_short.append([abs(x2 - x3), abs(y2 - y3)])
        
        tri1_long.sort();
        tri2_long.sort();
        
        counter = 0
        for j in range(3):
            if tri1_long[j] == tri2_long[j]:
                counter += 1
        

        if counter == 3:
            longer = True
        else:
            longer = False

        for j in range(3):
            tri1_short[j].sort()
            tri2_short[j].sort()

        tri1_short.sort()
        tri2_short.sort()

        counter = 0
        for j in range(3):
            if tri1_short[j][0] == tri2_short[j][0] and tri1_short[j][1] == tri2_short[j][1]:
                # print(tri1_short[j][0], tri2_short[j][0])
                # print(tri1_short[j][1], tri2_short[j][1])
                counter += 1
        
        if counter == 3:
            shorter = True
        else:
            shorter = False

        if (shorter is True or longer is True) and shorter != longer:
            print('shorter:', shorter, 'longer:', longer)
            print('first_tri:', first_tri, 'second_tri:', second_tri)
            print('short, tri1:', tri1_short, 'tri2:', tri2_short)
            print('long, tri1:', tri1_long, 'tri2:', tri2_long)
            how_false += 1

        if shorter is True or longer is True:
            how_true += 1
    print('True count:', how_true)
    print('False count:', how_false)
        
triangle_compare_long()

# triangle_compare()
