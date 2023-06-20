import logging
import voluptuous as vol

from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv

_LOGGER = logging.getLogger(__name__)

DOMAIN = "example_plugin"

# 服务定义
SERVICE_EXAMPLE = "example_service"
SERVICE_SCHEMA = vol.Schema({})

def setup(hass: HomeAssistant, config: dict):
    """设置插件"""

    def example_service(call):
        _LOGGER.info("Example service called")

    # 注册服务
    hass.services.register(DOMAIN, SERVICE_EXAMPLE, example_service, schema=SERVICE_SCHEMA)

    # 使用插件配置项
    config = config.get(DOMAIN)

    return True
