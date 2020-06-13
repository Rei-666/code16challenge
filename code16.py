# -*- coding: UTF-8 -*-
import requests, json, fbchat, time

class Code16(fbchat.Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        time.sleep(1)
        url = json.loads(requests.get("https://api.thecatapi.com/v1/images/search").text)[0]["url"]
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        if author_id != self.uid and str(message_object.text).lower() == "koteczek":
            self.sendRemoteFiles(url, thread_id=thread_id, thread_type=thread_type)

    def onFriendRequest(self, from_id, msg):
        self.friendConnect(from_id)

koteczko_maszyna = Code16("login", "pass")
koteczko_maszyna.listen()
