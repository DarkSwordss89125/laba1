P = 3.1415
a = 42
S = P * a * a
print(round(S, 4))
point_1 = (23, 34)
x, y = point_1
centr = (0, 0)
centr_x, centr_y = centr
radius = 42
distance = 0.5 * (((x - centr_x) ** 2) + ((y - centr_y) ** 2))
inside_circle = distance <= radius
print(inside_circle)



point_1 = (30, 30)
x, y = point_1
centr = (0, 0)
centr_x, centr_y = centr
radius = 42
distance = 0.5 * (((x - centr_x) ** 2) + ((y - centr_y) ** 2))
inside_circle = radius <= distance
print(inside_circle)
 