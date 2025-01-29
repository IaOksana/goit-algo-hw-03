# Завдання 3 (необов'язкове завдання). Ханойські башти
# Напишіть програму, яка виконує переміщення дисків з стрижня А на стрижень С, використовуючи стрижень В як 
# допоміжний. Диски мають різний розмір і розміщені на початковому стрижні у порядку зменшення розміру зверху 
# вниз.

# Правила:
# 1. За один крок можна перемістити тільки один диск.
# 2. Диск можна класти тільки на більший диск або на порожній стрижень.

# Вхідними даними програми має бути число n — кількість дисків на початковому стрижні. Вихідними даними — 
# логування послідовності кроків для переміщення дисків зі стрижня А на стрижень С.

# Наведемо приклад виконання коду для кількості дисків n = 3. На початковому стрижні вони розміщені так: 
# [3, 2, 1], де 3 — найбільший диск, а 1 — найменший.

# Початковий стан: {'A': [3, 2, 1], 'B': [], 'C': []}
# Перемістити диск з A на C: 1
# Проміжний стан: {'A': [3, 2], 'B': [], 'C': [1]}
# Перемістити диск з A на B: 2
# Проміжний стан: {'A': [3], 'B': [2], 'C': [1]}
# Перемістити диск з C на B: 1
# Проміжний стан: {'A': [3], 'B': [2, 1], 'C': []}
# Перемістити диск з A на C: 3
# Проміжний стан: {'A': [], 'B': [2, 1], 'C': [3]}
# Перемістити диск з B на A: 1
# Проміжний стан: {'A': [1], 'B': [2], 'C': [3]}
# Перемістити диск з B на C: 2
# Проміжний стан: {'A': [1], 'B': [], 'C': [3, 2]}
# Перемістити диск з A на C: 1
# Проміжний стан: {'A': [], 'B': [], 'C': [3, 2, 1]}
# Кінцевий стан: {'A': [], 'B': [], 'C': [3, 2, 1]}
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_triangle(vertices, ax):
    triangle = patches.Polygon(vertices, fill=False, edgecolor='black')
    ax.add_patch(triangle)

def midpoint(point1, point2):
    return [(point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2]

def sierpinski(vertices, level, ax):
    draw_triangle(vertices, ax)
    if level > 0:
        sierpinski([vertices[0], midpoint(vertices[0], vertices[1]), midpoint(vertices[0], vertices[2])], level-1, ax)
        sierpinski([vertices[1], midpoint(vertices[0], vertices[1]), midpoint(vertices[1], vertices[2])], level-1, ax)
        sierpinski([vertices[2], midpoint(vertices[2], vertices[1]), midpoint(vertices[0], vertices[2])], level-1, ax)

def main():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_axis_off()
    vertices = [[0, 0], [0.5, 0.75], [1, 0]]
    sierpinski(vertices, 3, ax)
    plt.show()

main()