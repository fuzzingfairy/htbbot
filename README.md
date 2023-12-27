# HTB toolkit

Tracks number of boxes done, box statistics and tries to estimate time to do a given retired box.

# Usage:
```                                                                                      
┌──(kali㉿kali)-[~/htb/htbbot]
└─$ python3 tracks.py
Pick a track:
Track:  0 Active Directory 101 40%
Track:  1 Bank of America Track 0%
Track:  2 Beginner Track [Done]
Track:  3 CREST CCT APP 14%
Track:  4 CREST CCT INF 14%
Track:  5 CREST CRT 21%
Track:  6 CVE 33%
Track:  7 Cloud Track 14%
Track:  8 Common Applications 0%
Track:  9 Containers and Pivoting 0%
Track:  10 Deserialization 0%
Track:  11 EPAM Track 0%
Track:  12 Expert Track 0%
Track:  13 Intro to Android Exploitation 0%
Track:  14 Intro to Dante 0%
Track:  15 Intro to Offshore 50%
Track:  16 Intro to Printer Exploitation 0%
Track:  17 Intro to Zephyr 18%
Track:  18 Linux Privilege Escalation 101 0%
Track:  19 Password Cracking 14%
Track:  20 Pro Track 0%
Track:  21 Pwn The Database 12%
Track:  22 Pwn With Metasploit [Done]
Track:  23 Scripting Master 0%
Track:  24 Synack Red Team Track 0%
Track:  25 TJNULL 2003 hard 0%
Track:  26 TJNULL 2003 starter 18%
Track:  27 TJNULL 2022 hard 12%
Track:  28 TJNULL 2022 starter 14%
Track:  29 TJNULL original 22%
Track:  30 TJNULL original hard 18%
Track:  31 The Classics 22%
Track:  32 UHC Track 0%
Track:  33 UNI CTF 2021 Track 20%
Track:  34 fun 0%
Track number: 
```


# TODO
- [x] add tjnull challenge boxes
- [ ] write data to sqlite database for easier querying and manipulations
- [ ] save predictions to  database so that easiest and hardest scripts don't take too long
- [ ] add htb track functionality
- [ ] add challenge tracking
- [ ] add sherlocks

# FIle Structure

## data
- `data/data.json` raw box data used to track number of boxes done
- `data/times.csv` records box info and the time it took you to do a box
- `data/tjnullstarter` list of tjnull starter boxes
