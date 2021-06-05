from datetime import timedelta

DOMAIN = "tuya_local"

CONF_DEVICE_ID = "device_id"
CONF_LOCAL_KEY = "local_key"
CONF_TYPE = "type"
CONF_TYPE_AUTO = "auto"
CONF_TYPE_GPPH_HEATER = "heater"
CONF_TYPE_DEHUMIDIFIER = "dehumidifier"
CONF_TYPE_FAN = "fan"
CONF_TYPE_GECO_HEATER = "geco_heater"
CONF_TYPE_EUROM_600_HEATER = "eurom_heater"
CONF_TYPE_GPCV_HEATER = "gpcv_heater"
CONF_TYPE_KOGAN_HEATER = "kogan_heater"
CONF_TYPE_KOGAN_SWITCH = "kogan_switch"
CONF_TYPE_GSH_HEATER = "gsh_heater"
CONF_TYPE_GARDENPAC_HEATPUMP = "gardenpac_heatpump"
CONF_TYPE_PURLINE_M100_HEATER = "purline_m100_heater"
CONF_TYPE_EANONS_HUMIDIFIER = "eanons_humidifier"
CONF_TYPE_REMORA_HEATPUMP = "remora_heatpump"
CONF_TYPE_INKBIRD_THERMOSTAT = "inkbird_thermostat"
CONF_CLIMATE = "climate"
CONF_DISPLAY_LIGHT = "display_light"
CONF_CHILD_LOCK = "child_lock"
CONF_SWITCH = "switch"
CONF_HUMIDIFIER = "humidifier"
API_PROTOCOL_VERSIONS = [3.3, 3.1]
SCAN_INTERVAL = timedelta(seconds=30)
