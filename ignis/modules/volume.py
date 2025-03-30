
# import alsaaudio
from ignis.utils import Utils
from ignis.widgets import Widget
from ignis.services.audio import AudioService

audio = AudioService.get_default()

# Volume functions
# def volume():
    # am = alsaaudio.Mixer()
    # current_volume = am.getvolume()
    # return current_volume[1]


def volume_label():
    return Widget.Label(
        css_classes=["volume"],
        label=audio.speaker.bind("volume", transform=lambda value: str(value)+"%"),
    )


def volume_scale():
    return Widget.Scale(
        css_classes=["volume"],
        min=0,
        max=100,
        vertical=True,
        valign="end",
        value=audio.speaker.bind("volume"),
        draw_value=False,
        value_pos="bottom",
        inverted=True,
    )

def volume_box():
    return Widget.Box(
        vertical=True,
        css_classes=["volume-box"],
        spacing=0,
        child=[
            volume_scale(),
            volume_label(),
        ]
    )
