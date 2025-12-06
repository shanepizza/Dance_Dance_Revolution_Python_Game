import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()

# Instantiate the canvas item and store its ID in the variable 'box'
box = canvas.create_rectangle(50, 50, 100, 100, fill="blue")

def move_box_right():
    # Call the move method on the canvas object
    # Use the variable 'box' as the item ID
    # Move 10 pixels right (dx=10), 0 pixels down (dy=0)
    canvas.move(box, 10, 0)

# Add a button to trigger the movement
move_button = tk.Button(root, text="Move Box Right", command=move_box_right)
move_button.pack()

root.mainloop()
