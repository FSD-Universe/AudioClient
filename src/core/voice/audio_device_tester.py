#  Copyright (c) 2026 Half_nothing
#  SPDX-License-Identifier: MIT
"""配置页「耳机测试/扬声器测试」：麦克风 -> 编码 -> 指定设备播放，用于试听设备。"""
from pyaudio import PyAudio

from src.signal import AudioClientSignals
from .opus import OpusDecoder, OpusEncoder, SteamArgs
from .stream import InputAudioSteam, OutputAudioSteam


class AudioDeviceTester:
    """试听管道：输入流编码后通过 on_encoded_audio 送入输出流，支持切换输入/输出设备。"""

    def __init__(self, signals: AudioClientSignals, audio: PyAudio, encoder: OpusEncoder, decoder: OpusDecoder, /):
        super().__init__()
        self.active = False
        self.input_stream = InputAudioSteam(audio, encoder)
        self.output_stream = OutputAudioSteam(audio, decoder)
        self.input_stream.on_encoded_audio = self._on_encode_audio
        signals.ptt_status_change.connect(self._ptt_status_change)
        signals.microphone_gain_changed.connect(self._microphone_gain_change)

    def _microphone_gain_change(self, gain: int):
        self.input_stream.gain = gain

    def update_input_device(self, input_arg: SteamArgs):
        if self.input_stream.active:
            self.input_stream.restart(input_arg)

    def update_output_device(self, output_arg: SteamArgs):
        if self.output_stream.active:
            self.output_stream.restart(output_arg)

    def _ptt_status_change(self, status: bool):
        self.input_stream.input_active = status

    def _on_encode_audio(self, data: bytes):
        self.output_stream.play_encoded_audio(data)

    def start(self, input_arg: SteamArgs, output_arg: SteamArgs):
        """开始试听：启动输入与输出流。"""
        self.active = True
        self.input_stream.start(input_arg)
        self.output_stream.start(output_arg)

    def stop(self):
        """停止试听。"""
        self.input_stream.stop()
        self.output_stream.stop()
        self.active = False
