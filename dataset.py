import csv

def optimal_move(points):
    
    if points % 4 == 0:
        return 1
    else:
        return points % 4

def generate_dataset(filename, max_points=8):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['points', 'move'])
        for points in range(1, max_points + 1):
            move = optimal_move(points)
            writer.writerow([points, move])

generate_dataset('nim_dataset.csv')