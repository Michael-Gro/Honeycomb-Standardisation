import matplotlib.pyplot as plt
from PIL import Image

# List to store clicked points
clicked_points = []
image_path = "C:/PROGRAMMING/optimize-gridding/onion cell aligned.jpg"
output_path = "C:/PROGRAMMING/optimize-gridding/points.txt"

# Define the event handler function for clicking
def onclick(event):
    # Check if the click was within the image bounds
    if event.xdata is not None and event.ydata is not None:
        # Append the (x, y) coordinates to the list
        clicked_points.append((int(event.xdata), int(event.ydata)))

        # Clear the plot and redraw the image
        ax.clear()
        ax.imshow(image)

        # Mark clicked points
        for point in clicked_points:
            ax.plot(point[0], point[1], 'ro')  # 'ro' = red circle

        # Update the plot
        plt.draw()

# Load the image (replace with your image path)

image = Image.open(image_path)

# Create a plot to display the image
fig, ax = plt.subplots()
ax.imshow(image)

# Connect the click event to the handler
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# Display the image and wait for user interaction
print("Click on the image to select points. Close the window when done.")

# Show the plot window and wait for user to click points
plt.show()

# After the plot window is closed, write the collected points to a file
with open(output_path, 'w') as f:
    for point in clicked_points:
        f.write(f"{point[0]}, {point[1]}\n")

print(f"Collected points written to {output_path}")
