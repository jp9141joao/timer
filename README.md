# **Timer**

This is a Python project that implements a timer with configurable time options, allowing the user to set the duration and format (hours, minutes, seconds, or hundredths). The timer counts down to zero and offers the option to return to the main menu.

---

## **Features**

* **Time Configuration:** The user can set the timer duration in hours, minutes, seconds, or hundredths.
* **Countdown:** The timer counts down and clearly displays the remaining time in the terminal.
* **Menu Options:**

  * Start the timer.
  * Exit the program.

---

## **How to Use**

1. Run the program in the terminal.
2. The main menu will appear, allowing you to choose between:

   * **1** to start the timer.
   * **2** to exit the program.
3. When starting the timer:

   * Enter the desired time.
   * Choose the time unit (hours, minutes, seconds, or hundredths).
4. The timer will start counting down.
5. After the time runs out, the program will prompt you to return to the main menu.

---

## **Example Run**

When the program starts, the menu will be displayed like this:

```
* Menu *
1- Start
2- Exit
R: 
```

After choosing option 1, the program will ask for the time and unit:

```
Enter how long the timer will run: 5
This value will be in
H- Hours
M- Minutes
S- Seconds
CS- Hundredths
R: m
```

The timer will then begin counting down and be displayed as follows:

```
hh:mm:ss:m
00:01:00:9
```

The timer will continue counting down until it reaches zero.

---

## **Requirements**

* **Python 3.x:** The code was developed to work with recent Python versions.

---

## **How to Run**

1. Make sure Python 3 is installed on your system.
2. Download the source code and save it as `timer.py`.
3. Open the terminal and navigate to the directory where the file is saved.
4. Run the command:

   ```bash
   python timer.py
   ```

---

## **Notes**

* The command `os.system('cls')` is used to clear the terminal screen and works only on Windows. If you are using Linux or macOS, replace this command with `os.system('clear')` to ensure the screen clears properly.
* The program accepts numeric inputs only and validates the user’s configured time options accordingly.

---

Have fun and enjoy! 😊
