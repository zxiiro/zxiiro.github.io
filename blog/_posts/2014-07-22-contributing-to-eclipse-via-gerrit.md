---
layout: post
title: "Contributing to Eclipse Projects via Gerrit"
published: true
tags:
- eclipse
- linux
---

## Gerrit Overview

Gerrit is a Web based code review system that is being deployed to projects at Eclipse.

## Creating and configuring your Gerrit account

Gerrit does not know your account exists until you login for the first time. Simply

For checking out repositories, Gerrit does not let you use the same password as your eclipse.org account password.
instead you will need to use either SSH or HTTP authentication. With SSH you simply upload your SSH keys.

### Upload your SSH keys

### Generate HTTP password

If using SSH key based authentication is not possible for you, or you would rather use a password. Gerrit will generate
a random password for you.

## Updating a existing Git repo to use Gerrit URL

If you have already cloned a Git project at Eclipse you do not need to reclone, simply update your Git URLs to point
to the new Gerrit URLs and you can start using Gerrit.

## Checkout a Gerrit Project
## Push to Gerrit
## Push to Gerrit for Review
## Updating a patch for Review
