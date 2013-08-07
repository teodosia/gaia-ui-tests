# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from marionette.by import By
from marionette.keys import Keys
from gaiatest import GaiaTestCase


class TestEverythingMeLaunchApp(GaiaTestCase):

    _rocket_bar_icon_locator = (By.ID, 'rocketbar-activation-icon')
    _rocket_search_box_locator = (By.ID, 'rocketbar-input')
    _search_results_locator = (By.CSS_SELECTOR, '#rocketbar-search-results .visual')
    _search_results_from_everything_me = (By.CSS_SELECTOR, '#rocketbar-search-results .visual > small')

    def setUp(self):
        GaiaTestCase.setUp(self)
        self.apps.set_permission('Homescreen', 'geolocation', 'deny')
        self.connect_to_network()

    def test_launch_everything_me_app(self):
        # https://github.com/mozilla/gaia-ui-tests/issues/69

        app_name = 'Twitter'
        self.homescreen = self.apps.launch('Homescreen')
        self._tap_rocket_bar()
        self._type_into_rocket_search_box(app_name)

        self._wait_for_everthimg_me_results_to_load()

        # Tap on firt icon returned from Everthing.Me category
        self._tap_first_result()

        self.assertIn(app_name, self.marionette.title)

    def _type_into_rocket_search_box(self, search_term):
        search_input = self.marionette.find_element(*self._rocket_search_box_locator)
        search_input.clear()
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.RETURN)

    def _tap_rocket_bar(self):
        rocket_bar = self.marionette.find_element(*self._rocket_bar_icon_locator)
        rocket_bar.tap()

    def _wait_for_everthimg_me_results_to_load(self):
        self.wait_for_element_displayed(*self._search_results_locator)

    def _tap_first_result(self):
        result = self.marionette.find_element(*self._search_results_from_everything_me)
        result.tap()
