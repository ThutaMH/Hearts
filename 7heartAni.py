import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def nested_heart_shape(t):
    x_outer = 16 * np.sin(t)**3
    y_outer = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

    # Additional hearts
    x_between_outer = 14 * np.sin(t)**3
    y_between_outer = 11.25 * np.cos(t) - 4.375 * np.cos(2*t) - 1.75 * np.cos(3*t) - 0.875 * np.cos(4*t)

    x_between_inner = 10 * np.sin(t)**3
    y_between_inner = 8.125 * np.cos(t) - 3.125 * np.cos(2*t) - 1.25 * np.cos(3*t) - 0.625 * np.cos(4*t)

    # Smaller inner hearts
    x_inner = 8 * np.sin(t)**3
    y_inner = 6.5 * np.cos(t) - 2.5 * np.cos(2*t) - np.cos(3*t) - 0.5 * np.cos(4*t)

    x_between_innermost = 6 * np.sin(t)**3
    y_between_innermost = 4.875 * np.cos(t) - 1.875 * np.cos(2*t) - 0.75 * np.cos(3*t) - 0.375 * np.cos(4*t)

    x_innermost = 4 * np.sin(t)**3
    y_innermost = 3.25 * np.cos(t) - 1.25 * np.cos(2*t) - 0.5 * np.cos(3*t) - 0.25 * np.cos(4*t)

    # Even smaller innermost heart
    x_even_smaller = 2 * np.sin(t)**3
    y_even_smaller = 1.625 * np.cos(t) - 0.625 * np.cos(2*t) - 0.25 * np.cos(3*t) - 0.125 * np.cos(4*t)

    return x_outer, y_outer, x_between_outer, y_between_outer, x_between_inner, y_between_inner, x_inner, y_inner, x_between_innermost, y_between_innermost, x_innermost, y_innermost, x_even_smaller, y_even_smaller

def update(frame, line_outer, line_between_outer, line_between_inner, line_inner, line_between_innermost, line_innermost, line_even_smaller, t_values):
    t = np.linspace(0, 2 * np.pi, 1000) * frame / 100.0
    x_outer, y_outer, x_between_outer, y_between_outer, x_between_inner, y_between_inner, x_inner, y_inner, x_between_innermost, y_between_innermost, x_innermost, y_innermost, x_even_smaller, y_even_smaller = nested_heart_shape(t)
    
    line_outer.set_xdata(x_outer)
    line_outer.set_ydata(y_outer)
    
    line_between_outer.set_xdata(x_between_outer)
    line_between_outer.set_ydata(y_between_outer)

    line_between_inner.set_xdata(x_between_inner)
    line_between_inner.set_ydata(y_between_inner)

    line_inner.set_xdata(x_inner)
    line_inner.set_ydata(y_inner)

    line_between_innermost.set_xdata(x_between_innermost)
    line_between_innermost.set_ydata(y_between_innermost)

    line_innermost.set_xdata(x_innermost)
    line_innermost.set_ydata(y_innermost)

    line_even_smaller.set_xdata(x_even_smaller)
    line_even_smaller.set_ydata(y_even_smaller)
    
    return line_outer, line_between_outer, line_between_inner, line_inner, line_between_innermost, line_innermost, line_even_smaller

def main():
    t_values = np.linspace(0, 2 * np.pi, 1000)
    x_outer_initial, y_outer_initial, x_between_outer_initial, y_between_outer_initial, x_between_inner_initial, y_between_inner_initial, x_inner_initial, y_inner_initial, x_between_innermost_initial, y_between_innermost_initial, x_innermost_initial, y_innermost_initial, x_even_smaller_initial, y_even_smaller_initial = nested_heart_shape(t_values)

    fig, ax = plt.subplots(figsize=(8, 6))
    line_outer, = ax.plot(x_outer_initial, y_outer_initial)
    line_between_outer, = ax.plot(x_between_outer_initial, y_between_outer_initial)
    line_between_inner, = ax.plot(x_between_inner_initial, y_between_inner_initial)
    line_inner, = ax.plot(x_inner_initial, y_inner_initial)
    line_between_innermost, = ax.plot(x_between_innermost_initial, y_between_innermost_initial)
    line_innermost, = ax.plot(x_innermost_initial, y_innermost_initial)
    line_even_smaller, = ax.plot(x_even_smaller_initial, y_even_smaller_initial)

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.grid(True)

    ani = FuncAnimation(fig, update, fargs=(line_outer, line_between_outer, line_between_inner, line_inner, line_between_innermost, line_innermost, line_even_smaller, t_values), frames=200, interval=50)
    plt.show()

if __name__ == "__main__":
    main()
