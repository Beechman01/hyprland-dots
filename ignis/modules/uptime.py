import datetime

from ignis.utils import Utils
from ignis.widgets import Widget
from ignis.services.fetch import FetchService

fetch=FetchService.get_default()

def formatted_uptime() -> tuple[str, str, str, str]:
    days = int(fetch.uptime[0])
    hours = int(fetch.uptime[1])
    minutes = int(fetch.uptime[2])
    seconds = int(fetch.uptime[3])

    if days < 10:
        days_formatted = "0"+str(days)
    else:
        days_formatted = str(days)

    if hours < 10:
        hours_formatted = "0"+str(hours)
    else:
        hours_formatted = str(hours)

    if minutes < 10:
        minutes_formatted = "0"+str(minutes)
    else:
        minutes_formatted = str(minutes)

    if seconds < 10:
        seconds_formatted = "0"+str(seconds)
    else:
        seconds_formatted = str(seconds)

    return days_formatted, hours_formatted, minutes_formatted, seconds_formatted

def spacer():
    return Widget.Label(
        css_classes=["uptime"],
        label="--"
    )

def days():
    return Widget.Label(
        css_classes=["uptime"],
        label=Utils.Poll(720_000, lambda self: str(formatted_uptime()[0])).bind("output")
    )

def hours():
    return Widget.Label(
        css_classes=["uptime"],
        label=Utils.Poll(1_000, lambda self: str(formatted_uptime()[1])).bind("output")
    )

def minutes():
    return Widget.Label(
        css_classes=["uptime"],
        label=Utils.Poll(1_000, lambda self: str(formatted_uptime()[2])).bind("output")
    )

def seconds():
    return Widget.Label(
        css_classes=["uptime"],
        label=Utils.Poll(1_000, lambda self: str(formatted_uptime()[3])).bind("output")
    )

def uptime_box():
    return Widget.Box(
        vertical=True,
        css_classes=["uptime"],
        child=[
            days(),
            spacer(),
            hours(),
            spacer(),
            minutes(),
            spacer(),
            seconds(),
        ]
    )
    
