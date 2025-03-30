import datetime 
from ignis.widgets import Widget
from ignis.utils import Utils



def hour():
    return Widget.Label(
        css_classes=["clock"],
        label=Utils.Poll(
            1000,
            lambda self: datetime.datetime.now().strftime("%H")
        ).bind("output"),
    )

def minute():
    return Widget.Label(
        css_classes=["clock"],
        label=Utils.Poll(
            1000,
            lambda self: datetime.datetime.now().strftime("%M")
        ).bind("output"),
    )

def second():
    return Widget.Label(
        css_classes=["clock"],
        label=Utils.Poll(
            1000,
            lambda self: datetime.datetime.now().strftime("%S")
        ).bind("output"),
    )

def time_back():
    return Widget.Label(
        css_classes=["clock-back"],
        label="00",
    )

def spacer_back():
    return Widget.Label(
        css_classes=["clock-back"],
        label="::"
    )

def spacer():
    return Widget.Label(
        css_classes=["clock"],
        label="::",
    )

def clock():
    return Widget.Box(
        vertical=True,
        css_classes=["clock-box"],
        halign="center",
        valign="center",
        spacing=1,
        child=[
            hour(),
            spacer(),
            minute(),
            spacer(),
            second(),
        ]
    )

    
