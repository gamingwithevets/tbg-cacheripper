# Basic info
CACHERIPPER is a file cache ripper for the game The Beginner's Guide.  
It is **only** designed to extract files from `filecache.bin`, located in `game-path/beginnersguide[_<language>]/`.

And yes, I made it myself since I don't see any on the Internet. I'm wondering if this repo will become popular.

**IMPORTANT NOTE: DO NOT TROLL THE SCRIPT BY MAKING IT EXTRACT FILES FROM A FAKE FILE CACHE!**

# Requirements
You just need Python...  
You can compile the script into a binary if you want. I won't provide any pre-compiled ones.

# How to use
## Preparations
First, find the file `filecache.bin` located in the directory mentioned above.  
After that, copy the file path.
## Running
Now open a terminal and run `tbg_cacheripper.py <filecache-path>`. It will first check if the file exists, and validate the file. Then it will start extracting.    
The process shouldn't take long, since all the files are text files. After it's done, the files are extracted to the `cacheripper_ripped` folder.
