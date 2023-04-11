from . import *
from typing import Tuple


class PlayerProgressBar:
    def __init__(
        self,
        playerid: int,
        bar_id: int,
        x: float,
        y: float,
        width: float,
        height: float,
        color: int,
        max: float,
        direction: int,
    ) -> None:
        self.playerid = playerid
        self.bar_id = bar_id
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._max = max
        self._direction = direction

    @classmethod
    def create(
        cls,
        playerid: int,
        x: float,
        y: float,
        width: float = 55.5,
        height: float = 3.2,
        color: int = 0xFFFFFFFF,
        max: float = 100.0,
        direction: int = BAR_DIRECTION_RIGHT,
    ) -> "PlayerProgressBar":
        return cls(
            playerid,
            create_player_progress_bar(
                playerid,
                x,
                y,
                width,
                height,
                color,
                max,
                direction,
            ),
            x,
            y,
            width,
            height,
            color,
            max,
            direction,
        )

    def destroy(self):
        return destroy_player_progress_bar(self.playerid, self.bar_id)

    def hide(self):
        return hide_player_progress_bar(self.playerid, self.bar_id)

    def show(self):
        return show_player_progress_bar(self.playerid, self.bar_id)

    def get_pos(self) -> Tuple[float, float]:
        return self._x, self._y

    def set_pos(self, x: float, y: float):
        self._x, self._y = x, y
        return set_player_progress_bar_pos(self.playerid, self.bar_id, x, y)

    def get_width(self):
        return self._width

    def set_width(self, width: float):
        self._width = width
        return set_player_progress_bar_width(self.playerid, self.bar_id, width)

    def get_height(self):
        return self._height

    def set_height(self, height: float):
        self._height = height
        return set_player_progress_bar_height(self.playerid, self.bar_id, height)

    def get_colour(self):
        return get_player_progress_bar_color(self.playerid, self.bar_id)

    def set_colour(self, colour: int):
        return set_player_progress_bar_color(self.playerid, self.bar_id, colour)

    def get_color(self):
        return get_player_progress_bar_color(self.playerid, self.bar_id)

    def set_color(self, colour: int):
        return set_player_progress_bar_color(self.playerid, self.bar_id, colour)

    def get_max_value(self):
        return self._max

    def set_max_value(self, max_val: float):
        self._max = max_val
        return set_player_progress_bar_max_value(self.playerid, self.bar_id, max_val)

    def get_value(self):
        return get_player_progress_bar_value(self.playerid, self.bar_id)

    def set_value(self, value: float):
        return set_player_progress_bar_value(self.playerid, self.bar_id, value)

    def get_direction(self):
        return self._direction

    def set_direction(self, direction: int):
        self._direction = direction
        return set_player_progress_bar_direction(self.playerid, self.bar_id, direction)
