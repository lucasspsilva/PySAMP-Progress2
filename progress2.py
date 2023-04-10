from . import *

class PlayerProgressBar:
    def __init__(self, id) -> None:
        self.id = id

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
    ):
        return cls(
            create_player_progress_bar(
            playerid,
            x,
            y,
            width,
            height,
            color,
            max,
            direction,            
            )
        )

    
    def destroy_for_player(self, playerid: int):
        return destroy_player_progress_bar(playerid, self.id)
    
    def show_for_player(self, playerid: int):
        return show_player_progress_bar(playerid, self.id)
    
    def get_pos_for_player(self, playerid: int):
        return get_player_progress_bar_pos(playerid, self.id)
    
    def set_pos_for_player(self, playerid: int, x: float, y: float):
        return set_player_progress_bar_pos(playerid, self.id, x, y)
    
    def get_width_for_player(self, playerid: int):
        return get_player_progress_bar_width(playerid, self.id)
    
    def set_width_for_player(self, playerid: int, width: float):
        return set_player_progress_bar_width(playerid, self.id, width)
    
    def get_height_for_player(self, playerid: int):
        return get_player_progress_bar_height(playerid, self.id)
    
    def set_height_for_player(self, playerid: int, height: float):
        return set_player_progress_bar_height(playerid, self.id, height)
    
    def get_colour_for_player(self, playerid: int):
        return get_player_progress_bar_colour(playerid, self.id)
    
    def set_colour_for_player(self, playerid: int, colour: int):
        return set_player_progress_bar_colour(playerid, self.id, colour)
    
    def get_max_value_for_player(self, playerid: int):
        return get_player_progress_bar_max_value(playerid, self.id)
    
    def set_max_value_for_player(self, playerid: int, max_val: float):
        return set_player_progress_bar_max_value(playerid, self.id, max_val)
    
    def get_value_for_player(self, playerid: int):
        return get_player_progress_bar_value(playerid, self.id)
    
    def set_value_for_player(self, playerid: int, value: float):
        return set_player_progress_bar_value(playerid, self.id, value)
    
    def get_direction_for_player(self, playerid: int):
        return get_player_progress_bar_direction(playerid, self.id)
    
    def set_direction_for_player(self, playerid: int, direction: int):
        return set_player_progress_bar_direction(playerid, self.id, direction)

