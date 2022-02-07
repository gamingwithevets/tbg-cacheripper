# Basic info
CACHERIPPER is a file cache ripper for the game The Beginner's Guide.  
It is **only** designed to extract files from `filecache.bin`, located in `game-path/beginnersguide[_<language>]/`.

And yes, I made it myself since I don't see any on the Internet. I'm wondering if this repo will become popular.

**IMPORTANT NOTE: DO NOT TROLL THE SCRIPT BY MAKING IT EXTRACT FILES FROM A FAKE FILE CACHE!**

# Requirements
You just need Python...  
You can compile the script into a binary if you want. I won't provide any pre-compiled ones.

# Usage
```
tbg_cacheripper.py [-h, --help] [-e, --export DIRECTORY] [-d, --disablelog] [-o, --overwrite] [-n, --newexport] [-a, --autoexit] filecache_path
```
## Parameters
| Parameter | Description |
|--|--|
| `filecache_path` | Path to the file cache for extracting. Checks will be in place to verify the file cache. |
| `-h, --help` | Show the help message. |
| `-e, --export DIRECTORY` | Export directory for extracting file caches. |
| `-d, --disablelog` | Skips creating `cacheripper.log` in the export directory. |
| `-o, --overwrite` | Overwrites the export directory even if it exists. |
| `-n, --newexport` | Prompts you to create a new export directory if the old one exists. |
| `-a, --autoexit` | Skips the 2 Enter presses required to exit the program. |

# Examples
To scan and extract files from `filecache.bin` in the directory `C:\Program Files (x86)\Steam\steamapps\common\The Beginner's Guide\beginnersguide`, type:
```
python tbg_cacheripper.py "C:\Program Files (x86)\Steam\steamapps\common\The Beginner's Guide\beginnersguide\filecache.bin"
```

To scan and extract files from `cache.cache` in the program's starting directory, type:
```
python tbg_cacheripper.py cache.cache
```

# Planned Features
Here's a list of my planned features for the next update:
- Scan the file cache only
- Add more checks for scanning file caches
- Without the auto-exit parameter, 10 Enter presses are required
- Make a "no UI" mode to avoid flashes
