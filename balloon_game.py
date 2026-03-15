import tkinter as tk #it is a standard library in Python for creating graphical user interfaces (GUIs).
from collections import deque
import random

# Main window
root = tk.Tk()
root.title("🎈 Balloon Shooter Game (Queue)")
root.geometry("700x450")
root.configure(bg="#effafb") #we can change settings in the window like background color, title, size etc.

# Queue to store balloons
balloons = deque() #deque is a double-ended queue which allows adding and removing elements from both ends efficiently.

# Canvas for balloons
canvas = tk.Canvas(root, width=680, height=300, bg="#87CEEB", highlightthickness=0)  #sky blue canvas #Its basically game area
canvas.pack(pady=20) #canvas use to show balloons and pady 20 means padding in y direction 

# Label for messages
label = tk.Label(root, text="Click 'Add' to add balloon and 'Shoot' to remove (FIFO)",
                 font=("Arial", 12, "italic"), bg="#e0f7fa")
label.pack(pady=5)


# Balloon colors
colors = ["red", "blue", "green", "yellow", "orange", "purple", "black","pink"]

# Function to add balloon
def add_balloon():
    if len(balloons) >= 8:
        label.config(text="🎈 Queue Full! Shoot some balloons first.", fg="red")
        return

    
    color = random.choice(colors)
    x = 50 + len(balloons) * 80  #50 is initial x position and 80 is space between balloons
    y = 150  #y position of balloon 
    balloon = canvas.create_oval(x, y, x+50, y+70, fill=color, outline="#333", width=2)
    string = canvas.create_line(x+25, y+70, x+25, y+120, fill="#555", width=3)
    balloons.append((balloon, string))   #This line adds the new balloon and its string together into the list called balloons.
    label.config(text=f"🎈 Added {color} balloon!", fg="green")

# Function to shoot balloon
def shoot_balloon(): # This function is called when the "Shoot Balloon" button is clicked.
    if not balloons:
        label.config(text="No balloons to shoot! 😅", fg="red")
        return
    balloon, string = balloons.popleft()
    canvas.delete(balloon)    #This removes both the balloon and its string from the window.
    canvas.delete(string)
    realign_balloons() #This function is called to adjust the positions of the remaining balloons after one is removed.
    label.config(text="💥 Balloon shot!", fg="blue")

# Function to realign balloons
def realign_balloons(): # This function adjusts the positions of the remaining balloons after one has been shot.
    for i, (balloon, string) in enumerate(balloons):
        canvas.coords(balloon, 50+i*80, 150, 100+i*80, 220) #coords method changes the position of the balloon and string based on its new index in the queue.
        canvas.coords(string, 50+i*80+25, 220, 50+i*80+25, 270)



#Buttons
frame = tk.Frame(root, bg="#e0f7fa") #Frame is a container to hold other widgets (like buttons) together.
frame.pack(pady=10)


add_btn = tk.Button(frame, text="Add Balloon 🎈", command=add_balloon, bg="#4CAF50", fg="white", width=15)
add_btn.grid(row=0, column=0, padx=10) #grid method places the button in a grid layout within the frame, with some padding (padx) between buttons.



shoot_btn = tk.Button(frame, text="Shoot Balloon 💥", command=shoot_balloon, bg="#f44336", fg="white", width=15)
shoot_btn.grid(row=0, column=1, padx=10)


reset_btn = tk.Button(frame, text="Reset 🔁", command=lambda: reset_game(), bg="#2196F3", fg="white", width=15)
reset_btn.grid(row=0, column=2, padx=10)


# Reset function
def reset_game():  #This function resets the whole game to start fresh.
    canvas.delete("all") #Removes all drawings (balloons, strings, etc.) from the screen.
    balloons.clear()  
    label.config(text="Game reset. Add balloons again!", fg="black")


# Run the game
root.mainloop() #root.mainloop() runs the window continuously so your program doesn’t close immediately — it keeps the GUI active and responsive.
