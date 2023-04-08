from samp import CallRemoteFunction
import struct

BAR_DIRECTION_RIGHT = 0
BAR_DIRECTION_LEFT = 1
BAR_DIRECTION_UP = 3
BAR_DIRECTION_DOWN = 4


def create_player_progress_bar(
    playerid: int,
    x: float,
    y: float,
    width: float = 55.5,
    height: float = 3.2,
    color: int = 0xFFFFFFFF,
    max: float = 100.0,
    direction: int = BAR_DIRECTION_RIGHT,
):
    return CallRemoteFunction(
        "CreatePlayerProgressBar_py",
        playerid,
        x,
        y,
        width,
        height,
        color,
        max,
        direction,
    )


def destroy_player_progress_bar(playerid: int, progressbar: int):
    return CallRemoteFunction("DestroyPlayerProgressBar_py", playerid, progressbar)


def show_player_progress_bar(playerid: int, progressbar: int):
    return CallRemoteFunction("ShowPlayerProgressBar_py", playerid, progressbar)


def get_player_progress_bar_pos(playerid: int, progressbar: int):
    pos_packed = CallRemoteFunction("GetPlayerProgressBarPos_py", playerid, progressbar)
    x = pos_packed & 0xFFFF
    y = pos_packed >> 16
    return (x / 1000, y / 1000)


def set_player_progress_bar_pos(playerid: int, progressbar: int, x: float, y: float):
    return CallRemoteFunction("SetPlayerProgressBarPos_py", playerid, progressbar, x, y)


def get_player_progress_bar_width(playerid: int, progressbar: int):
    width = CallRemoteFunction("GetPlayerProgressBarWidth_py", playerid, progressbar)
    return width / 1000


def set_player_progress_bar_width(playerid: int, progressbar: int, width: float):
    return CallRemoteFunction(
        "SetPlayerProgressBarWidth_py", playerid, progressbar, width
    )


def get_player_progress_bar_height(playerid: int, progressbar: int):
    height = CallRemoteFunction("GetPlayerProgressBarHeight_py", playerid, progressbar)
    return struct.unpack("<f", (height).to_bytes(4, "little"))[0]


def set_player_progress_bar_height(playerid: int, progressbar: int, height: float):
    return CallRemoteFunction(
        "SetPlayerProgressBarHeight_py", playerid, progressbar, height
    )


def get_player_progress_bar_color(playerid: int, progressbar: int):
    return CallRemoteFunction("GetPlayerProgressBarColour_py", playerid, progressbar)


get_player_progress_bar_colour = get_player_progress_bar_color


def set_player_progress_bar_color(playerid: int, progressbar: int, color: int):
    return CallRemoteFunction(
        "SetPlayerProgressBarColour_py", playerid, progressbar, color
    )


set_player_progress_bar_colour = get_player_progress_bar_color


def get_player_progress_bar_max_value(playerid: int, progressbar: int):
    max_value = CallRemoteFunction(
        "GetPlayerProgressBarMaxValue_py", playerid, progressbar
    )
    return struct.unpack("<f", (max_value).to_bytes(4, "little"))[0]


def set_player_progress_bar_max_value(
    playerid: int, progressbar: int, max_value: float
):
    return CallRemoteFunction(
        "SetPlayerProgressBarMaxValue_py", playerid, progressbar, max_value
    )


def get_player_progress_bar_value(playerid: int, progressbar: int):
    value = CallRemoteFunction("GetPlayerProgressBarValue_py", playerid, progressbar)
    return struct.unpack("<f", (value).to_bytes(4, "little"))[0]


def set_player_progress_bar_value(playerid: int, progressbar: int, value: float):
    return CallRemoteFunction(
        "SetPlayerProgressBarValue_py", playerid, progressbar, value
    )


def get_player_progress_bar_direction(playerid: int, progressbar: int):
    return CallRemoteFunction("GetPlayerProgressBarDirection_p", playerid, progressbar)


def set_player_progress_bar_direction(playerid: int, progressbar: int, direction: int):
    return CallRemoteFunction(
        "SetPlayerProgressBarDirection_p", playerid, progressbar, direction
    )
