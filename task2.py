# Завдання 2
# Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» за умови, 
# що користувач повинен мати можливість вказати рівень рекурсії.

# Завдання 2:
# 1. Код виконується. Програма візуалізує фрактал «сніжинка Коха».
# 2. Користувач має можливість вказати рівень рекурсії.

import turtle

def koch_curve(t, order, size):
    try:
        # Recursively draws a Koch curve.
        if order == 0:
            t.forward(size)
        else:
            for angle in [60, -120, 60, 0]:
                koch_curve(t, order - 1, size / 3)
                t.left(angle)
    except:
        print("Unexpected error")


def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")
    window.title(f"Koch ShowFlake. Order: {order}")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size / (2 * 3 ** 0.5))
    t.pendown()

    for _ in range(3):  # Draw three Koch curves to form a snowflake
        koch_curve(t, order, size)
        t.right(120)

    window.listen()  # Enables listening for key events
    turtle.mainloop()


def main(): 

    while True:
        user_input = input("Enter order (or type 'q' to quit): ").strip()
        
        if user_input.lower() == 'q':  # Allow quitting
            print("Goodbye!")
            break

        try:
            order = int(user_input)
            draw_koch_snowflake(order)
            print("Goodbye!")
            return
        except ValueError:
            print("❌ Invalid input! Please enter a valid integer or type 'q' to quit.")


if __name__ == "__main__":
    main()