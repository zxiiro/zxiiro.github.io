#!/bin/bash

export PRE_COMMIT_ALLOW_NO_CONFIG=1

git worktree add -f /tmp/site master

cd src && hugo
cd /tmp/site
git add .
git commit -sm "Update site $(date +'%Y%m%d-%H%M')"
git push

git worktree remove -f /tmp/site
