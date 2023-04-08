# PySAMP-Progress2

Progress2 include adapted to be used with PySAMP

## Installing

1.  Download the repository and put the filterscript and python folders in your server folder.
2.  Add the filterscript to your `server.cfg`.

## Usage

```py
from pysamp.commands import cmd
from .player import Player
from .registry import using_registry

from .pyprogress2 import create_player_progress_bar, show_player_progress_bar


@Player.on_connect
@using_registry
def on_player_connect(player: Player):
    barid = create_player_progress_bar(player.id, 50.0, 51.0)
    show_player_progress_bar(player.id, barid)
```

## Credits

- Flávio Toribio for developing Progress2
- [Southclaws](https://github.com/Southclaws) for maintaining [Progress2](https://github.com/Southclaws/progress2)
- [habecker](https://github.com/habecker),
  [denNorske](https://github.com/dennorske), [Cheaterman](https://github.com/Cheaterman),
  [Ykpauneu](https://github.com/Ykpauneu) for developing and maintaining [PySAMP](https://github.com/pysamp)
- All of the pysamp discord community for the extra help.
