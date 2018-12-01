from telegram import Update


class UpdateInfo():

    def __init__(self, update: Update):
        self.update = update

    @property
    def bot_name(self):
        return '@pinoquioBot'

    @property
    def update_id(self):
        return self.update.update_id

    @property
    def message_id(self):
        return self.update.message.message_id

    @property
    def text(self):
        return self.update.message.text

    @property
    def chat_id(self):
        return self.update.message.chat.id

    @property
    def entities(self):
        return self.update.message.entities

    @property
    def captions(self):
        return self.update.message.caption_entities

    @property
    def hastags(self):
        return [c for c in self.entities if c.type == 'hashtag']

    @property
    def chat_type(self):
        return self.update.message.chat.type

    @property
    def is_chat_type_group(self):
        return self.chat_type == 'group'

    @property
    def is_chat_type_private(self):
        return self.chat_type == 'private'

    @property
    def bot_has_been_mentioned(self):

        for e in self.entities:
            if (e.type == 'mention'):
                if self.text[e.offset:e.offset + e.length] == self.bot_name:
                    return True

        return False

    @property
    def bot_commands(self):
        return [c for c in self.entities if c.type == 'bot_command']

    @property
    def has_commands(self):
        return len(self.bot_commands) > 0

    @property
    def bot_has_been_mentioned_in_captions(self):

        for e in self.captions:
            if (e.type == 'mention'):
                if self.text[e.offset:e.offset + e.length] == self.bot_name:
                    return True

        return False

    @property
    def is_photo(self):
        return self.text == None \
            and self.update.message.photo != None \
            and len(list(self.update.message.photo)) > 0

    def is_allowed_to_reply(self):
        return self.is_chat_type_private  \
            or (self.is_chat_type_group and self.bot_has_been_mentioned) \
            or (self.is_photo and self.is_chat_type_group) \
            or (self.is_chat_type_group and self.has_commands)

    def is_allowed_chat(self, chats: list):
        return self.chat_id in chats

    
