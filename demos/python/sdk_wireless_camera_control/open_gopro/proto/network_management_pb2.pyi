"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
from . import response_generic_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _EnumProvisioning:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EnumProvisioningEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EnumProvisioning.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PROVISIONING_UNKNOWN: _EnumProvisioning.ValueType
    PROVISIONING_NEVER_STARTED: _EnumProvisioning.ValueType
    PROVISIONING_STARTED: _EnumProvisioning.ValueType
    PROVISIONING_ABORTED_BY_SYSTEM: _EnumProvisioning.ValueType
    PROVISIONING_CANCELLED_BY_USER: _EnumProvisioning.ValueType
    PROVISIONING_SUCCESS_NEW_AP: _EnumProvisioning.ValueType
    PROVISIONING_SUCCESS_OLD_AP: _EnumProvisioning.ValueType
    PROVISIONING_ERROR_FAILED_TO_ASSOCIATE: _EnumProvisioning.ValueType
    PROVISIONING_ERROR_PASSWORD_AUTH: _EnumProvisioning.ValueType
    PROVISIONING_ERROR_EULA_BLOCKING: _EnumProvisioning.ValueType
    PROVISIONING_ERROR_NO_INTERNET: _EnumProvisioning.ValueType
    PROVISIONING_ERROR_UNSUPPORTED_TYPE: _EnumProvisioning.ValueType

class EnumProvisioning(_EnumProvisioning, metaclass=_EnumProvisioningEnumTypeWrapper):
    pass

PROVISIONING_UNKNOWN: EnumProvisioning.ValueType
PROVISIONING_NEVER_STARTED: EnumProvisioning.ValueType
PROVISIONING_STARTED: EnumProvisioning.ValueType
PROVISIONING_ABORTED_BY_SYSTEM: EnumProvisioning.ValueType
PROVISIONING_CANCELLED_BY_USER: EnumProvisioning.ValueType
PROVISIONING_SUCCESS_NEW_AP: EnumProvisioning.ValueType
PROVISIONING_SUCCESS_OLD_AP: EnumProvisioning.ValueType
PROVISIONING_ERROR_FAILED_TO_ASSOCIATE: EnumProvisioning.ValueType
PROVISIONING_ERROR_PASSWORD_AUTH: EnumProvisioning.ValueType
PROVISIONING_ERROR_EULA_BLOCKING: EnumProvisioning.ValueType
PROVISIONING_ERROR_NO_INTERNET: EnumProvisioning.ValueType
PROVISIONING_ERROR_UNSUPPORTED_TYPE: EnumProvisioning.ValueType
global___EnumProvisioning = EnumProvisioning

class _EnumDeprecated:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EnumDeprecatedEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EnumDeprecated.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DEPRECATED_1: _EnumDeprecated.ValueType
    DEPRECATED_2: _EnumDeprecated.ValueType
    DEPRECATED_3: _EnumDeprecated.ValueType
    DEPRECATED_4: _EnumDeprecated.ValueType
    DEPRECATED_5: _EnumDeprecated.ValueType
    DEPRECATED_6: _EnumDeprecated.ValueType
    DEPRECATED_7: _EnumDeprecated.ValueType

class EnumDeprecated(_EnumDeprecated, metaclass=_EnumDeprecatedEnumTypeWrapper):
    pass

DEPRECATED_1: EnumDeprecated.ValueType
DEPRECATED_2: EnumDeprecated.ValueType
DEPRECATED_3: EnumDeprecated.ValueType
DEPRECATED_4: EnumDeprecated.ValueType
DEPRECATED_5: EnumDeprecated.ValueType
DEPRECATED_6: EnumDeprecated.ValueType
DEPRECATED_7: EnumDeprecated.ValueType
global___EnumDeprecated = EnumDeprecated

