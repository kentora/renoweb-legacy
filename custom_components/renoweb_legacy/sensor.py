"""Sensor platform for Renoweb_Legacy."""
import logging

from .const import (
    ATTR_DESCRIPTION,
    ATTR_MATTYPE,
    ATTR_NEXT_PICKUP,
    ATTR_SCHEDULE,
    DEFAULT_NAME,
    ICON_RECYCLE,
    ICON_RESIDUAL,
)
from .const import DOMAIN
from .const import SENSOR
from .entity import RenowebLegacyEntity


_LOGGER: logging.Logger = logging.getLogger(__package__)


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    if not coordinator.data:
        return

    sensors = []
    for sensor in coordinator.data:
        sensors.append(RenowebLegacySensor(coordinator, entry, sensor))
        _LOGGER.debug("SENSOR ADDED: %s", sensor)

    async_add_devices(sensors)


class RenowebLegacySensor(RenowebLegacyEntity):
    """renoweb_legacy Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return self.coordinator.data.get(self.sensor).get("ordningnavn")

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get(self.sensor).get("daysuntilpickup")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        mattype = self.coordinator.data.get(self.sensor)["mattypeid"]
        if mattype in [500, 502, 491]:
            return ICON_RESIDUAL
        if mattype in [528, 532]:
            return ICON_RECYCLE
        else:
            _LOGGER.debug("Unknown mattype %s for sensor %s", mattype, self.name)

    @property
    def extra_state_attributes(self):
        data = self.coordinator.data.get(self.sensor)
        return {
            ATTR_NEXT_PICKUP: data.get("toemningsdato"),
            ATTR_SCHEDULE: data.get("toemningsdage"),
            ATTR_MATTYPE: data.get("mattypeid"),
            ATTR_DESCRIPTION: data.get("materielnavn"),
        }

    @property
    def device_class(self):
        """Return de device class of the sensor."""
        return "renoweb_legacy__custom_device_class"
