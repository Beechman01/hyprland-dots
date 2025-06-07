from pynput import keyboard
from threading import Thread

from ignis.app import IgnisApp
from ignis.utils import Utils, socket
from ignis.widgets import Widget

from modules import workspaces
from modules import volume
from modules import uptime
from modules import system_tray
from modules import clock
from modules import monitoring
from modules.keybinds import Keybinds

from ignis.services.hyprland import HyprlandService, HyprlandWorkspace

app = IgnisApp.get_default()
app.apply_css(f"{Utils.get_current_dir()}/style.scss")

hyprland = HyprlandService.get_default()

workspaces=workspaces.Workspaces()
volume=volume.volume_box()
uptime=uptime.uptime_box()
sys_tray=system_tray.tray()
clock=clock.clock()
cpu=monitoring.cpu()
gpu=monitoring.gpu()


# Layout boxes
def top_box():
    return Widget.Box(
        vertical=True,
        valign="start",
        halign="center",
        homogeneous=False,
        spacing=5,
        child=[
            workspaces,
        ],
    )

def center_box():
    return Widget.Box(
        vertical=True,
        valign="center",
        halign="center",
        homogeneous=False,
        spacing=5,
        child=[
            cpu,
            Widget.Separator(vertical=True),
            clock,
            Widget.Separator(vertical=True),
            gpu
        ],
    )

def bottom_box():
    return Widget.Box(
        vertical=True,
        valign="end",
        halign="center",
        homogeneous=False,
        spacing=5,
        child=[
            uptime,
            volume,
            sys_tray,
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

def keys_box():
    return Widget.Box(
        vertical=False,
        css_classes=["bar"],
        halign="center",
        child=[
            Keybinds,
        ]
    )
def keys(monitor: int):
    return Widget.Window(
        namespace="Key-Binds",
        monitor= monitor,
        width_request=500,
        height_request=100,
        exclusivity="ignore",
        anchor=["bottom"],
        layer="top",
        visible=False,
        child=keys_box()
    )


bar(1)
keys(2)





