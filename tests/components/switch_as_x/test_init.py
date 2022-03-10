"""Tests for the Switch as X."""
import pytest

from homeassistant.components.switch_as_x import DOMAIN
from homeassistant.core import HomeAssistant

from tests.common import MockConfigEntry


@pytest.mark.parametrize("target_domain", ("light",))
async def test_config_entry_unregistered_uuid(hass: HomeAssistant, target_domain):
    """Test light switch setup from config entry with unknown entity registry id."""
    fake_uuid = "a266a680b608c32770e6c45bfe6b8411"

    config_entry = MockConfigEntry(
        data={},
        domain=DOMAIN,
        options={"entity_id": fake_uuid, "target_domain": target_domain},
        title="ABC",
    )

    config_entry.add_to_hass(hass)

    assert not await hass.config_entries.async_setup(config_entry.entry_id)
    await hass.async_block_till_done()

    assert len(hass.states.async_all()) == 0
