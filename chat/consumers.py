import json

from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

# from .models import Group, Message
# from users.models import Profile
User = get_user_model()


class GroupChatConsumer(WebsocketConsumer):

    def connect(self):
        self.group_slug = self.scope["url_route"]["kwargs"]["group_slug"]
        self.group_room = "room_%s" % self.group_slug

        async_to_sync(self.channel_layer.group_add)(
            self.group_room,
            self.channel_name
        )

        self.accept()
        self.send(text_data=json.dumps({"message": "CONNECTED!"}))

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_room,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        print(data)
        message = data["message"]
        username = data["username"]
        group_slug = data["group_slug"]
        user_id = data["user_id"]
        is_authenticated = data["is_authenticated"]

        # self.save_message(username, group_slug, message)

        async_to_sync(self.channel_layer.group_send)(
            self.group_room,
            {
                "type": "chat_message",
                "message": message,
                "username": username,
                "user_id": user_id,
                "is_authenticated": is_authenticated,
                "group_slug": group_slug
            }
        )

    def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        group_slug = event["group_slug"]
        user_id = event["user_id"]
        is_authenticated = event["is_authenticated"]

        user = User.objects.get(id=user_id)
        # profile = Profile.objects.get(user=user)

        self.send(text_data=json.dumps({
            "message": message,
            "username": username,
            "group_slug": group_slug,
            "user_id": user_id,
            # "user_image": profile.profile_pic_url,
            # "is_authenticated": is_authenticated,
        }))

    # def save_message(self, username, group_slug, message):
    #     user = User.objects.get(username=username)
    #     group = Group.objects.get(slug=group_slug)
    #
    #     Message.objects.create(sender=user, group=group, content=message)

