
from ignis.app import IgnisApp
from ignis.utils import Utils
from ignis.widgets import Widget

from modules import workspaces
from modules import volume
from modules import uptime
from modules import system_tray
from modules import clock
from modules import monitoring

app = IgnisApp.get_default()
app.apply_css(f"{Utils.get_current_dir()}/style.scss")

workspaces=workspaces.Workspaces()
volume=volume.volume_box()
uptime=uptime.uptime_box()
sys_tray=system_tray.tray()
clock=clock.dateTime()
cpu=monitoring.cpu()
gpu=monitoring.gpu()


# Layout boxes
def top_box():
    return Widget.Box(
        css_classes=["top_box"],
        vertical=True,
        valign="start",
        halign="center",
        homogeneous=False,
        spacing=5,
        child=[
            Widget.Separator(
                vertical=True,
                css_classes=['spacer']
            ),
            workspaces,
        ],
    )

def center_box():
    return Widget.Box(
        css_classes=["center_box"],
        vertical=True,
        valign="center",
        halign="center",
        homogeneous=False,
        spacing=5,
        child=[
            cpu,
            Widget.Separator(
                vertical=True
            ),
            clock,
            Widget.Separator(
                vertical=True
            ),
            gpu
        ],
    )

def bottom_box():
    return Widget.Box(
        css_classes=["bottom_box"],
        vertical=True,
        valign="end",
        halign="center",
        homogeneous=False,
        spacing=5,
        child=[
            uptime,
            sys_tray,
            volume,
            Widget.Separator(
                vertical=True,
                css_classes=['spacer']
            ),
        ],
    )

def hyprbar():
    return Widget.CenterBox(
        vertical=True,
        css_classes=["bar"],
        halign="center",
        start_widget=top_box(),
        center_widget=center_box(),
        end_widget=bottom_box(),
    )

def bar(monitor: int) -> Widget.Window:
    return Widget.Window(
        namespace=f"Hypr-bar-{monitor}",
        monitor=monitor,
        width_request=20,
        height_request=2555,
        exclusivity="exclusive",
        anchor=["left"],
        layer="top",
        child=hyprbar(),
    )



bar(1)





