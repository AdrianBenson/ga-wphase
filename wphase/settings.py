# -*- coding: utf-8 -*-

"""
.. module:: settings

Configuration settings for :mod:`wphase`. At present, the settings are declared
directly as python variables, but eventually may be moved to an external file
(e.g. JSON) which persists outside the code base and can be customised for a
specific system.
"""

import os
import sys
import multiprocessing as mp

# Set the number of threads used by OpenBLAS.
os.environ['OPENBLAS_NUM_THREADS'] = '1'

#: Use HDF5 version of Green's functions (the alternative [original] is to use
#: SAC files).
USE_HDF5_GREENS_DB = True

#: Home directory for wphase. This will be used to define default locations for
#: where inputs (Green's functions, inventories, saved datasets) can be found
#: and where outputs will be written.
WPHASE_HOME = os.environ.get(
    "WPHASE_HOME",
    os.path.join(os.environ.get("HOME"), 'wphase'))
if not WPHASE_HOME:
    raise Exception('env var WPHASE_HOME is defined but is blank')

#: Directory containing the green's functions.
GREEN_DIR = os.environ.get('WPHASE_GREENS_FUNCTIONS')

#: Path to where datasets are saved for posterity.
WPHASE_SAVED_DATASETS_ROOT = os.environ.get(
    'WPHASE_SAVED_DATASETS_ROOT',
    os.path.join(WPHASE_HOME, 'wphase_saved_datasets'))
if not WPHASE_SAVED_DATASETS_ROOT:
    raise Exception('env var WPHASE_SAVED_DATASETS_ROOT is defined but is blank')

#: Path to system test datasets.
WPHASE_TEST_DATASETS_ROOT = os.environ.get(
    'WPHASE_TEST_DATASETS_ROOT',
    os.path.join(WPHASE_HOME, 'wphase_test_data'))
if not WPHASE_TEST_DATASETS_ROOT:
    raise Exception('env var WPHASE_TEST_DATASETS_ROOT is defined but is blank')

#: Root directory for system test data.
SYSTEM_TEST_DATA_ROOT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'tests', 'TEST_DATA')

#: The number of worker processes to use in :py:class:`multiprocessing.Pool`.
N_WORKERS_IN_POOL = None

#: The name of the JSON file to contain the output from wphase caclcutions.
WPHASE_OUTPUT_FILE_NAME = 'wphase_output.json'

#: Name of the file that contains the exclude list.
WPHASE_EXCLUDE_LIST_FILE_NAME = 'exclude_list.json'

#: wphase intermediate mseed file name.
WPHASE_MSEED_FILE = "Mini-SEED-traces.mseed"

#: Prefix for the names of the images containing the beachball.
WPHASE_BEACHBALL_PREFIX = "beachball"

#: Prefix for the station distribution plot.
WPHASE_STATION_DISTRIBUTION_PREFIX = "station_distribution"

#: Prefix for the grid search plot.
WPHASE_GRID_SEARCH_PREFIX = "grid_search"

#: Prefix for the names of the images containing the traces.
WPHASE_STATION_TRACES_PREFIX = "raw_traces"

#: Prefix for the names of the images containing the wphase traces.
WPHASE_RESULTS_TRACES_PREFIX = "wphase_traces"

#: Prefix for the names of the images containing the wphase misfit info.
WPHASE_MISFIT_PREFIX = "wphase_misfit"

#: Authority used for wphase.
GA_AUTHORITY = "GA W-phase"

#: The name of the current host.
WPHASE_HOST_NAME = os.environ.get(
    'WPHASE_HOST_NAME',
    'localhost')
if not WPHASE_HOST_NAME:
    raise Exception('env var WPHASE_HOST_NAME is defined but is blank')

#: Should profiling information for wphase be produced.
PROFILE_WPHASE = False

#: Number of traces to put in each wphase results plot
N_TRACES_PER_RESULT_PLOT = 6

#: Key for warnings in the result dictionary.
WPHASE_WARNINGS_KEY = 'Warnings'

#: Key for the wphase processing error.
WPHASE_ERROR_KEY = 'Error'

#: Key for the wphase event description.
WPHASE_EVENT_KEY = 'Event'

#: Key containing the stack trace.
WPHASE_ERROR_STACKTRACE_KEY = 'StackTrace'

#: Key for the list of wphase results plots.
RESULTS_PLOTS_KEY = 'WphaseResultPlots'

#: Key for the data source.
WPHASE_DATA_SOURCE_KEY = 'DataSource'

#: Key containing the wpinv profiling output.
WPINV_PROFILE_OUTPUT_KEY = 'WPInvProfile'

#: Key containing the misfits.
MISFIT_KEY = 'Misfits'

#: Key containing the host name.
HOST_NAME_KEY = 'HostName'

#: Key for errors caused by Antelope.
INVERSION_ERROR_KEY = 'InversionError'

#: Implementation of bandpass filter to use
BANDPASS_IMPLEMENTATION = 'scipy'

def safe_make_dir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

# ensure that all the directories we need to exist do exist.
safe_make_dir(WPHASE_SAVED_DATASETS_ROOT)
