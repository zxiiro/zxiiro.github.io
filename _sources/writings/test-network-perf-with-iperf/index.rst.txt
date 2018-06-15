Test network performance with iperf
===================================

`iperf <https://code.google.com/archive/p/iperf/>`_ is a handy tool to check
network performance between 2 computers. You can install this tool using your
distro’s package manager.

There are 2 modes this tool runs in. Server and Client, you will need to run it
in server mode on one end and client mode on the other end.

Server usage:

.. code-block:: bash

   iperf -s

Client usage:

.. code-block:: bash

   iperf -c <host/ip>

Basically you want to run it with the ``-s`` option on the server side and the
``-c`` option on the client side. On the client end you will also need to
provider the server's *hostname* or *IP address*.

Here's an example of what it looks like when run.

.. code-block:: none

   ------------------------------------------------------------
   Client connecting to 192.168.32.50, TCP port 5001
   TCP window size: 22.9 KByte (default)
   ------------------------------------------------------------
   [  3] local 192.168.32.152 port 40885 connected with 192.168.32.50 port 5001
   [ ID] Interval       Transfer     Bandwidth
   [  3]  0.0-10.0 sec   897 MBytes   752 Mbits/sec
