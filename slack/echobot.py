import slack
# Import Flask
from flask import Flask
# Handles events from Slack
from slackeventsapi import SlackEventAdapter

# Configure your flask application
app = Flask(__name__)
# Configure SlackEventAdapter to handle events
slack_event_adapter = SlackEventAdapter('08c9554915735fc6c48e95bbed87265a','/slack/events',app)

# Using WebClient in slack, there are other clients built-in as well !!
client = slack.WebClient(token='xoxb-1825539444752-1802157454770-MPjvhWYFTnxUDUw2cVMS2Aau')
client.chat_postMessage(channel='#general', text='Start')

# connect the bot to the channel in Slack Channel
#client.chat_postMessage(channel='#cps-847-course', text='Send Message Demo')

# Get Bot ID
BOT_ID = client.api_call("auth.test")['user_id']

@app.route('/')
def hello():
    return 'up'

# handling Message Events
@slack_event_adapter.on('message')
def message(payload):
    print(payload)
    event = payload.get('event',{})
    user_id = event.get('user')
    text2 = event.get('text')
    if text2[-1] == '?' or ['what', 'how', 'when', 'why', 'where'].intersection(text2.lower().split()):
        if user_id != BOT_ID:
            client.chat_postMessage(channel='#general', text=text2)



# Run the webserver micro-service
if __name__ == "__main__":
    app.run(debug=True)