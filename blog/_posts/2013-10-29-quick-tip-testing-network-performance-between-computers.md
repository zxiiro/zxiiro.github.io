---
layout: post
title: "Quick Tip: Testing network performance between computers with iperf"
published: true
tags:
- linux
---
I discovered a handy tool to check network performance between 2 computers. This tool called
<a href="https://code.google.com/p/iperf/">iperf</a> is quite easy to use too. You can install this tool using your
distro's package manager. In my case I was using OpenSUSE which was available via "zypper install iperf".

There are 2 modes this tool runs in. Server and Client, you will need to run it in server mode on one end and client
mode on the other end. Doesn't matter which.

Server Usage:
<pre>
  iperf -s
</pre>

Client Usage:
<pre>
iperf -c host/ip
</pre>

Basically you want to run it with the "-s" option on the serverside and the "-c" option on the client side. On the
client end you will also need to provide the server's hostname or ip

Here is an example of what it looks like when I run it on my network.
<pre>
------------------------------------------------------------
Client connecting to 192.168.32.50, TCP port 5001
TCP window size: 22.9 KByte (default)
------------------------------------------------------------
[  3] local 192.168.32.152 port 40885 connected with 192.168.32.50 port 5001
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec   897 MBytes   752 Mbits/sec
</pre>
