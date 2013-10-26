---
layout: post
title: Optimizing Freeseer Controller GUI Design
categories:
- fosslc
- freeseer
tags:
- freeseer
- python
status: publish
type: post
published: true
meta:
  _publicize_pending: '1'
  _wpas_done_757239: '1'
  _wpas_done_1297749: '1'
  _publicize_done_external: a:1:{s:8:"facebook";a:1:{i:90410736;b:1;}}
  publicize_twitter_user: zxiiro
  _wpas_done_757240: '1'
  _wpas_skip_1297749: '1'
  _wpas_skip_757240: '1'
  _wpas_skip_757239: '1'
  _elasticsearch_indexed_on: '2012-10-17 02:14:17'
---
Lately I've been looking into ways we can improve Freeseer's GUI to make it more simple and less complex looking. My current attention is at the Freeseer Controller Client UI. Lets take a look at what it looks like today.

<a href="/assets/blog/2012-10/connclient-01.png"><img class="img-responsive img-thumbnail" title="Conntroller Client Widget Today" alt="Image" src="/assets/blog/2012-10/connclient-01.png?w=374" height="349" width="224" /></a>

Without looking at code, I think it is likely using only 1 layout the QVBoxLayout which lays out widgets in a Vertical layout. While that is a simple and easy way of getting widgets attached to a window it tends to make GUIs rather long.

I bounced some ideas off to the guys in IRC and came up with a mockup for some improvements to this layout.

<a href="/assets/blog/2012-10/connclient-02.png"><img class="img-responsive img-thumbnail" title="New Connection Settings" alt="Image" src="/assets/blog/2012-10/connclient-02.png?w=326" height="197" width="196" /></a>
<a href="/assets/blog/2012-10/connclient-03.png"><img class="img-responsive img-thumbnail" title="New Recent Connections" alt="Image" src="/assets/blog/2012-10/connclient-03.png?w=326" height="197" width="196" /></a>

This new layout uses a QToolBox to separate the Connection settings and the Recent Connections log window. This allows the Widget to take up less screen estate as the logging window takes up a lot of space.

Another improvement is using the QFormLayout to set the Host/Port/Passphrase Labels on the left and their respective Edit boxes on the right. We have also reduced the Start and Connect button to simply be a single "Connect" button. From a user's perspective having a start and connect button is very confusing especially if you don't know what the difference is.

Finally removing completely the copy-paste box for copying connection information from a server instance. It simply took up way too much screen space it composes of a Text box as well as 2 buttons. My new idea is to change the copy paste text to simplify it to something like "passphrase@host:port" and allow the user to paste this into the host box. Logic can be set so that if it detects the correct format it will copy the details to the correct edit boxes.

Any ideas on further improvements to the mockups are welcome.
