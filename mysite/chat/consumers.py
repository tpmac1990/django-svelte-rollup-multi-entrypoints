import json
from channels.generic.websocket import WebsocketConsumer # all consumers will inherit from this
from asgiref.sync import async_to_sync

# consumers are the channels version of django views except they do more than just 
# respond to requests from the client, they can also initiate requests to the client
# all while keeping an open connection.
class ChatConsumer(WebsocketConsumer):
    """
    responsible for incoming messages from the client and broadcasting them out to anybody
    that has a connection to this consumer, all in real time. Consumers structure the code 
    into a series of functions:
    1. connect: initial request from the client
    2. receive: messages received from the client
    3. disconnect: handle what happens when a user disconnects from the consumer
    """
    def connect(self):
        """ 
        # use this to test connection
        self.accept()
        self.send(text_data=json.dumps({
            'type':'connection_established',
            'message':'you are now connected!'
        }))
        """
        # usually be a dynamic value from a url or what ever room the user joined
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name # created automatically for each user
        )

        self.accept()
   

    def receive(self, text_data):
        """
        listens for incoming messages from the client.
        channel layers allow us to create an interaction between different instances of an application for real-time communication.
        channel layers are an entirely optional part of django channels and they provide a way for multiple consumer instances to talk to each other and other parts of django.
        a channel layer provides us with groups and channels. groups are like chat rooms that store information about users in a particular room. these rooms will be stored inside of an in-memory database.
        inside of these groups we have a bunch of channels also known as users and a channel is simply a mailbox representing a user in a particular group and anybody that knows that specific channel name can
        send a message to that user via that channel.
        with channels, anytime we create a chat room we're going to have a group that represents a specific room, so anytime users join a chat room, we're going to take that user's channel and we're going to 
        add it to that group. Now when a user sends a message, this message will actually go to the group they sent it to, and because a group is simply a collection of channels and remember channels are now 
        just mailboxes that represent users, we're going to be able to broadcast that message to every single channel inside of that group. so this is how a user can send a message and that message can be 
        spread out to every single user in that group

        """
        # parse the data
        text_data_json = json.loads(text_data)
        # message held in 'message'. see lobby.html chatSocket.send(JSON.stringify({'message':message}))
        message = text_data_json['message']

        # the message needs to be broadcast to everyone who has a connection with this consumer
        # send message to everyone in the group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, # from the connect method
            {
                'type':'chat_message', # name of function to handle the event
                'message':message
            }
        )

    def chat_message(self, event):
        message = event['message'] # retrieve the sent message

        # because this message was sent to a group, every user that has a channel in this group will receive this
        # message and this will be broadcasted out in real time
        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))