# 🐍 Python Syntax Reference Guide: Task Manager Edition

This guide covers the fundamental Python concepts used in the **Task Manager v2.0** project.

## 1. Variables & Data Types
Variables store information. Python is "dynamically typed," meaning it figures out the data type automatically.

* **String (str):** Text wrapped in quotes.
    * `name = "Alex"`
* **Integer (int):** Whole numbers.
    * `age = 25`
* **List (list):** A collection of items in square brackets.
    * `tasks = ["Task 1", "Task 2"]`

---

## 2. Input & Output
How the program talks to the user.

* **`print()`**: Displays text to the console.
* **`input("Prompt")`**: Stops the program and waits for the user to type something. **Note:** It always returns a *String*.
* **`int()` / `str()`**: Conversion functions. Use `int()` to turn "20" into a number you can do math with.

---

## 3. String Formatting (The "f-string")
The modern way to inject variables into sentences.
* **Syntax:** `f"Text {variable} text"`
* **Example:** `print(f"Hello {name}!")`

---

## 4. List Operations
Lists are "mutable," meaning you can change them after they are created.

* **`.append(item)`**: Adds an item to the very end of the list.
* **`.pop(index)`**: Removes and returns the item at a specific position.
* **`len(list)`**: Returns the number of items in the list (the "length").
* **`.capitalize()`**: A string method that makes the first letter uppercase.

---

## 5. Control Flow (Logic)
This controls which "path" the code takes.

### If / Elif / Else
Used for making decisions.
* `if`: The first check.
* `elif`: Short for "else if"—checked only if the first `if` failed.
* `else`: The "catch-all" if nothing else matched.

### Comparison Operators
* `==` : Is equal to?
* `!=` : Is NOT equal to?
* `>=` : Greater than or equal to?
* `<`  : Less than?

---

## 6. Loops (Iteration)
Doing things over and over.

* **`while True:`**: An infinite loop. Great for menus.
* **`break`**: Immediately exits the loop.
* **`continue`**: Skips the rest of the current loop and jumps back to the start.
* **`for item in list:`**: Runs once for every item in a collection.

---

## 7. File Handling (I/O)
Saving data permanently.

* **`with open("filename", "mode") as file:`**: The safest way to handle files. It closes the file automatically.
* **Mode `"w"`**: Write mode. Overwrites the file.
* **Mode `"a"`**: Append mode. Adds to the end of the file.
* **`\n`**: The "Newline" character. Essential for keeping items on separate lines in a text file.

---

### Pro-Tip for GitHub:
Once you save this as `PYTHON_BASICS.md`, run your Git commands again:
1. `git add .`
2. `git commit -m "added syntax reference guide"`
3. `git push`
