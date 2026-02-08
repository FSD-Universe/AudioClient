#  Copyright (c) 2025-2026 Half_nothing
#  SPDX-License-Identifier: MIT
"""
FSUIPC 客户端：通过 libfsuipc 与飞行模拟器通信，读写 COM 频率与连接状态。
依赖 lib/libfsuipc.dll，使用 ctypes 调用 C 接口。
"""
from collections.abc import Callable
from ctypes import POINTER, Structure, c_bool, c_char_p, c_int32, c_uint16, c_uint32, c_uint8, cast, cdll
from dataclasses import dataclass
from pathlib import Path

_simulator_name: dict[str, list[str]] = {
    "zh-CN": ["未知", "FS98", "FS2K", "CFS2", "CFS1", "FLY", "FS2K2", "FS2K4", "FSX", "ESP", "P3D"]
}


class CBaseModel(Structure):
    """C 层通用返回结构：请求状态与错误信息。"""
    _fields_ = [
        ("requestStatus", c_bool),
        ("errMessage", c_char_p)
    ]


class CConnectionStatus(Structure):
    """C 层连接状态结构。"""
    _fields_ = [
        ("requestStatus", c_bool),
        ("errMessage", c_char_p),
        ("status", c_uint32)
    ]


class CFrequencies(Structure):
    """C 层频率信息：COM1/COM2 等频率及接收标志。"""
    _fields_ = [
        ("requestStatus", c_bool),
        ("errMessage", c_char_p),
        ("frequencyFlag", c_uint8),
        ("frequency", c_uint32 * 4)
    ]


class CVersion(Structure):
    """C 层版本信息：模拟器类型、FSUIPC 版本等。"""
    _fields_ = [
        ("requestStatus", c_bool),
        ("errMessage", c_char_p),
        ("simulatorType", c_uint16),
        ("fsuipcVersion", c_uint32),
        ("apiVersion", c_uint8)
    ]


@dataclass
class BaseModel:
    """FSUIPC 调用返回的通用字段。"""
    request_status: bool
    err_message: str


@dataclass
class ConnectionStatus(BaseModel):
    status: int


@dataclass
class Frequencies(BaseModel):
    """COM 频率与接收标志，含 com1_rx/com2_rx 等解析属性。"""
    frequency_flag: int
    frequency: list[int]

    @property
    def com1_rx(self) -> bool:
        return self.frequency_flag & 0xA0 != 0x80

    @property
    def com2_rx(self) -> bool:
        return self.frequency_flag & 0x60 != 0x40


@dataclass
class Version(BaseModel):
    """FSUIPC/模拟器版本信息，含 version、simulator_name 等属性。"""
    simulator_type: int
    fsuipc_version: int
    api_version: int

    @property
    def version(self) -> str:
        hiword = (self.fsuipc_version & 0xFFFF0000) >> 16
        loword = self.fsuipc_version & 0x0000FFFF

        major = (hiword >> 12) & 0x0F
        minor = ((hiword >> 8) & 0x0F) * 100 + ((hiword >> 4) & 0x0F) * 10 + (hiword & 0x0F)
        build_letter = '' if loword == 0 else chr(ord('a') + loword - 1)

        version_str = f"{major}.{minor}"
        if build_letter != '':
            version_str += build_letter

        return version_str

    @property
    def simulator_name(self, locale: str = "zh-CN") -> str:
        if self.simulator_type >= len(_simulator_name[locale]):
            return _simulator_name[locale][0]
        return _simulator_name[locale][self.simulator_type]


