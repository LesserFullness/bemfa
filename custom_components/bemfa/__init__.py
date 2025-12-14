"""The bemfa integration."""
from __future__ import annotations

import hashlib
import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import CONF_UID, DOMAIN, OPTIONS_CONFIG
from .mqtt import BemfaMqtt
from .service import BemfaService

from . import (
    sync_binary_sensor,
    sync_sensor,
    sync_light,
    sync_fan,
    sync_cover,
    sync_climate,
    sync_switch,
)

_LOGGING = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up bemfa from a config entry."""
    # 新的异步初始化代码
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    # 添加平台
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "switch")
    )

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    # 卸载处理

    return True