class RequestConnectNew(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SSID_FIELD_NUMBER: builtins.int
    PASSWORD_FIELD_NUMBER: builtins.int
    STATIC_IP_FIELD_NUMBER: builtins.int
    GATEWAY_FIELD_NUMBER: builtins.int
    SUBNET_FIELD_NUMBER: builtins.int
    DNS_PRIMARY_FIELD_NUMBER: builtins.int
    DNS_SECONDARY_FIELD_NUMBER: builtins.int
    SET_TO_LEAST_PREFERRED_AP_FIELD_NUMBER: builtins.int
    DEPRECATED_FIELD_NUMBER: builtins.int
    ssid: typing.Text
    password: typing.Text
    static_ip: builtins.bytes
    gateway: builtins.bytes
    subnet: builtins.bytes
    dns_primary: builtins.bytes
    dns_secondary: builtins.bytes
    set_to_least_preferred_ap: builtins.bool
    deprecated: global___EnumDeprecated.ValueType

    def __init__(
        self,
        *,
        ssid: typing.Optional[typing.Text] = ...,
        password: typing.Optional[typing.Text] = ...,
        static_ip: typing.Optional[builtins.bytes] = ...,
        gateway: typing.Optional[builtins.bytes] = ...,
        subnet: typing.Optional[builtins.bytes] = ...,
        dns_primary: typing.Optional[builtins.bytes] = ...,
        dns_secondary: typing.Optional[builtins.bytes] = ...,
        set_to_least_preferred_ap: typing.Optional[builtins.bool] = ...,
        deprecated: typing.Optional[global___EnumDeprecated.ValueType] = ...
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "deprecated",
            b"deprecated",
            "dns_primary",
            b"dns_primary",
            "dns_secondary",
            b"dns_secondary",
            "gateway",
            b"gateway",
            "password",
            b"password",
            "set_to_least_preferred_ap",
            b"set_to_least_preferred_ap",
            "ssid",
            b"ssid",
            "static_ip",
            b"static_ip",
            "subnet",
            b"subnet",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "deprecated",
            b"deprecated",
            "dns_primary",
            b"dns_primary",
            "dns_secondary",
            b"dns_secondary",
            "gateway",
            b"gateway",
            "password",
            b"password",
            "set_to_least_preferred_ap",
            b"set_to_least_preferred_ap",
            "ssid",
            b"ssid",
            "static_ip",
            b"static_ip",
            "subnet",
            b"subnet",
        ],
    ) -> None: ...

global___RequestConnectNew = RequestConnectNew

class ResponseConnectNew(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    RESULT_FIELD_NUMBER: builtins.int
    PROVISIONING_STATE_FIELD_NUMBER: builtins.int
    TIMEOUT_SECONDS_FIELD_NUMBER: builtins.int
    result: response_generic_pb2.EnumResultGeneric.ValueType
    provisioning_state: global___EnumProvisioning.ValueType
    timeout_seconds: builtins.int

    def __init__(
        self,
        *,
        result: typing.Optional[response_generic_pb2.EnumResultGeneric.ValueType] = ...,
        provisioning_state: typing.Optional[global___EnumProvisioning.ValueType] = ...,
        timeout_seconds: typing.Optional[builtins.int] = ...
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "provisioning_state",
            b"provisioning_state",
            "result",
            b"result",
            "timeout_seconds",
            b"timeout_seconds",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "provisioning_state",
            b"provisioning_state",
            "result",
            b"result",
            "timeout_seconds",
            b"timeout_seconds",
        ],
    ) -> None: ...

global___ResponseConnectNew = ResponseConnectNew

class NotifProvisioningState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PROVISIONING_STATE_FIELD_NUMBER: builtins.int
    provisioning_state: global___EnumProvisioning.ValueType

    def __init__(
        self, *, provisioning_state: typing.Optional[global___EnumProvisioning.ValueType] = ...
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["provisioning_state", b"provisioning_state"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["provisioning_state", b"provisioning_state"]
    ) -> None: ...

global___NotifProvisioningState = NotifProvisioningState
