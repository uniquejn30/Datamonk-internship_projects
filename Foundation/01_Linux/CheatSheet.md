# 🐧 Linux Command Reference

A beginner-friendly table of essential Linux commands, including descriptions, examples, and explanations of what each command does.

| **Command** | **Description** | **Practice Example** | **What It Does** |
| --- | --- | --- | --- |
| `ls` | List files/directories | `ls -lh` | Lists with size in human-readable format |
| `pwd` | Show current path | `pwd` | Prints current directory location |
| `cd` | Change directory | `cd ~/Documents` | Navigates to Documents |
| `mkdir` | Create folder | `mkdir demo` | Makes a folder named demo |
| `rmdir` | Remove empty directory | `rmdir demo` | Deletes demo folder (if empty) |
| `rm` | Delete files/folders | `rm file.txt`<br>`rm -r myfolder/` | Deletes a file or a folder |
| `cp` | Copy files/folders | `cp file1.txt copy.txt`<br>`cp -r dir1/ dir2/` | Copies file or folder |
| `mv` | Move or rename | `mv old.txt new.txt` | Renames or moves a file |
| `touch` | Create file | `touch hello.txt` | Makes an empty file |
| `echo` | Print/write to file | `echo "Hi" > hi.txt` | Writes "Hi" into a file |
| `cat` | View file | `cat hello.txt` | Prints file contents |
| `less` | View file (paged) | `less bigfile.txt` | Scrollable file viewer |
| `head` | View top lines | `head -n 5 file.txt` | Shows first 5 lines |
| `tail` | View last lines | `tail -f log.txt` | Shows real-time updates |
| `nano` | Terminal text editor | `nano file.txt` | Opens file in terminal for editing |
| `vim` | Advanced terminal editor | `vim file.txt` | Opens file in Vim |
| `clear` | Clear terminal | `clear` | Wipes terminal screen |
| `history` | Show past commands | `history` | Displays command history |
| `man` | Show manual | `man cp` | Shows help for `cp` |
| `sudo` | Run as root | `sudo apt update` | Executes with admin permission |
| `apt` | Package manager | `sudo apt install git` | Installs a package |
| `apt-get` | Advanced pkg manager | `sudo apt-get upgrade` | Upgrades all packages |
| `add-apt-repository` | Add repo | `sudo add-apt-repository ppa:xyz/abc` | Adds PPA |
| `df` | Show disk space | `df -h` | Shows free/used disk in human-readable units |
| `du` | File size usage | `du -sh *` | Shows space used by each item |
| `uname` | System info | `uname -a` | Shows OS/kernel details |
| `whoami` | Current user | `whoami` | Displays your username |
| `id` | User UID/GID info | `id` | Shows user and group IDs |
| `top` | View running processes | `top` | Live system monitor |
| `htop` | Colorful process viewer | `htop` | Easier-to-read `top` (needs install) |
| `ps` | List processes | `ps aux` | All processes currently running |
| `kill` | Kill process | `kill 1234` | Kills PID 1234 |
| `killall` | Kill by name | `killall chrome` | Kills all "chrome" processes |
| `chmod` | Change permissions | `chmod +x run.sh` | Makes a script executable |
| `chown` | Change ownership | `sudo chown $USER:$USER file.txt` | Gives file ownership to you |
| `find` | Search files | `find . -name "*.txt"` | Searches for all `.txt` files |
| `locate` | Fast file finder | `locate config.json` | Searches indexed files (faster than `find`) |
| `updatedb` | Update locate DB | `sudo updatedb` | Updates file index for `locate` |
| `grep` | Search inside files | `grep "error" log.txt` | Finds lines with “error” |
| `awk` | Text/data processing | `awk '{print $1}' file.txt` | Prints 1st column of each line |
| `cut` | Cut by delimiter | `cut -d ':' -f1 /etc/passwd` | Cuts first field separated by `:` |
| `sort` | Sort lines | `sort names.txt` | Alphabetically sorts lines |
| `uniq` | Remove duplicates | `uniq sorted.txt` | Filters repeating lines |
| `wc` | Word/line count | `wc -l file.txt` | Counts lines in file |
| `tar` | Archive files | `tar -czvf backup.tar.gz folder/` | Compresses folder to tar.gz |
| `zip` | Create zip file | `zip file.zip file.txt` | Zips file.txt into file.zip |
| `unzip` | Extract zip | `unzip file.zip` | Unzips contents |
| `ping` | Check internet | `ping google.com` | Pings Google continuously |
| `ip` | Network info | `ip a` | Shows network interface details |
| `netstat` | Port info (deprecated) | `netstat -tuln` | Lists open ports |
| `ss` | Modern netstat | `ss -tunlp` | View open ports with process ID |
| `tcpdump` | Capture network packets | `sudo tcpdump -i eth0` | Captures live network traffic |
| `nmap` | Network scanner | `nmap 192.168.1.1` | Scans a device for open ports |
| `rsync` | File sync | `rsync -av source/ dest/` | Copies and syncs folders |
| `date` | Show current date | `date` | Shows system date/time |
| `cal` | Calendar | `cal` | Shows current month calendar |
| `alias` | Create command shortcut | `alias ll='ls -lah'` | Makes shortcut for command |
| `exit` | Close terminal/session | `exit` | Logs out or closes session |
| `reboot` | Restart system | `sudo reboot` | Restarts machine |
| `shutdown` | Shutdown system | `sudo shutdown now` | Powers off immediately |
| `lsb_release -a` | Check Ubuntu version | `lsb_release -a` | Prints distribution info |

---

📝 *This cheat sheet is perfect for beginners learning Linux or anyone who needs a quick terminal reference!*
