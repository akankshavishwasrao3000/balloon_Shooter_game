import tkinter as tk 
from collections import deque
import random


root = tk.Tk()
root.title("🎈 Balloon Shooter Game (Queue)")
root.geometry("700x450")
root.configure(bg="#effafb")

balloons = deque() 


canvas = tk.Canvas(root, width=680, height=300, bg="#87CEEB", highlightthickness=0)
canvas.pack(pady=20)


label = tk.Label(root, text="Click 'Add' to add balloon and 'Shoot' to remove (FIFO)",
                 font=("Arial", 12, "italic"), bg="#e0f7fa")
label.pack(pady=5)



colors = ["red", "blue", "green", "yellow", "orange", "purple", "black","pink"]


def add_balloon():
    if len(balloons) >= 8:
        label.config(text="🎈 Queue Full! Shoot some balloons first.", fg="red")
        return

    
    color = random.choice(colors)
    x = 50 + len(balloons) * 80 
    y = 150 
    balloon = canvas.create_oval(x, y, x+50, y+70, fill=color, outline="#333", width=2)
    string = canvas.create_line(x+25, y+70, x+25, y+120, fill="#555", width=3)
    balloons.append((balloon, string)) 
    label.config(text=f"🎈 Added {color} balloon!", fg="green")


def shoot_balloon():
    if not balloons:
        label.config(text="No balloons to shoot! 😅", fg="red")
        return
    balloon, string = balloons.popleft()
    canvas.delete(balloon)
    canvas.delete(string)
    realign_balloons()
    label.config(text="💥 Balloon shot!", fg="blue")


def realign_balloons():
    for i, (balloon, string) in enumerate(balloons):
        canvas.coords(balloon, 50+i*80, 150, 100+i*80, 220)
        canvas.coords(string, 50+i*80+25, 220, 50+i*80+25, 270)




frame = tk.Frame(root, bg="#e0f7fa")
frame.pack(pady=10)


add_btn = tk.Button(frame, text="Add Balloon 🎈", command=add_balloon, bg="#4CAF50", fg="white", width=15)
add_btn.grid(row=0, column=0, padx=10)



shoot_btn = tk.Button(frame, text="Shoot Balloon 💥", command=shoot_balloon, bg="#f44336", fg="white", width=15)
shoot_btn.grid(row=0, column=1, padx=10)


reset_btn = tk.Button(frame, text="Reset 🔁", command=lambda: reset_game(), bg="#2196F3", fg="white", width=15)
reset_btn.grid(row=0, column=2, padx=10)



def reset_game():
    canvas.delete("all")
    balloons.clear()  
    label.config(text="Game reset. Add balloons again!", fg="black")



root.mainloop() 
