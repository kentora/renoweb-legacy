"""Constants for Renoweb_Legacy."""
# Base component constants
from token import TYPE_IGNORE


NAME = "Renoweb_Legacy"
DOMAIN = "renoweb_legacy"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.0"

ISSUE_URL = "https://github.com/kentora/renoweb-legacy/issues"

# Icons
ICON_RESIDUAL = "mdi:delete"
ICON_RECYCLE = "mdi:recycle"

# Platforms
PLATFORMS = ["sensor"]

SENSOR = "sensor"

# Configuration and options
ATTR_DESCRIPTION = "description"
ATTR_NEXT_PICKUP = "next_pickup"
ATTR_SCHEDULE = "schedule"
ATTR_MATTYPE = "mattype"

CONF_HOST = "host"
CONF_ADDRESS_ID = "address_id"
CONF_UPDATE_INTERVAL = "update_interval"

# Defaults
DEFAULT_NAME = DOMAIN

DEFAULT_ATTRIBUTION = "Data delivered by RenoWeb"
DEFAULT_BRAND = "RenoWeb"
DEFAULT_UPDATE_INTERVAL = 6


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is for renoweb legacy version.
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
