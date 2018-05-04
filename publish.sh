#!/bin/bash
cp CNAME ../zxiiro.github.io/
cd ../zxiiro.github.io
git add .
git commit -sm "Update site"
git push
