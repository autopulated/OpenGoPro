# communication_client.py/Open GoPro, Version 2.0 (C) Copyright 2021 GoPro, Inc. (http://gopro.com/OpenGoPro).
# This copyright was auto-generated on Tue Sep  7 21:35:53 UTC 2021

"""GoPro specific BLE client"""

import re
import logging
from pathlib import Path
from abc import ABC, abstractmethod
from typing import Generic, Optional, Union, Pattern

from open_gopro.ble import (
    BleDevice,
    BleHandle,
    BLEController,
    DisconnectHandlerType,
    NotiHandlerType,
    BleClient,
    BleUUID,
)
from open_gopro.wifi import WifiClient, WifiController
from open_gopro.responses import GoProResp, GoProDataHandler
from open_gopro.constants import GoProUUIDs, ProducerType, ResponseType

logger = logging.getLogger(__name__)


class GoProWifi(ABC, GoProDataHandler):
    """GoPro specific WiFi Client

    Args:
        controller (WifiController): instance of Wifi Controller to use for this client
    """

    def __init__(self, controller: WifiController):
        GoProDataHandler.__init__(self)
        self._wifi: WifiClient = WifiClient(controller)

    @abstractmethod
    def _get(self, url: str) -> GoProResp:
        """Send an HTTP GET request to a string endpoint.

        Args:
            url (str): endpoint not including GoPro base path

        Returns:
            GoProResp: GoPro response
        """
        raise NotImplementedError

    @abstractmethod
    def _stream_to_file(self, url: str, file: Path) -> None:
        """Send an HTTP GET request to an Open GoPro endpoint to download a binary file.

        Args:
            url (str): endpoint URL
            file (Path): location where file should be downloaded to
        """
        raise NotImplementedError

    @property
    def password(self) -> Optional[str]:
        """Get the GoPro AP's password

        Returns:
            Optional[str]: password or None if it is not known
        """
        return self._wifi.password

    @property
    def ssid(self) -> Optional[str]:
        """Get the GoPro AP's WiFi SSID

        Returns:
            Optional[str]: SSID or None if it is not known
        """
        return self._wifi.ssid


class GoProBle(ABC, GoProDataHandler, Generic[BleHandle, BleDevice]):
    """GoPro specific BLE Client

    Args:
        controller (BLEController): controller implementation to use for this client
        disconnected_cb (DisconnectHandlerType): disconnected callback
        notification_cb (NotiHandlerType): notification callback
        target (Union[Pattern, BleDevice]): regex or device to connect to
    """

    def __init__(
        self,
        controller: BLEController,
        disconnected_cb: DisconnectHandlerType,
        notification_cb: NotiHandlerType,
        target: Union[Pattern, BleDevice],
    ) -> None:
        GoProDataHandler.__init__(self)
        self._ble: BleClient = BleClient(
            controller,
            disconnected_cb,
            notification_cb,
            (re.compile(r"GoPro [A-Z0-9]{4}") if target is None else target, [GoProUUIDs.S_CONTROL_QUERY]),
            uuids=GoProUUIDs,
        )

    @abstractmethod
    def _register_listener(self, producer: ProducerType) -> None:
        """Register to receive notifications for a producer.

        Args:
            producer (ProducerType): producer that we want to receive notifications from
        """
        raise NotImplementedError

    @abstractmethod
    def _unregister_listener(self, producer: ProducerType) -> None:
        """Stop receiving notifications from a producer.

        Args:
            producer (ProducerType): Producer to stop receiving notifications for
        """
        raise NotImplementedError

    @abstractmethod
    def get_notification(self, timeout: Optional[float] = None) -> GoProResp:
        """Get a notification that was received from a registered producer.

        Args:
            timeout (float, Optional): Time to wait for a notification before returning. Defaults to None (wait forever)

        Returns:
            GoProResp: the received update
        """
        raise NotImplementedError

    @abstractmethod
    def _write_characteristic_receive_notification(
        self, uuid: BleUUID, data: bytearray, response_id: ResponseType
    ) -> GoProResp:
        """Write a characteristic and block until its corresponding notification response is received.

        Args:
            uuid (BleUUID): _description_
            data (bytearray): _description_
            response_id (ResponseType): identifier of expected response. used to find correct parser

        Returns:
            GoProResp: _description_
        """
        raise NotImplementedError

    @abstractmethod
    def _read_characteristic(self, uuid: BleUUID) -> GoProResp:
        """Read a characteristic and block until its corresponding notification response is received.

        Args:
            uuid (BleUUID): _description_

        Returns:
            GoProResp: _description_
        """
        raise NotImplementedError
