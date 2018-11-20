README

songs.csv: list of songs that appeared in training data.
unique_tracks_full.csv: mapping of tracking_id and song_id for 1M songs. Full data set.
mismatches.txt: pairs listed here should not be considered. Not yet considered in my training data. https://labrosa.ee.columbia.edu/millionsong/blog/12-2-12-fixing-matching-errors 

Inside full_profile.zip:
   training.csv: 38,839,204 listening records of 1,019,318 users.
   test.csv: 10,581,579, listening records of 999,221 users.

Each listening record contains: user, count, track_id, song_id, artist, song_y
Sample:
b80344d063b5ccb3212f76538f3d9e43d87dca9e  1  TRIQAUQ128F42435AD  SOAKIMP12A8C130995  Jack Johnson  The Cove

# You can find how I created those datasets in Code_userprofile/User_profile.ipynb
# User taste profile website: https://labrosa.ee.columbia.edu/millionsong/tasteprofile