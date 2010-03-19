#!/bin/bash

echo "SVN commit"

svn add v2.0/images/*
svn add v2.0/thumbs/*

svn commit -m "Autopush to google"



