from PySide6.QtCore import QObject, Signal

from src.model import ConnectionState, ControlMessage, VoicePacket


class AudioClientSignals(QObject):
    # emit when connection changed
    connection_state_changed = Signal(ConnectionState)
    # emit when receive control message
    control_message_received = Signal(ControlMessage)
    # emit when receive voice data
    voice_data_received = Signal(VoicePacket)
    # emit when send voice data
    voice_data_sent = Signal()
    # emit when receive error
    error_occurred = Signal(str)
    # emit when frequency change
    update_current_frequency = Signal(int)

    # emit to log message
    # arguments: from | level | content
    log_message = Signal(str, str, str)

    # signals below are for internal use
    # emit when tcp and udp socket connect or disconnect
    socket_connection_state = Signal(bool)
    # emit when input device changed
    audio_input_device_change = Signal(int)
    # emit when output device changed
    audio_output_device_change = Signal(int)
    # emit when ptt button pressed or released
    ptt_status_change = Signal(bool)
