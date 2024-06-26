# Copyright (C) 2013-2023 Bastian Kleineidam
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Test the isoinfo program"""

from . import ArchiveTest
from .. import needs_program


class TestIsoinfo(ArchiveTest):
    """Test class for the isoinfo program"""

    program = 'isoinfo'

    @needs_program(program)
    def test_isoinfo(self):
        """List an ISO archive."""
        self.archive_list('t.iso')

    @needs_program(program)
    def test_isoinfo_file(self):
        """List a renamed ISO archive."""
        self.archive_list('t.iso.foo')
