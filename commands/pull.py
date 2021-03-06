# Copyright (C) 2013 Fox Wilson, Peter Foley, Srijay Kasturi, Samuel Damashek and James Forcier
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import subprocess
from config import ADMINS
from os.path import dirname

args = ['nick']


def cmd(send, msg, args):
        if args['nick'] not in ADMINS:
            return
        try:
            gitdir = dirname(__file__) + '/..'
            output = subprocess.check_output(['git', 'pull'], cwd=gitdir).decode().splitlines()[-1]
            send(output)
        except subprocess.CalledProcessError:
            send("Something went wrong!")
