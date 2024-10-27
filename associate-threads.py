import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

# Read points from the output_path file
output_path = "C:/PROGRAMMING/optimize-gridding/points.txt"

# Dictionary to store threads and their points
threads_dict = {}
current_thread = 1  # Start with thread 1
threads_dict[current_thread] = []

# Read the points from the file
points = []
with open(output_path, 'r') as f:
    for line in f:
        x, y = map(int, line.strip().split(', '))
        points.append((x, y))

# Variables for mouse interactions
dragging = False
circle_patch = None
selection_radius = 20  # Fixed circle radius for collision detection
selected_points = []  # Points selected during the drag

# Function to detect points inside the circle
def points_in_circle(center, radius, points):
    selected = []
    cx, cy = center
    for idx, (x, y) in enumerate(points):
        distance = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)
        if distance <= radius:
            selected.append((x, y, idx))  # Include index for identification
    return selected

# Event handler for mouse press
def on_mouse_press(event):
    global dragging, selected_points
    if event.button == 1:  # Left mouse button pressed
        dragging = True
        selected_points = []  # Clear current selected points

# Event handler for mouse movement during drag
def on_mouse_motion(event):
    global circle_patch, selected_points, threads_dict, current_thread
    
    if dragging and event.xdata is not None and event.ydata is not None:
        # Update circle position to follow the cursor
        if circle_patch is None:
            # Create the circle the first time we start dragging
            circle_patch = Circle((event.xdata, event.ydata), selection_radius, color='blue', fill=False, lw=2)
            ax.add_patch(circle_patch)
        else:
            # Update circle position
            circle_patch.center = (event.xdata, event.ydata)
        
        # Find points within the circle and add them to the selection
        new_selected_points = points_in_circle((event.xdata, event.ydata), selection_radius, points)

        # Avoid duplicating points in the selected list
        for point in new_selected_points:
            if point[:2] not in [p[:2] for p in selected_points]:
                selected_points.append(point)
        print(selected_points)

        # Redraw plot with highlighted selected points
        draw_plot()

# Event handler for mouse release
def on_mouse_release(event):
    global dragging, selected_points, threads_dict, current_thread, circle_patch
    if dragging:
        dragging = False

        threads_dict[current_thread] = selected_points.copy()

        # Remove the circle after selection
        if circle_patch is not None:
            circle_patch.remove()
            circle_patch = None

        # Redraw the plot to finalize the selection
        draw_plot()

# Event handler for key press (up and down arrow keys to change threads)
def on_key_press(event):
    global current_thread
    if event.key == 'up':
        current_thread += 1  # Move to next thread
        if current_thread not in threads_dict:
            threads_dict[current_thread] = []  # Create new thread if it doesn't exist
    elif event.key == 'down' and current_thread > 1:
        current_thread -= 1  # Move to previous thread
    draw_plot()

# Function to draw the plot and threads
def draw_plot():
    ax.clear()

    # Fix the axis limits to prevent resizing due to the circle
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    ax.set_title(f"Thread {current_thread} (Use UP/DOWN to switch threads)")
    
    # Plot all the points
    x_points, y_points = zip(*points)
    ax.scatter(x_points, y_points, c='gray', marker='o', label='All Points')
    
    # Draw lines between points in each thread
    for thread, thread_points in threads_dict.items():
        if thread_points:
            thread_x, thread_y = zip(*[p[:2] for p in thread_points])
            ax.plot(thread_x, thread_y, marker='o', label=f'Thread {thread}')
    
    # Highlight selected points
    if selected_points:
        selected_x, selected_y = zip(*[p[:2] for p in selected_points])
        ax.scatter(selected_x, selected_y, c='red', marker='o', label='Selected Points')

    # If the circle is being dragged, keep it visible
    if circle_patch:
        ax.add_patch(circle_patch)

    ax.set_aspect('equal', 'box')
    plt.legend()
    plt.draw()

def on_close(event):
    output_file = "C:/PROGRAMMING/optimize-gridding/selected_threads.txt"  # Output file path
    with open(output_file, 'w') as f:
        for thread, thread_points in threads_dict.items():
            f.write(f"Thread {thread}:\n")
            for point in thread_points:
                f.write(f"  {point[0]}, {point[1]}\n")
    print(f"Thread data written to {output_file}")

# Main script to display the plot
fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')

# Set fixed axis limits to avoid resizing
x_min, x_max = min(x for x, y in points)-20, max(x for x, y in points)+20
y_min, y_max = min(y for x, y in points)-20, max(y for x, y in points)+20
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Connect event handlers
fig.canvas.mpl_connect('button_press_event', on_mouse_press)
fig.canvas.mpl_connect('motion_notify_event', on_mouse_motion)
fig.canvas.mpl_connect('button_release_event', on_mouse_release)
fig.canvas.mpl_connect('key_press_event', on_key_press)
fig.canvas.mpl_connect('close_event', on_close)

# Initial plot
draw_plot()
plt.show()
