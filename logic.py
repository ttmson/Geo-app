import math

def angle_between(p1, p2):
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    return math.atan2(dy, dx)

def infer_relationships(shapes):
    relations = []
    for i in range(len(shapes)):
        for j in range(i + 1, len(shapes)):
            a, b = shapes[i], shapes[j]
            if a['label'] == 'line' and b['label'] == 'line':
                ax1, ay1, ax2, ay2 = a['bbox']
                bx1, by1, bx2, by2 = b['bbox']
                angle_a = angle_between((ax1, ay1), (ax2, ay2))
                angle_b = angle_between((bx1, by1), (bx2, by2))
                diff = abs(angle_a - angle_b)
                if abs(diff) < 0.1:
                    relations.append((a, b, 'song song'))
                elif abs(abs(diff) - math.pi/2) < 0.1:
                    relations.append((a, b, 'vuông góc'))
    return relations
