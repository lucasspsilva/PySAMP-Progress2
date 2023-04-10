from . import *

class PlayerProgressBar:
    def __init__(self, playerid: int, bar_id: int) -> None:
        self.playerid = playerid
        self.bar_id = bar_id

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
            )
        )


    
    def destroy(self):
        return destroy_player_progress_bar(self.playerid, self.bar_id)
    
    def hide(self):
        return hide_player_progress_bar(self.playerid, self.bar_id)
    
    def show(self):
        return show_player_progress_bar(self.playerid, self.bar_id)
    
    def get_pos(self):
        return get_player_progress_bar_pos(self.playerid, self.bar_id)
    
    def set_pos(self, x: float, y: float):
        return set_player_progress_bar_pos(self.playerid, self.bar_id, x, y)
    
    def get_width(self):
        return get_player_progress_bar_width(self.playerid, self.bar_id)
    
    def set_width(self, width: float):
        return set_player_progress_bar_width(self.playerid, self.bar_id, width)
    
    def get_height(self):
        return get_player_progress_bar_height(self.playerid, self.bar_id)
    
    def set_height(self, height: float):
        return set_player_progress_bar_height(self.playerid, self.bar_id, height)
    
    def get_colour(self):
        return get_player_progress_bar_colour(self.playerid, self.bar_id)
    
    def set_colour(self, colour: int):
        return set_player_progress_bar_color(self.playerid, self.bar_id, colour)
    
    def get_max_value(self):
        return get_player_progress_bar_max_value(self.playerid, self.bar_id)
    
    def set_max_value(self, max_val: float):
        return set_player_progress_bar_max_value(self.playerid, self.bar_id, max_val)
    
    def get_value(self):
        return get_player_progress_bar_value(self.playerid, self.bar_id)
    
    def set_value(self, value: float):
        return set_player_progress_bar_value(self.playerid, self.bar_id, value)
    
    def get_direction(self):
        return get_player_progress_bar_direction(self.playerid, self.bar_id)
    
    def set_direction(self, direction: int):
        return set_player_progress_bar_direction(self.playerid, self.bar_id, direction)

