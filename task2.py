# Завдання 2
# Напишіть програму на Python, яка використовує рекурсію для створення фракталу «сніжинка Коха» за умови, 
# що користувач повинен мати можливість вказати рівень рекурсії.

# Завдання 2:
# 1. Код виконується. Програма візуалізує фрактал «сніжинка Коха».
# 2. Користувач має можливість вказати рівень рекурсії.

import turtle

def koch_curve(t, order, size):
    # Recursively draws a Koch curve.
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")
    window.title(f"Koch ShowFlake. Order: {order}")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size / (2 * 3 ** 0.5))
    t.pendown()

    try:
        for _ in range(3):  # Draw three Koch curves to form a snowflake
            koch_curve(t, order, size)
            t.right(120)
    except turtle.Terminator:  # Handle window closing
        print("Window closed during drawing.")
    except RecursionError:
        print("❌ Recursion depth exceeded! Try a lower order.")
    finally:
        return

    turtle.mainloop()


def main(): 

    while True:
        user_input = input("Enter order (or type 'q' to quit): ").strip()
        
        if user_input.lower() == 'q':  # Allow quitting
            print("Goodbye!")
            break

        try:
            order = int(user_input)
            if 0 <= order <= 5:
                draw_koch_snowflake(order)
                return
            else:
                print("❌ Order must be between 0 and 5.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid integer or type 'q' to quit.")


if __name__ == "__main__":
    main()