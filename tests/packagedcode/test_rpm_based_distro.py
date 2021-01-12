#
# Copyright (c) nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/scancode-toolkit/ for support and download.

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import os.path
import json
from unittest.case import skipIf

from commoncode.system import py2
from packagedcode import rpm_based_distro
from packages_test_utils import check_result_equals_expected_json
from packages_test_utils import PackageTester


#@skipIf(py2, 'Alpine linux package parsing is not worth testing on Python2')
class TestRpmBasePackage(PackageTester):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_parse_alpine_installed_db_small(self):
        test_installed = self.get_test_loc('rpm_distro/rpm.xml.txt')
        result = [package.to_dict(_detailed=True)
            for package in rpm_based_distro.parse_rpm_db(test_installed)]
        expected = test_installed + '-expected.json'
        check_result_equals_expected_json(result, expected, regen=False)

