import logging

from homeassistant.util import utcnow

from custom_components.ecoflow_cloud.devices import BaseDevice
from custom_components.ecoflow_cloud.entities import (
    BaseSensorEntity, BaseNumberEntity, BaseSelectEntity, BaseSwitchEntity
)
from custom_components.ecoflow_cloud.sensor import (
    AmpSensorEntity, CentivoltSensorEntity, DeciampSensorEntity,
    DecicelsiusSensorEntity, DecihertzSensorEntity, DeciwattsSensorEntity,
    DecivoltSensorEntity, InWattsSolarSensorEntity, LevelSensorEntity,
    MiscSensorEntity, RemainSensorEntity, StatusSensorEntity, ReconnectStatusSensorEntity,
)
from ...api import EcoflowApiClient

# from ..number import MinBatteryLevelEntity, MaxBatteryLevelEntity
# from ..select import DictSelectEntity
_LOGGER = logging.getLogger(__name__)


class PowerOcean(BaseDevice):
    def sensors(self, client: EcoflowApiClient) -> list[BaseSensorEntity]:
        return []

    def numbers(self, client: EcoflowApiClient) -> list[BaseNumberEntity]:
        return []

    def switches(self, client: EcoflowApiClient) -> list[BaseSwitchEntity]:
        return []

    def selects(self, client: EcoflowApiClient) -> list[BaseSelectEntity]:
        return []

    def _prepare_data(self, raw_data) -> dict[str, any]:
        raw = {"params": {}}
        from .proto import ecopacket_pb2 as ecopacket, powerocean_pb2 as powerocean
        try:
            payload = raw_data

            while True:
                packet = ecopacket.SendHeaderMsg()
                packet.ParseFromString(payload)

                _LOGGER.debug("cmd id %u payload \"%s\"", packet.msg.cmd_id, payload.hex())

                if packet.msg.cmd_id == 8:
                    _LOGGER.debug("pdata %s", packet.msg.pdata)

                    report = powerocean.TestChangeReport()
                    report.ParseFromString(payload)

                    for descriptor in report.DESCRIPTOR.fields:
                        if not report.HasField(descriptor.name):
                            continue

                        raw["params"][descriptor.name] = getattr(report, descriptor.name)

                    _LOGGER.info("Found %u fields", len(raw["params"]))

                    raw["timestamp"] = utcnow()

                else:
                    _LOGGER.info("Unsupported EcoPacket cmd id %u", packet.msg.cmd_id)


                    #proto_message_types = {
                    #    1: powerocean.HeartbeatReport(),
                    #    7: powerocean.BpHeartbeatReport(),
                    #    8: powerocean.ChangeReport(),
                    #    13: powerocean.ParamChangeReport()
                    #}



                    # pdata example
                    # b'\x84\x15\xbb+' = 8415bb2b = 132, 21, 187, 43
                    # 132 >>> 3 --> right shift 3 bits --> decimal 16, which is the ID for "emsFeedMode"
                    #
                    # 144, 1, 157, 63
                    # 144 >>> 3 --> right shift 3 bits --> decimal 18, which is the ID for "emsFeedPwr"
                    #

                if packet.ByteSize() >= len(payload):
                    break

                _LOGGER.info("Found another frame in payload")

                packet_length = len(payload) - packet.ByteSize()
                payload = payload[:packet_length]

        except Exception as error:
            _LOGGER.error(error)
            _LOGGER.info(raw_data.hex())

        return raw
