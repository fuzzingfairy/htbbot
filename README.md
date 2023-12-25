# HTB toolkit

Tracks number of boxes done, box statistics and tries to estimate time to do a given retired box.

# Usage:
Scrapes hackthebox data from site.
```
python3 scrape.py
```
Trains predictive model based on data in `data\times.csv`
```
python3 train.py
```

Picks box that takes the shortest time based on the predictive model.
```
python3 easiest.py
```

Picks box that takes the longest time based on the predictive model.
```
python3 hardest.py
```

Picks a random tjnull starter boxes that you have not done.
```
python3 tjnull.py
```

# TODO
- [ ] write datato sqlite datbase for easier querying and manipulations
- [ ] save predictions to  database so that easiest and hardest scripts don't take too long
- [ ] add htb track functionality
- [ ] add challenge tracking
- [ ] add sherlocks

# FIle Structure

## data
- `data/data.json` raw box data used to track number of boxes done
- `data/times.csv` records box info and the time it took you to do a box
- `data/tjnullstarter` list of tjnull starter boxes
