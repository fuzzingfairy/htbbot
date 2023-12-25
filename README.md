# HTB toolkit

Tracks number of boxes done, box statistics and tries to estimate time to do a given retired box.

# Usage:
Scrapes hackthebox data from site.
```
python3 scrape.py
```

Picks box that takes the longest tiem based on a predictive model.
```
python3 hardest.py
```

Picks 3 random tjnull starter boxes that you have not done.
```
python3 tjnull.py
```

# Structure

## data
- data/data.json raw box data used to track number of boxes done
- data/times.csv records box info and the time it took you to do a box
- data/tjnullstarter list of tjnull starter boxes
