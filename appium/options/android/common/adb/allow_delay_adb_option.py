# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from typing import Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

ALLOW_DELAY_ADB = "allowDelayAdb"


class AllowDelayAdbOption(SupportsCapabilities):
    @property
    def allow_delay_adb(self) -> Optional[bool]:
        """
        Whether to prevent the emulator to use -delay-adb feature.
        """
        return self.get_capability(ALLOW_DELAY_ADB)

    @allow_delay_adb.setter
    def allow_delay_adb(self, value: bool) -> None:
        """
        Being set to false prevents emulator to use -delay-adb feature to detect its startup.
        See https://github.com/appium/appium/issues/14773 for more details.
        """
        self.set_capability(ALLOW_DELAY_ADB, value)
