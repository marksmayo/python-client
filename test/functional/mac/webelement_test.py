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

from appium.webdriver.common.appiumby import AppiumBy
from test.functional.mac.helper.test_helper import BaseTestCase
from test.functional.test_helper import wait_for_element


class TestWebElement(BaseTestCase):
    def test_clear_text_field(self) -> None:
        edit_field = wait_for_element(
            self.driver, AppiumBy.CLASS_NAME, "XCUIElementTypeTextView"
        )
        edit_field.send_keys("helloworld")
        assert edit_field.text == "helloworld"
        edit_field.clear()
        assert edit_field.text == ""
