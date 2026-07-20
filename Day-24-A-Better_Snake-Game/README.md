# 📅 Day 24 - File Handling & Mail Merge

## 📖 Overview

Today I learned how to work with **files in Python** by reading from and writing to text files. Using these concepts, I upgraded the **Snake Game** so it can permanently store the highest score, even after closing the game.

I also built a **Mail Merge** project that automatically creates personalized letters from a template and a list of names, removing the need to manually create multiple drafts.

---

## 🚀 Projects

### 🐍 Snake Game - High Score Tracker

**Features**
- Stores the highest score in a text file.
- Loads the high score every time the game starts.
- Updates the file automatically when a new high score is achieved.
- Keeps the high score even after the game is closed.

### 📧 Mail Merge

**Features**
- Reads a list of names from a text file.
- Reads a letter template.
- Replaces the placeholder with each recipient's name.
- Generates personalized letters automatically.
- Saves time by eliminating repetitive manual work.

---

## 🧠 Concepts Practiced

- File handling
- Reading files
- Writing files
- File modes (`r`, `w`, `a`)
- `with` statement
- String replacement
- Text file manipulation
- Data persistence
- Automation with loops

---

## ▶️ How to Run

### Snake Game

1. Navigate to the Snake Game folder.
2. Ensure the high score text file is present.
3. Run:

```bash
python main.py
```

4. Play the game and beat your previous high score.

---

### Mail Merge

1. Add names to the names text file.
2. Edit the letter template if required.
3. Run:

```bash
python main.py
```

4. The program will generate personalized letters for every name.

---

## 💻 Example

### Snake Game

```
Score: 12
High Score: 18

New High Score!

Score: 19
High Score: 19
```

### Mail Merge

**Template**

```
Dear [name],

Congratulations on your achievement!

Best Regards,
Soham
```

**Generated Letter**

```
Dear Alice,

Congratulations on your achievement!

Best Regards,
Soham
```

---

## 📚 What I Learned

- How to permanently store data using text files.
- How to read and update files safely using the `with` statement.
- How file handling makes applications more practical.
- How automation can save significant time for repetitive tasks.
- The importance of separating data, templates, and program logic.

---

## 📌 Project Status

**Status:** ✅ Completed

### Projects Completed

- 🐍 Snake Game with Persistent High Score
- 📧 Mail Merge

---

### Key Takeaway

Learning file handling made my Python programs much more useful by allowing them to save data between runs. The Mail Merge project also demonstrated how a few lines of code can automate repetitive tasks efficiently.