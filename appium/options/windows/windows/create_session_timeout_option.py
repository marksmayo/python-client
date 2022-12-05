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

from datetime import timedelta
from typing import Optional, Union

from appium.options.common.supports_capabilities import SupportsCapabilities

CREATE_SESSION_TIMEOUT = "createSessionTimeout"


class CreateSessionTimeoutOption(SupportsCapabilities):
    @property
    def create_session_timeout(self) -> Optional[timedelta]:
        """
        Timeout used to retry Appium Windows Driver session startup.
        """
        value = self.get_capability(CREATE_SESSION_TIMEOUT)
        return None if value is None else timedelta(milliseconds=value)

    @create_session_timeout.setter
    def create_session_timeout(self, value: Union[timedelta, int]) -> None:
        """
        Set the timeout used to retry Appium Windows Driver session startup.
        This capability could be used as a workaround for the long startup times
        of UWP applications (aka Failed to locate opened application window
        with appId: TestCompany.my_app4!App, and processId: 8480).
        """
        self.set_capability(
            CREATE_SESSION_TIMEOUT,
            int(value.total_seconds() * 1000)
            if isinstance(value, timedelta)
            else value,
        )
