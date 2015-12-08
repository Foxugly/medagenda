# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

import random
import string


def string_random(size):
    s = string.lowercase + string.uppercase + string.digits
    return ''.join(random.sample(s, size))