class FSUIPCClient:
    """FSUIPC 客户端封装：加载 DLL，提供打开/关闭、读频率、设 COM 频率等接口。"""

    def __init__(self, fsuipc_lib_path: Path) -> None:
        fsuipc_lib = cdll.LoadLibrary(str(fsuipc_lib_path.resolve()))
        fsuipc_lib.OpenFSUIPCClient.restype = POINTER(CVersion)
        fsuipc_lib.CloseFSUIPCClient.restype = POINTER(CBaseModel)
        fsuipc_lib.ReadFrequencyInfo.restype = POINTER(CFrequencies)
        fsuipc_lib.GetConnectionState.restype = POINTER(CConnectionStatus)
        fsuipc_lib.GetFSUIPCVersionInfo.restype = POINTER(CVersion)
        fsuipc_lib.SetCom1Frequency.argtypes = [c_int32]
        fsuipc_lib.SetCom1Frequency.restype = POINTER(CBaseModel)
        fsuipc_lib.SetCom2Frequency.argtypes = [c_int32]
        fsuipc_lib.SetCom2Frequency.restype = POINTER(CBaseModel)
        fsuipc_lib.FreeMemory.argtypes = [POINTER(CBaseModel)]
        fsuipc_lib.FreeMemory.restype = None
        self._fsuipc_lib = fsuipc_lib

    def open_fsuipc_client(self) -> Version:
        func = self._get_function("OpenFSUIPCClient")
        result = func()
        try:
            version = Version(
                request_status=result.contents.requestStatus,
                err_message=result.contents.errMessage.decode("utf-8"),
                simulator_type=result.contents.simulatorType,
                fsuipc_version=result.contents.fsuipcVersion,
                api_version=result.contents.apiVersion
            )
        finally:
            self._free_memory(result)
        return version

    def close_fsuipc_client(self) -> BaseModel:
        func = self._get_function("CloseFSUIPCClient")
        result = func()
        try:
            base_model = BaseModel(
                request_status=result.contents.requestStatus,
                err_message=result.contents.errMessage.decode("utf-8")
            )
        finally:
            self._free_memory(result)
        return base_model

    def get_connection_state(self) -> ConnectionStatus:
        func = self._get_function("GetConnectionState")
        result = func()
        try:
            connection_status = ConnectionStatus(
                request_status=result.contents.requestStatus,
                err_message=result.contents.errMessage.decode("utf-8"),
                status=result.contents.status
            )
        finally:
            self._free_memory(result)
        return connection_status

    def get_fsuipc_version_info(self) -> Version:
        func = self._get_function("GetFSUIPCVersionInfo")
        result = func()
        try:
            version = Version(
                request_status=result.contents.requestStatus,
                err_message=result.contents.errMessage.decode("utf-8"),
                simulator_type=result.contents.simulatorType,
                fsuipc_version=result.contents.fsuipcVersion,
                api_version=result.contents.apiVersion
            )
        finally:
            self._free_memory(result)
        return version

    def get_frequency(self) -> Frequencies:
        func = self._get_function("ReadFrequencyInfo")
        result = func()
        try:
            frequencies = Frequencies(
                request_status=result.contents.requestStatus,
                err_message=result.contents.errMessage.decode("utf-8"),
                frequency_flag=result.contents.frequencyFlag,
                frequency=result.contents.frequency[:]
            )
        finally:
            self._free_memory(result)
        return frequencies

    def set_com1_frequency(self, frequency: int) -> BaseModel:
        func = self._get_function("SetCom1Frequency")
        result = func(frequency)
        try:
            base_model = BaseModel(
                request_status=result.contents.requestStatus,
                err_message=result.contents.errMessage.decode("utf-8")
            )
        finally:
            self._free_memory(result)
        return base_model

    def set_com2_frequency(self, frequency: int) -> BaseModel:
        func = self._get_function("SetCom2Frequency")
        result = func(frequency)
        try:
            base_model = BaseModel(
                request_status=result.contents.requestStatus,
                err_message=result.contents.errMessage.decode("utf-8")
            )
        finally:
            self._free_memory(result)
        return base_model

    def _get_function(self, function_name: str) -> Callable:
        """按名称获取 DLL 中的函数。"""
        if not hasattr(self._fsuipc_lib, function_name):
            raise AttributeError(f"Function {function_name} not available")
        return getattr(self._fsuipc_lib, function_name)

    def _free_memory(self, pointer) -> None:
        """释放 DLL 返回的指针，避免内存泄漏。"""
        base_ptr = cast(pointer, POINTER(CBaseModel))
        self._fsuipc_lib.FreeMemory(base_ptr)
