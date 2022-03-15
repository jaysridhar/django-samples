'use strict';

import dayjs from 'dayjs';
import utc from 'dayjs/plugin/utc';
import { timeSince } from './myfuncs';
import * as ut from './utils';
import { get_row, get_table } from './menu_funcs';
import { make_refresh_func, prepare_row } from './app_utils';

dayjs.extend(utc);

$(function() {
})
