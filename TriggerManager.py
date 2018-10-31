import asyncio

from enum import Flag, auto

class TriggerOptions(Flag):
    """Option flags for a trigger"""

    STARTS = auto()
    ENDS = auto()
    ANYWHERE = STARTS | ENDS
    CASE_SENSITIVE = auto()


class Trigger:
    """
    A text trigger
    """

    # REVIEW: should optionFlags be a dict (**kwargs) ??
    def __init__(self, name, func, optionFlags = 0x0):
        self.func = func
        self.is_case_sensitive = TriggerOptions.CASE_SENSITIVE in optionFlags
        self.pos = (optionFlags & TriggerOptions.ANYWHERE) or TriggerOptions.ANYWHERE
        self.name = self.prepare_string(name)

    def prepare_string(self, str):
        """ lowers the case of `str` if the trigger is case insensitive"""

        return str if self.is_case_sensitive else str.lower()

    def is_triggered(self, message):
        """
        Determines if this trigger is triggered by the inputed `message`
        """

        message = self.prepare_string(message)
        if TriggerOptions.ANYWHERE in self.pos:
            return message.find(self.name) != -1
        elif TriggerOptions.STARTS in self.pos:
            return message[:len(self.name) - 1] == self.name
        elif TriggerOptions.ENDS in self.pos:
            return message[-len(self.name):] == self.name


class TriggerManager:
    """
    Simplifies the management of Discord bot "triggers"
    """

    def __init__(self):
        """
        Constructor
        """
        self.triggers = []

    def trigger(self, trigger = None, options = TriggerOptions(0)):
        """
        Decorator to specify that a function is a trigger word
        the trigger string for this command will be the `func` name if `trigger` is None
        """

        def decorator(func):
            name = trigger or func.__name__
            self.triggers.append(Trigger(name, func, options))

        return decorator

    async def process_triggers(self, msg):
        for t in self.triggers:
            if t.is_triggered(msg):
                # WARN: This runs each triggers (if needed) non-concurrently one after another
                # WARN: updating python to 3.7 gives the ability to create easily tasks that can run concurrent awaitables
                await t.func()