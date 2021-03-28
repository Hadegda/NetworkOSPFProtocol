import math

def CreateRingScheme():
    POINT_COUNT = 6
    points = []
    
    r = 0.2
    for p_count in range(POINT_COUNT):
        x = 0.5 + r * math.sin(2 * math.pi / POINT_COUNT * p_count)
        y = 0.5 + r * math.cos(2 * math.pi / POINT_COUNT * p_count)
        points.insert(p_count, [x,y])
    return points

def CreateStarScheme():
    POINT_COUNT = 6
    points = []
    points.insert(0, [0.5, 0.5])

    r = 0.25
    for p_count in range(1, POINT_COUNT):
        x = 0.5 + r * math.sin(2 * math.pi / (POINT_COUNT - 1) * p_count)
        y = 0.5 + r * math.cos(2 * math.pi / (POINT_COUNT - 1) * p_count)
        points.insert(p_count, [x,y])
    return points

def CreateBusScheme():
    points = []

    points.insert(0, [0.2, 0.5])
    points.insert(1, [0.4, 0.5])
    points.insert(2, [0.6, 0.5])
    points.insert(3, [0.8, 0.5])
    points.insert(4, [0.2, 0.3])
    points.insert(5, [0.4, 0.7])
    points.insert(6, [0.6, 0.3])
    points.insert(7, [0.8, 0.7])
    return points

def CreateMeshScheme():
    points = []

    points.insert(0, [0.45, 0.45])
    points.insert(1, [0.45, 0.55])
    points.insert(2, [0.55, 0.45])
    points.insert(3, [0.55, 0.55])
    return points