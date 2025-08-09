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

def day():
    print(datetime.datetime.now().strftime("%d"))
    return Widget.Label(
        css_classes=["clock"],
        label=Utils.Poll(
            43200000,
            lambda self: datetime.datetime.now().strftime("%d")
        ).bind("output"),
    )

def month():
    print(datetime.datetime.now().strftime("%m"))
    return Widget.Label(
        css_classes=["clock"],
        label=Utils.Poll(
            43200000,
            lambda self: datetime.datetime.now().strftime("%m")
        ).bind("output"),
    )

def year():
    print(datetime.datetime.now().strftime("%y"))
    return Widget.Label(
        css_classes=["clock"],
        label=Utils.Poll(
            43200000,
            lambda self: datetime.datetime.now().strftime("%y")
        ).bind("output"),
    )

def spacer():
    return Widget.Label(
        css_classes=["clock"],
        label="-",
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

def date():
    return Widget.Box(
        vertical=True,
        css_classes=["clock-box"],
        halign="center",
        valign="center",
        spacing=1,
        child=[
            day(),
            spacer(),
            month(),
            spacer(),
            year(),
        ]
    )

def dateTime():
    return Widget.Box(
        vertical=False,
        css_classes=["clock"],
        halign="center",
        valign="center",
        spacing=0,
        child=[
            clock(),
            date(),
        ]
    )
