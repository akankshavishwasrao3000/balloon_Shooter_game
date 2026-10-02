# 🎈 Balloon Shooter Game – Queue

A simple **Balloon Shooter Game** built with **Python and Tkinter** to demonstrate the **Queue (FIFO – First In, First Out)** data structure.

The game allows users to add colorful balloons to a queue and shoot them in the same order they were added.

## 🚀 Features

* 🎈 Add colorful balloons to the queue
* 💥 Shoot balloons using FIFO order
* 🔄 Reset the game
* 🚫 Maximum queue size of 8 balloons
* 🎨 Simple graphical interface using Tkinter
* 📦 Uses Python's `deque` for efficient queue operations
* 🎲 Random balloon colors

## 🛠️ Technologies Used

* Python
* Tkinter
* `collections.deque`
* Random module

## 🧠 Data Structure Used

The project demonstrates a **Queue** using Python's `deque`.

### FIFO – First In, First Out

The first balloon added to the queue is the first balloon that gets shot.

Example:

```text
Add:     🔴 → 🟢 → 🔵 → 🟡

Shoot:   🔴
         🟢
         🔵
         🟡
```

The project uses:

```python
balloons.append((balloon, string))
```

to add balloons and:

```python
balloon, string = balloons.popleft()
```

to remove the first balloon from the queue.

## 🎮 How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd <project-folder>
```

### 3. Run the game

```bash
python balloon_game.py
```

## 🎯 How to Play

1. Click **Add Balloon 🎈** to add a balloon.
2. Balloons are added to the queue in order.
3. Click **Shoot Balloon 💥** to remove the first balloon.
4. The remaining balloons automatically move forward.
5. Click **Reset 🔁** to clear the game and start again.

## 📌 Queue Operations Demonstrated

| Operation   | Python Method     | Purpose                           |
| ----------- | ----------------- | --------------------------------- |
| Add         | `append()`        | Adds a balloon to the queue       |
| Remove      | `popleft()`       | Removes the first balloon         |
| Check Empty | `if not balloons` | Checks whether the queue is empty |
| Clear       | `clear()`         | Removes all balloons              |

## 📂 Project Structure

```text
balloon-game/
│
└── balloon_game.py
```

## 💡 Learning Objective

This project was created to understand how the **Queue data structure** works in a practical and interactive way using a simple graphical game.

It demonstrates how **FIFO (First In, First Out)** works through adding and removing balloons.

## 👩‍💻 Author

**Akanksha Vishwasrao**

