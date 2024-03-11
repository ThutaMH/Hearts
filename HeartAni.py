import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def nested_heart_shape(t, frame):
    # Outer heart
    x_outer = 16 * np.sin(t)**3
    y_outer = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

    # Inner heart position
    x_center = 0
    y_center = 3 * np.sin(frame / 100.0 * 2 * np.pi)  # Varying the y-coordinate for animation

    # Inner heart
    x_inner = 8 * np.sin(t)**3 + x_center
    y_inner = 6.5 * np.cos(t) - 2.5 * np.cos(2*t) - np.cos(3*t) - 0.5 * np.cos(4*t) + y_center

    x = np.concatenate((x_outer, x_inner))
    y = np.concatenate((y_outer, y_inner))
    return x, y

def update(frame, line, t_values):
    t = np.linspace(0, 2 * np.pi, 1000)
    x, y = nested_heart_shape(t, frame)
    line.set_xdata(x)
    line.set_ydata(y)
    return line,

def main():
    t_values = np.linspace(0, 2 * np.pi, 1000)
    x_initial, y_initial = nested_heart_shape(t_values, 0)

    fig, ax = plt.subplots(figsize=(8, 6))
    line, = ax.plot(x_initial, y_initial, label='Nested Hearts')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.grid(True)

    ani = FuncAnimation(fig, update, fargs=(line, t_values), frames=200, interval=50)
    plt.show()

if __name__ == "__main__":
    main()
