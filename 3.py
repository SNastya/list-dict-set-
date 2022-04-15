coords1 = [(1, 10), (1, 11)]
coords2 = [(0, 20), (20, 20)]
coords3 = [(100, 91, 87), (80, 35, 70)]
coords4 = [(0, 100, 20), (0, 0, 80)]


def rasst(coords):
    if len(coords[0]) == 2:
        x,y = zip(*coords)
        return ((x[1] - x[0])**2 + (y[1] - y[0])**2)**0.5
    else:
        x,y,z = zip(*coords)
        return ((x[1] - x[0])**2 + (y[1] - y[0])**2 + (z[1] - z[0])**2)**0.5

print(rasst(coords4))