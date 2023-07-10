A telegram bot that provides users with functions:
  * communicate with ChatGPT 3.5
  * generate images from the message's text

The bot supports dialog history separated for every user, so its answers may vary depending on previous messages
A request for bot's answer may take some time(0.5 - 8 secs) depending on various factors, so its work was made fully asynchronous to avoid request queues
