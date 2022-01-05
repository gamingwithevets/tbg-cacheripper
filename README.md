# Basic info
CACHERIPPER is a file cache ripper for the game The Beginner's Guide.  
It is **only** designed to extract files from `filecache.bin`, located in `game-path/beginnersguide/`.

And yes, I made it myself since I don't see any on the Internet. I'm wondering if this repo will become popular.

**IMPORTANT NOTE: DO NOT TROLL THE SCRIPT BY MAKING IT EXTRACT FILES FROM A FAKE FILE CACHE!**

# Requirements
You just need Python...  
You can compile the script into a binary if you want. I won't provide any pre-compiled ones.

# How to use
## Preparations
First, find the file `filecache.bin` located in the directory mentioned above.  
After that, place it in the same directory as the script.
## Running
Now run `tbg_cacheripper.py`. It will first check for `filecache.bin` in the current directory. If it finds it, it will start extracting files.  
The process shouldn't take long, since all the files are text files. After it's done, the files are extracted to the `cacheripper_ripped` folder.
