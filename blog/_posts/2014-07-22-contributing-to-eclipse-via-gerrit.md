---
layout: post
title: "Contributing to Eclipse Projects via Gerrit"
published: true
tags:
- eclipse
- linux
---

## Gerrit Overview

Gerrit is a Web based code review system that is being deployed to projects at Eclipse. The service is available at
https://git.eclipse.org/r/


## Creating and configuring your Gerrit account

Gerrit does not know your account exists until you login for the first time. Simply login to Gerrit once if you have
not already did to initialize your Gerrit account. You can login at https://git.eclipse.org/r/

For checking out repositories, Gerrit does not let you use the same password as your eclipse.org account password.
Instead if you are using SSH authentication Gerrit requires you provide it with your SSH public key. If you are using
HTTP authentication then Gerrit will generate a random password for you.

SSH key based authentication is a bit more secure and easier as you do not need to save your password on your system.
GitHub has a pretty decent documentation on how to Generate SSH key pair if you are interested in trying this method
https://help.github.com/articles/generating-ssh-keys


### Upload your SSH keys

1. Login to Gerrit
2. Click your name at the top right
3. Click **Settings > SSH Public Keys** (https://git.eclipse.org/r/#/settings/ssh-keys)
4. Click **Add Key ..**
5. Paste the text of your public key into the text box
6. Click **Add**

Your key may look something like this:

    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDEELNeLbxkyFI3JfIC7sutF2NLJwizVDDljw6h2KB9dwUrVGUBQM7r9+4Ndp/ojJ+lEk8OuNh+Kicc0hwHLHz+v81ejN62yQe+c16fvard6MdkrA3xr1WuvNZDvBQhVUkNmEoYYa3C+GpvEmQssvrPhpU0RD6AELzBnrG+VME9Vb2ObvIHKj8OulxD96zk2GTRHM0KaR9XhLPsLQ7U0ML715BDA3k1Zf66DOmZiyzckZZD+YtiV3qnAfwW5hU9Xi+M92vqf5Z5mC7t6aX9Pu5TXb614NE1GKUZ6yDEWFLspo4ihl+X2pA2oMONjbgOG5gqlnBAArsG0WP6dVF+jKQ5 your_email@example.com

Note: The last part where it says your_email@example.com is actually just a comment and can be anything you want here.
      Typically I put my email address or some word to identify who's key this is or where it came from in case you
      have multiple keys.


### Generate HTTP password

If using SSH key based authentication is not possible for you, or you would rather use a password. You will need to tell
Gerrit to generate a random password for you before you can use password authentication.

1. Login to Gerrit
2. Click your name at the top right
3. Click **Settings > HTTP Password** (https://git.eclipse.org/r/#/settings/http-password)
4. Click **Generate**

![HTTP Password](/assets/blog/2014-07/gerrit-http-password.png "HTTP Password")

This random password will be the password you use to work with Git via Gerrit URLs. If you are ever worried that your
password is compromised simply clear your password and re-generate a new one.


## Understanding Eclipse Git and Gerrit URLs

At Eclipse we support 3 types of URLs git://, ssh://, and https://.

You can find the Git URLs via cGit at https://git.eclipse.org/c

For Git the URLs are:

- git://git.eclipse.org/gitroot/project/repo.git
- ssh://git.eclipse.org/gitroot/project/repo.git
- http://git.eclipse.org/gitroot/project/repo.git


You can find the Gerrit URLs via Gerrit at https://git.eclipse.org/r

For Gerrit the URLs are:

- git://git.eclipse.org/gitroot/project/repo
- ssh://git.eclipse.org:29418/project/repo
- https://git.eclipse.org/r/project/repo

**git:// url**

The first is a read-only URL via the git:// protocol. This URL is git://git.eclipse.org/gitroot/**project/repo.git**
and is the same no matter if you copied it from cGit or Gerrit.

- **project** is a directory containing all the repos for a specific project. For example the CBI project is under
/gitroot/**cbi**/repo.git
- **repo.git** is the specific git repository for a project, some projects may have more than 1 repo
- Tip: The final ".git" part of the URL is actually optional

**ssh:// urls**

Next the ssh:// protocol URLs are slightly different depending on if you are pulling from Git or Gerrit. If your project
is Gerrit enabled you should prefer the Gerrit URL otherwise you won't be able to push to the repository.

The reason the URLs are different is because Gerrit provides it's own SSH service on port 29418 and does not use the
same SSH service that is on the default port on git.eclipse.org.

Gerrit trims the "/gitroot" portion of the URL and adds a port ":29418" in it's place. This is the only difference
between the 2 URLs.

**http:// urls**

Again the URLs are slightly different depending on if you are using Git or Gerrit. If your project is Gerrit enabled
you should prefer the Gerrit URL otherwise you won't be able to push to the repository.

The reason the URL pattern is different here is because Gerrit hosts it's own HTTP service for Git. The difference here
is Gerrit only supports https (secure) and again Gerrit trims the "/gitroot" part of the URL and replaces it with "/r"
which is the Gerrit web URL.


## Updating a existing Git repo to use Gerrit URL

If you have already cloned a Git project at Eclipse you do not need to reclone, simply update your Git URLs to point
to the new Gerrit URLs and you can start using Gerrit.

**Using Git CLI**

    git remote set-url origin <gerrit-url>

**Using EGit**

1. Navigate to the Git perspective (Window > Open Perspective > Other > Git)
2. Right click on the repo you wish to modify
3. Click **Properties**
4. Under Configuration tab, look for remote > origin > url
5. Enter the new URL
6. Click **Apply**
7. Click **Ok**

![EGit Remote URL](/assets/blog/2014-07/gerrit-egit-url.png "Egit Remote URL")

## Checkout a Gerrit Project

**Using Git CLI**

    git clone <gerrit-url>

**Using EGit**

1. Navigate to the Git perspective (Window > Open Perspective > Other > Git)
2. Click the Clone Repository button in the Git Repository view
3. Enter the Gerrit URL into the URI link
4. Enter your credentials if applicable (If you are using SSH you'll have to configure your public/private keys)


## Push to Gerrit

Simply push as you would with any other repository and your changes will go directly into the repo.

**Using Git CLI**

    git push origin master

**Using EGit**


## Push to Gerrit for Review

Pushing for Review is a feature of Gerrit which allows you to push a patch online for developers to review. This is the
method you should use to push if you are not a committer on the project or if you'd like a second opinion on your patch
before it goes live.

Gerrit provides a special refspec to push your changes to which will instead of merging into the upstream repository
commits it to be reviewed. This refspec is **refs/for/\*** if where the \* tells Gerrit which branch you want your patch
to be reviewed against. For example if you'd like to push your patch to be reviewed against the **master** branch then
you push to **refs/for/master**. Change master to be any other existing branch online for it to be reviewed against
another branch.

**Using Git CLI**

    git push origin HEAD:refs/for/master

## Updating a patch for Review

**Using Git CLI**

    git add <files>
    git commit --amend

**Using EGit**

1. Navigate to the Git perspective (Window > Open Perspective > Other > Git)
2. Right click on the repo you are making changes to
3. Click **Commit...**
4. Select the files you modified
5. Check the **Amend Previous Commit** button

![EGit Amend](/assets/blog/2014-07/gerrit-egit-amend.png "Egit Amend")


## Navigating the Gerrit Website

For most contributors there will only be 2 tabs on Gerrit that will be of interest. The **My** tab and the **Projects**
tab. The **My** tab lists reviews that you've pushed to Gerrit or are CC'd on. Clicking any of them will

