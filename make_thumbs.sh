#!/bin/bash

cd ./v2.0/images/
for img in `ls *.jpg`
do
  convert -resize 180 $img ../thumbnails/$img
  echo $img
done

cd ../../

