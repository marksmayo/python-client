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

KEYSTORE_PASSWORD = "keystorePassword"


class KeystorePasswordOption(SupportsCapabilities):
    @property
    def keystore_password(self) -> Optional[str]:
        """
        Keystore password.
        """
        return self.get_capability(KEYSTORE_PASSWORD)

    @keystore_password.setter
    def keystore_password(self, value: str) -> None:
        """
        The password to the keystore file provided in keystorePath capability.
        This option is used in combination with useKeystore, keystorePath,
        keystorePassword, keyAlias and keyPassword options. Unset by default
        """
        self.set_capability(KEYSTORE_PASSWORD, value)
