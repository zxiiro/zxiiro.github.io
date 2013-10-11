---
layout: post
title: ! 'Quick Tip: Razor Megalodon on Linux'
categories:
- linux
tags:
- headset
- linux
status: publish
type: post
published: true
meta:
  _publicize_pending: '1'
  _publicize_done_external: a:1:{s:8:"facebook";a:1:{i:90410736;b:1;}}
  _wpas_done_1297749: '1'
  publicize_twitter_user: zxiiro
  _wpas_done_757240: '1'
  _wpas_done_757239: '1'
  _elasticsearch_indexed_on: '2013-09-24 01:17:51'
  _wpas_skip_1297749: '1'
  _wpas_skip_757240: '1'
  _wpas_skip_757239: '1'
---
<p>
  I've been using a headset on my gaming computer for the longest time. The Razor Megalodon. It's a USB Headset from Razor which works pretty well on Windows but unfortunately it does not seem to work out of the box on Linux. For me anyway it's always gave me crackling sound when I try to play any audio.
</p>
<p>
  Today I finally discovered the fix for this is actually quite simple. The module snd-usb-audio settings need to be tweaked when using the Megalodon. I created a new file in <strong>/etc/modprobe.d/megalodon.conf</strong> and added a line:
</p>

<pre>options snd-usb-audio nrpacks=16</pre>

<p>With this setting I no longer hear crackling sound and the headset appears to work perfectly.</p>
