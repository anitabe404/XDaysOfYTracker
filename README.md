# XDaysOfY
## Purpose
Inspired by the 100DaysOfCode challenge, XDaysOfY is a simple CLI app that keeps track of all the important details of your challenge, so you don't have to. No more forgetting which day you're on or how many days you've missed. Just set your start date and challenge duration, and let XDaysOfY do the rest.

XDaysOfY keeps track of your:
- start date
- challenge duration
- end date
- current day
- missed days (tally)
- remaining days.

You can also manage your challenge journal in the app; create, modify and view journal entries in the app as well as export all journal entries to a txt file. XDaysOfY automatically labels your journal entry with the associated challenge day and date.

The best part is, XDaysOfY can be used for any type of challenge where you do a specific task for a specified duration. So whether it's 100DaysOfCode, 66DaysOfData, or 30DaysOfBurpees, XDaysOfY can help you stay on track.

## CLI Today, GUI Tomorrow
The current version of the app (main branch), is CLI only. However, the final version of the app will feature a GUI (made with Tkinter). Stay tuned for more details!

## Getting Started
XDaysOfY is still in development, and as such is quite rough around the edges. However, if you would like to start using it, you can do so by completing the following steps.

### Installation
To use XDaysOfY, you need to make sure you have Python 3 installed on your machine and manually download the files from the GitHub repo into a directory (you can name the directory whatever you like). Complete the following steps to download the app:
- Install Python 3 (3.9.4 for best results)
- Download the following files into a directory: 
  - challenge_tracker.py, 
  - config.json, 
  - config_manager.py,
  - day.py
  - journal_entry.py, and
  - main.py.
- Navigate to the directory that contains the files.
- Open config.json.
  - If the file contains any data, delete it.
  - If it's blank, do nothing.
- Open main.py
  - Search for `if __name__ == '__main__':`
  - Confirm that `config` variable is set to `ConfigManager('config.json')`

## Running the App
To use the app, you will need to be familiar with the Terminal. Navigate to the directory that contains the app's files and run main.py ($ `python3 main.py`). It's important that you complete **ALL** of the steps in the Installation section (above) before you run the app. Once, you've completed the installation, do the following:
- Open the Terminal and navigate to the directory that contains the app's files.
- Once there, run the following command: $ `Python3 main.py`
- If this is your first time running the app, you should be prompted to enter your challenge start date and duration.
  - **IMPORTANT NOTE:** All dates must be entered in ISO format (i.e. YYYY-MM-DD). Any other formats will cause an error. If you get a traceback, restart the app by using the `Python3 main.py` command.
  - **NOTE:** If you do not receive a prompt to enter this info, it's a sign that the config.json file contains old data. Open config.json, delete its contents and rerun `main.py`.
- Once you've successfully set your challenge start date and duration, any time you subsequently run the app, it will give you the option to display your challenge data, set a day to completed or missed, or modify a journal entry.
  - **IMPORTANT NOTE:** Once you've entered your challenge data, it gets stored in the config.json file. In order for the app to keep tracking your data, you **must not** modify the config.json file. The data in the file only needs to be deleted during the installation process. After that, it should **not** manually changed. If you modify the data in config.json, you risk corrupting the file and **permanently losing** your challenge details.

### Best Practices & Recommendations
To prevent any loss of challenge data, you can use git to track the config.json file. This way, if the file ever becomes corrupted, it can be restored to a previous version. You can do the same for exports of the journal/log txt file.