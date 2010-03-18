This is currently proof of concept.

The idea is to host the gallery images here on google.

This is then called remotely.

=========================================================================================
Gallery Process 
=========================================================================================

1) drop any new images in the v2.0/images/ directory

2) run "make_thumbs.sh" to process the images and generate the xml/json files

3) run "make_index.py" to generate the xml and json indexes

4) run "push_to_google" to commit changes to google svn server

5) "run_all.sh" does all the above


==========================================================================================
Feed
==========================================================================================

The feed is at this link 

http://flightgear-gallery.googlecode.com/svn/trunk/gallery.js

