#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Dict, TypeVar, Union

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands

from ..mobilecommand import MobileCommand as Command

T = TypeVar("T", bound=CanExecuteCommands)


class Location(CanExecuteCommands):
    def toggle_location_services(self: T) -> T:
        """Toggle the location services on the device.

        Android only.

        Returns:
            Union['WebDriver', 'Location']: Self instance
        """
        self.execute(Command.TOGGLE_LOCATION_SERVICES, {})
        return self

    def set_location(
        self: T,
        latitude: Union[float, str],
        longitude: Union[float, str],
        altitude: Union[float, str, None] = None,
        speed: Union[float, str, None] = None,
        satellites: Union[float, str, None] = None,
    ) -> T:
        """Set the location of the device

        Args:
            latitude: String or numeric value between -90.0 and 90.00
            longitude: String or numeric value between -180.0 and 180.0
            altitude: String or numeric value (Android real device only)
            speed: String or numeric value larger than 0.0 (Android real devices only)
            satellites: String or numeric value of active GPS satellites in range 1..12. (Android emulators only)

        Returns:
            Union['WebDriver', 'Location']: Self instance
        """
        data = {
            "location": {
                "latitude": latitude,
                "longitude": longitude,
            },
        }
        if altitude is not None:
            data["location"]["altitude"] = altitude
        if speed is not None:
            data["location"]["speed"] = speed
        if satellites is not None:
            data["location"]["satellites"] = satellites
        self.execute(Command.SET_LOCATION, data)
        return self

    @property
    def location(self) -> Dict[str, float]:
        """Retrieves the current location

        Returns:
            A dictionary whose keys are
                - latitude (float)
                - longitude (float)
                - altitude (float)
        """
        return self.execute(Command.GET_LOCATION)[
            "value"
        ]  # pylint: disable=unsubscriptable-object

    def _add_commands(self) -> None:
        """Add location endpoints. They are not int w3c spec."""
        # noinspection PyProtectedMember,PyUnresolvedReferences
        commands = self.command_executor._commands
        commands[Command.TOGGLE_LOCATION_SERVICES] = (
            "POST",
            "/session/$sessionId/appium/device/toggle_location_services",
        )
        commands[Command.GET_LOCATION] = ("GET", "/session/$sessionId/location")
        commands[Command.SET_LOCATION] = ("POST", "/session/$sessionId/location")
