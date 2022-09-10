"""RenowebLegacyEntity class"""
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DEFAULT_ATTRIBUTION
from .const import DOMAIN
from .const import NAME
from .const import VERSION


class RenowebLegacyEntity(CoordinatorEntity):
    def __init__(self, coordinator, config_entry, sensor):
        super().__init__(coordinator)
        self.config_entry = config_entry
        self.sensor = sensor

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return self.config_entry.entry_id + str(self.sensor)

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": NAME,
            "model": VERSION,
            "manufacturer": NAME,
        }
