Compatibility
==============


.. toctree::
   :maxdepth: 1
   :caption: Compatibility
   :name: toc-metin2-knowledge-compatibility

   improvements

Compatible Platforms
=====================

# [//]: # (TODO: Review text for correction and minimization)

Client
=======
The Metin2 client is ONLY compatible with Windows 2000 or newer operating system. (The newer official versions of the game ships a Chromium Embemmed Framework browser and Steam API, which are not compatible with Windows 2000 or XP. Leaked source code that we have access to DOES NOT include such changes.)

The following technologies would need to be changed or upgraded in order to launch the client in a non-Windows envionment!


Server
=======

The Metin2 server is compatible with both Windows and FreeBSD
operating system.

It is NOT compatible with any Linux based operative system.
The server should be compatible with any BSD variant,
as well as CygWin (the source code contains some reference of CygWin).


FreeBSD
********

BSD Extensions/File Monitoring
###############################

Metin2 uses BSD C extensions and FreeBSD native API for monitoring both sockets and files (by using the native API called kqueue).

The source code already contains definitions for the BSD C extensions in Windows platform, as well as a working implementation of socket monitoring (using select), but not for the File Monitor.

The select implementation does not correctly work under Linux based systems, that would either fix the implementation or add support for epoll.

NOTE: There could be more issues in the networking (perhaps related to how Linux handles networking interfaces).


Windows
********


