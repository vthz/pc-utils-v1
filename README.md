# pc-utils-v1

This Repository contains a complete package of various Computer utils which tracks various stats of your computer and
save the results for later analysis. Combine this with Task Scheduler and explore the pattern of your PC uses.

# 1. Storage Drive Usage Pattern Tracker

## Comes with two function

1. First function **records** the storage media usage whenever script is run and saves the same in csv file.
2. Second function **generates the reports** and plot the values on a **time series chart**.

## Steps to Configure

1. **Clone** the repository.
2. Make a **basic task in Task Scheduler** and pass on "Start in" param with the directory where main.py is located.(You
   want to run this code in this directory)
3. In "**script to run**" param, add absolute path of the **main.py** file.
4. Add trigger points and the execution interval(Daily, weekly).
5. Recording setup is completed.
6. Go to directory where main.py is located and open command prompt.
7. run command -> **main.py generate-report**.

## Additional

1. Comes with **typer module**. You can execute both function **directly from CLI**. Very helpful when you want your
   script to be executed with Task Scheduler.
2. CLI functions are listed here
    1. main.py record-drive-stats
    2. main.py generate-report
    3. main.py --help

Note to self: Task Schedule task name : psutils_recorddrivestats