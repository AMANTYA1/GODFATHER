import asyncio
import json
import math
import re
import time
import aiofiles
import aiohttp
import urllib3
from mills.utils.logger import log

def cmd_regex_replace(cmd):
    cmd = str(cmd)
    return (
        cmd.replace("$", "")
        .replace("?(.*)", "")
        .replace("(.*)", "")
        .replace("(?: |)", "")
        .replace("| ", "")
        .replace("( |)", "")
        .replace("?((.|//)*)", "")
        .replace("?P<shortname>\\w+", "")
        .replace("(", "")
        .replace(")", "")
        .replace("?(\\d+)", "")
        .replace("|@roldexeversepybot|$", "")
        .replace("|@roldexeversepybot|", "")
        .replace(" - Admins Only", "").strip()
    )
