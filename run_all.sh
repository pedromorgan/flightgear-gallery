#!/bin/bash

sh ./make_thumbs.sh
python ./make_index.py
sh ./push_to_google.sh


echo "All done !"
