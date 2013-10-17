---
layout: post
title: Mountain Lion / Gatekeeper selectively enforced?
categories:
- eclipse
- macosx
tags: []
status: publish
type: post
published: true
meta:
  _wpas_done_linkedin: '1'
  _wpas_done_facebook: '1'
  _wpas_done_twitter: '1'
  _elasticsearch_indexed_on: '2012-08-23 15:58:29'
---
I recently upgraded my Macbook to the new Mountain Lion with the intention to test the new Gatekeeper feature it provides to understand what it would take to provide packages that will work in the new OS. After doing a few test runs with unsigned applications I noticed a few oddities that I wouldn't have expected: I noticed in a few cases I was able to run my application despite it being unsigned even with the default settings.

Gatekeeper is a new security feature added in Mountain Lion that by default only allows applications to run if they are signed by a developer. In the default setup this means only applications downloaded from the AppStore or signed by a developer with a valid Apple Developer ID signature can be run on your system. The default setting that my system was left post upgrade is shown in the below screenshot.

<a href="/assets/blog/2012-08/screen-shot-2012-08-23-at-11-26-47-am.png"><img class="alignnone size-medium wp-image-51" title="Gatekeeper" src="/assets/blog/2012-08/screen-shot-2012-08-23-at-11-26-47-am.png?w=300" alt="" width="300" height="91" /></a>

&nbsp;

So in theory this should mean that I should not be able to run unsigned applications on my system. I thought I'd give this a try by downloading the latest Eclipse SDK 4.2 to see if it'll run. As expected when I try to run the application I am presented with a popup below that tells me the application cannot be opened because it is from an unidentified developer.

&nbsp;

<a href="/assets/blog/2012-08/screen-shot-2012-08-23-at-11-38-34-am1.png"><img class="alignnone size-full wp-image-53" title="Unidentified" src="/assets/blog/2012-08/screen-shot-2012-08-23-at-11-38-34-am1.png" alt="" width="408" height="188" /></a>

&nbsp;

At this point I thought great Gatekeeper's doing it's job and it seems to be working. However I noticed I was able to run applications that I compiled on my own machine without them being signed. Thinking this was a weird behaviour I thought I'd investigate it a little more. Noticing that the popup mentions that the application was downloaded using "Google Chrome" on a specific date I thought it'd try using different less conventional browsers to download the same application.

My first attempt I downloaded the same application via SCP from another computer of mine. When I tried to run it Gatekeeper did not prevent me from launching the unsigned application. Instead Eclipse launched just fine without any complaints.

Thinking maybe Gatekeeper doesn't consider SCP to be "the internet" I thought I'd try downloading the same Application using wget instead. So I pointed my wget to the Eclipse Download page for Eclipse SDK 4.2. When I tried to run the Eclipse SDK downloaded by wget I was still able to run it without any complaints from Gatekeeper despite again still being an unsigned application.

This seems to be a strange implementation of security to me. Admittedly most users will likely use a normal web browser such as Safari or Chrome or Firefox, etc... however it is strange to me that this security feature seems to be selectively active depending where your files come from and perhaps seems to be not as secure as it should be.
