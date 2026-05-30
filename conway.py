# Conway's Game of Life

import random, time, copy

WIDTH = 50
HEIGHT = 100

next_cells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 1:
            column.append('#')
        else:
            column.append(' ')
    next_cells.append(column)
    
current_cells = copy.deepcopy(next_cells)
while True:
    print('\n\n\n\n\n')
    for x in range(WIDTH):
        for y in range(HEIGHT):
            print(current_cells[x][y], end='')
        print()


    
    for x in range(WIDTH):
        for y in range(HEIGHT):
                    
            left_coord = (x-1) % WIDTH
            right_coord = (x+1) % WIDTH
            above_coord = (y-1) % HEIGHT
            blow_coord = (y+1) % HEIGHT

            num_neighbors = 0

            if current_cells[left_coord][above_coord] == '#':
                num_neighbors += 1
            if current_cells[x][above_coord] == '#':
                num_neighbors += 1
            if current_cells[right_coord][above_coord] == '#':
                num_neighbors +=1
            if current_cells[left_coord][y] == '#':
                num_neighbors += 1
            if current_cells[right_coord][y] == '#':
                num_neighbors += 1
            if current_cells[left_coord][blow_coord] == '#':
                num_neighbors += 1
            if current_cells[x][blow_coord] == '#':
                num_neighbors += 1
            if current_cells[right_coord][blow_coord] == '#':
                num_neighbors += 1

            if current_cells[x][y] == '#' and (num_neighbors == 2 or num_neighbors == 3):
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' ' and num_neighbors == 3:
                next_cells[x][y] = '#'
            else:
                next_cells[x][y] = " "
    current_cells = copy.deepcopy(next_cells)
    time.sleep(1)
