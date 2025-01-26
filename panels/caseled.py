import logging
import os
import gi
import sys
sys.path.append('/usr/lib/python3/dist-packages')  # Adjust path as needed
import RPi.GPIO as GPIO
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from ks_includes.screen_panel import ScreenPanel

class Panel(ScreenPanel):

    def __init__(self, screen, title):
        title = title or _("Leds")
        super().__init__(screen, title)

        # Initialize GPIO for the LED
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.OUT, initial=GPIO.HIGH)
        
        # Create ON Button
        on_button = self._gtk.Button("light_on", _("LIGHT ON"), "color4")
        on_button.connect("clicked", self.led_on_action)

        # Create OFF Button
        off_button = self._gtk.Button("light", _("LIGHT OFF"), "color1")
        off_button.connect("clicked", self.led_off_action)

        # Create and configure the grid
        self.grid = Gtk.Grid(row_homogeneous=True, column_homogeneous=True)
        self.grid.attach(on_button, 0, 0, 1, 1)  # Attach ON button (column 0, row 0)
        self.grid.attach(off_button, 1, 0, 1, 1)  # Attach OFF button (column 1, row 0)

        # Add the grid to the panel
        self.content.add(self.grid)

    def led_on_action(self, *args):
        """Turn ON the LED."""
        GPIO.output(4, GPIO.LOW)  # Turn on light

    def led_off_action(self, *args):
        """Turn OFF the LED."""
        GPIO.output(4, GPIO.HIGH)  # Turn off light