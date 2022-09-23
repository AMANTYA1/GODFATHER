from io import BytesIO
import os
import re
import sys
import inspect

from pathlib import Path
from asyncio import sleep
from time import gmtime, strftime
from traceback import format_exc

from telethon.tl.types import InputWebDocument
from telethon import Button, __version__ as tv
from telethon.events import NewMessage
from telethon import events
from telethon.utils import get_display_name
from telethon.tl.types import Message
from telethon.errors.common import *
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.errors.rpcerrorlist import AuthKeyDuplicatedError
from telethon.events import CallbackQuery, InlineQuery, NewMessage


from TGN import HANDLERS
from TGN.services.telethon import tbot as client
from TGN.plugins.checkers.utils.tool import cmd_regex_replace



def bot_cmd(pattern=None, *args, **kwargs):
    cmd_name = kwargs.get("cmd", False) or kwargs.get("cmds", False)
    groups_only = kwargs.get("groups_only", False)
    gadmins_only = kwargs.get("gadmins_only", False)
    perm = kwargs.get("perm", False)
    admins_only = kwargs.get("admins_only", False)
    private_only = kwargs.get("private_only", False)
    text_only = kwargs.get("text_only", False)
    funcc = kwargs.get("func", lambda e: not e.via_bot_id)
    re_pattern = r"^[{}]".format(''.join(HANDLERS)) or "/"
    if not pattern and not cmd_name:
        log.critical("no pattern or cmds are found.")
        sys.exit(1)
    if cmd_name and not pattern:
        cmd = r"{}( (.*)|@{}|$)".format(cmd_name , client.me.username)
    else:
        if pattern.endswith("$"):
            cmd = pattern[:-1] + r"(|@{}|$)".format(client.me.username)
        else:
            cmd = cmd_name
