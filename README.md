# CoopAPIEmulator
An emulator for the Coop's API. It pulls data from Matt's API and can be reset.

Use "/fetch/\<memberid\>/" to get \<memberid\>'s next shifts

Use "/put/" to POST a series of swaps 

To reload shifts from Coop's API, go to "/" and press the "Reload from real API" button.

When you reload, it fetches data for each memberid listed in data/id_list.csv from the Coop's API. This file contains a subset of all available memberids. For a full list look at data/id_list_full.csv.
