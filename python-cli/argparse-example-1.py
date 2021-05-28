"""
A typical example of Python's argparse combined with configparser . #python #argparse #configparser
https://gist.github.com/drmalex07/9995807
"""

import os
import logging
import argparse
import ConfigParser as configparser
from paste.deploy.converters import asbool, asint, aslist

#
# Declare expected command-line arguments
#

argp = argparse.ArgumentParser()

# Add positional arguments (many)
argp.add_argument ("inputs", metavar='INFILE', type=str, nargs='+',
    help='Provide input logs to parse and load into database');

# Add an optional string argument 'config' 
argp.add_argument ("-c", "--config", dest='config_file', default='config.ini', type=str);

# Add a optional switch (boolean optional argument)
argp.add_argument ("-v", "--verbose", dest='verbose', default=False, action='store_true',
    help='Be verbose');

# Parse command line    
args = argp.parse_args()

#
# Parse a config ini-style file
#

"""
TBD:
The preferred order is to have a set of hardcoded configuration parameters in the code,
which will first get overwritten by config.ini file and finally the command line
arguments have the highest priority and they will overwrite whatever has been specified.
"""

here = os.path.realpath('.')

config_file = args.config_file
logging.info('Reading configuration from %s' %(config_file))
config = configparser.ConfigParser(defaults = {'here': here})
config.read(args.config_file)

# Do something with them

if args.verbose:
    logging.info('Will produce verbose output')

sqla_url = config.get('main', 'sqlalchemy_url')
