# AI-Chat-BOT-With-A-GUI
An AI chat bot with a pyqt5 GUI using Tensorflow.

* Like other chatbots, this bot is also using A json file and A chat medel.
* This bot has two python files,
  1) main.py - main code
  2) train.py - to train the bot's model (chatmodel)

<b>Screenshots</b><br>
<img src="https://github.com/chenurawinrada/AI-Chat-BOT-With-A-GUI/blob/main/AIROBOTGUI/imgs/bot_sc_1.png"><br>
<img src="https://github.com/chenurawinrada/AI-Chat-BOT-With-A-GUI/blob/main/AIROBOTGUI/imgs/bot_sc_2.png"><br>

<b>Installation</b>
* Requirments (Will need only if you use .py files),
  1) Tensorflow.
  2) python3 (I'm using 3.10)
  3) pyqt5
  4) sklearn

* Clone the repository.

<b>How to use? (In windows you without python files)</b>
1) Run BOT.
  * In windows you can simply use the exe files.
  * Find the shortcut named 'BOT' in the folder named 'AIROBOTGUI'.
  * Copy & Paste it to your desktop,
  * Then double click on it. Tis will run the bot and show you a cute GUI.
2) Train bot.
  * If you want to add more commands, just open the 'intents.json' and add them in it on this order,
    1) A tag.
    2) Questions.
    3) Answers.
  * Then simply run the train.exe. It will pop up a terminal window (A cmd) and closed automatically after the model is trained.

<b>Using python files</b>
1) Run BOT.
  * In windows,
    > python main.py
  * In linux (If tensorflow works well),
    > python3 main.py
2) Train bot.
  * If you want to add more commands (Same as up above), just open the 'intents.json' and add them in it on this order,
    1) A tag.
    2) Questions.
    3) Answers.
  * Then simply run the train.py. It will pop up a terminal window (A cmd) and closed automatically after the model is trained.
    1) In windows,
      > python train.py
    2) In linux.
      > python3 train.py
