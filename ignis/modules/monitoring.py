import sys
import psutil
from pynvml import *

from ignis.widgets import Widget
from ignis.utils import Utils


def getCpuPercent():
    cpu = psutil.cpu_percent()

    # print(int(cpu))
    return cpu

def getRamPercent():
    ram = psutil.virtual_memory()

    # print(int(ram.percent))
    return ram.percent

def getCpuTemp():
    sensor = psutil.sensors_temperatures()
    temp = sensor["k10temp"][0][1]

    # print(int(temp))
    return str(int(temp))

def cpuUsageScale():
    return Widget.Scale(
        css_classes=["monitoring"],
        min=0,
        max=100,
        vertical=True,
        # draw_value=True,
        # value_pos="bottom",
        inverted=True,
        value=Utils.Poll(1000, lambda self: getCpuPercent()).bind("output")
    )

def ramUsageScale():
    return Widget.Scale(
        css_classes=["monitoring"],
        min=0,
        max=100,
        vertical=True,
        inverted=True,
        value=Utils.Poll(1000, lambda self: getRamPercent()).bind("output")
    )
def cpuScaleBox():
    return Widget.Box(
        vertical=False,
        spacing=1,
        child=[
            cpuUsageScale(),
            ramUsageScale()
        ]
    )

def cpuTempLabel():
    return Widget.Label(
        label=Utils.Poll(1000, lambda self: getCpuTemp() + "°C").bind("output")
    )

def cpuLabel():
    return Widget.Label(
        label="CPU"
    )


def getGpuPercent():
    nvmlInit()
    handle = nvmlDeviceGetHandleByIndex(0)
    usage = nvmlDeviceGetUtilizationRates(handle)

    # print(usage.gpu)
    nvmlShutdown()
    return usage.gpu


def getVramPercent():
    nvmlInit()
    handle = nvmlDeviceGetHandleByIndex(0)
    usage = nvmlDeviceGetUtilizationRates(handle)

    # print(usage.memory)
    nvmlShutdown()
    return usage.memory


def getGpuTemp():
    nvmlInit()
    handle = nvmlDeviceGetHandleByIndex(0)
    temp = nvmlDeviceGetTemperature(handle, 0)

    # print(temp)
    nvmlShutdown()
    return str(temp)

def gpuUsageScale():
    return Widget.Scale(
        css_classes=["monitoring"],
        min=0,
        max=100,
        vertical=True,
        draw_value=False,
        inverted=False,
        value=Utils.Poll(1000, lambda self: getGpuPercent()).bind("output")
    )

def vramUsageScale():
    return Widget.Scale(
        css_classes=["monitoring"],
        min=0,
        max=100,
        vertical=True,
        inverted=False,
        value=Utils.Poll(1000, lambda self: getVramPercent()).bind("output")
    )
def gpuScaleBox():
    return Widget.Box(
        vertical=False,
        spacing=1,
        child=[
            gpuUsageScale(),
            vramUsageScale()
        ]
    )

  

def gpuTempLabel():
    return Widget.Label(
        label=Utils.Poll(1000, lambda self: getGpuTemp() + "°C").bind("output")
    )

def gpuLabel():
    return Widget.Label(
        label="GPU"
    )

def spacer():
    return Widget.Label(
        label="---"
    )
def cpu():
    return Widget.Box(
        vertical=True,
        css_classes=["monitoring"],
        halign="center",
        valign="center",
        spacing=1,
        child=[
            cpuScaleBox(),
            cpuTempLabel(),
            spacer(),
            cpuLabel(),
            spacer(),
        ]
    )

def gpu():
    return Widget.Box(
        vertical=True,
        css_classes=["monitoring"],
        halign="center",
        valign="center",
        spacing=1,
        child=[
            spacer(),
            gpuLabel(),
            spacer(),
            gpuTempLabel(),
            gpuScaleBox()
        ]
    )
