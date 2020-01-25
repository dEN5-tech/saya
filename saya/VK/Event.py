# -*- coding: utf-8 -*-
# author: Ethosa


class Event(dict):
    def __init__(self, dict_obj):
        """создать объект dict из списка

        Arguments:
            dict_obj {dict or list} -- event from longpoll
        """
        if isinstance(dict_obj, dict):
            dict.__init__(self, dict_obj)
        else:
            if dict_obj[0] in types:
                timed = types[dict_obj[0]][:]
                self["type"] = timed[0]
                timed.pop(0)
                dict_obj.pop(0)
                length = len(dict_obj)
                for index, key in enumerate(timed):
                    if index < length:
                        self[key] = dict_obj[index]
            else:
                self["type"] = "untyped"
                self["object"] = dict_obj

types = {
    1: ["message_flags_replace", "message_id", "flags", "peer_id", "timestamp", "text", "object", "attachments", "random_id"],
    2: ["message_flags_add", "message_id", "flags", "peer_id", "timestamp", "text", "object", "attachments", "random_id"],
    3: ["message_flags_delete", "message_id", "flags", "peer_id", "timestamp", "text", "object", "attachments", "random_id"],
    4: ["message_new", "message_id", "flags", "peer_id", "timestamp", "text", "object", "attachments", "random_id"],
    5: ["message_edit", "message_id", "mask", "peer_id", "timestamp", "new_text", "attachments"],
    6: ["read_input_messages", "peer_id", "local_id"],
    7: ["read_out_messages", "peer_id", "local_id"],
    8: ["friend_online", "user_id", "extra", "timestamp"],
    9: ["friend_offline", "user_id", "flags", "timestamp"],
    10: ["dialog_flags_delete", "peer_id", "mask"],
    11: ["dialog_flags_replace", "peer_id", "flags"],
    12: ["dialog_flags_add", "peer_id", "mask"],
    13: ["delete_messages", "peer_id", "local_id"],
    14: ["restore_messages", "peer_id", "local_id"],
    51: ["chat_edt", "chat_edit", "self"],
    52: ["chat_info_edit", "type_id", "peer_id", "info"],
    61: ["user_typing_dialog", "user_id", "flags"],
    62: ["user_typing_chat", "user_id", "chat_id"],
    63: ["users_typing_chat", "user_ids", "peer_id", "total_count", "ts"],
    64: ["users_record_audio", "user_ids", "peer_id", "total_count", "ts"],
    70: ["user_was_call", "user_id", "call_id"],
    80: ["count_left", "count"],
    114: ["notification_settings_edit", "peer_id", "sound", "disable_until"]
}
