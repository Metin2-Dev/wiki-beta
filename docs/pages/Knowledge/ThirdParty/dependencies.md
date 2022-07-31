# Dependencies

## Client Binary

## DirectX 8 and Windows 32bit native APIs

Metin2 uses a lot of libraries from DirectX.

Direct3D8 as a graphic API, which is supressed by Direct3D11 (and optionally Direct3D9, which is the easiest to port). DirectInput, used to grab the mouse and keyboard input (now supressed by Windows native API and XInput2 for joystick). WinSock2 for networking and DirectShow to display the intro videos. And other Windows native API that handles important stuff like window creation, virtual file system (used in EterPacks), file I/O.

Today, there are modern libraries (like SDL2) that could be used to provide most of the Windows native API functions (as well as DirectInput and WinSock2). Mesa (open source render driver for linux) DOES support Direct3D9 (which the community has proven that the upgrade is possible). While DirectShow could be changed to any video render library (e.g. Bandicam or Bink) or completely removed.


### Granny 3D
Granny 3D is an animation engine that empowers Metin2.
This commercial product is also used in AAA games like The Elder Scrolls: Online, Lineage Forever, Battlefield Bad Company 2 and many more.

RAD sells Granny2 licenses to developers for each platform (e.g. the Windows SDK and the Linux one are two different products), as of today, there is no leaked SDK that works for Linux or other machines.

The default version that Metin2 uses is v2.4.0.7, although the community has shown that upgrading to v2.9 or v2.11 is possible.


### Miles Sound System

Miles sound system (MSS for short) is the Audio engine that Metin2 uses, developed by RAD, same as Granny 3D. As of today, both version 7 and version 9 are leaked (along with the sources for Linux). Same as Granny 3D, MSS is used in many popular games like Duke Nukem Forever, Warcraft II, Zoo Tycoon 2 and many more.

The default version that Metin2 uses is 6.5c.


### SpeedTree

SpeedTree is a commercial tree rendering engine, developed by Interactive Data Visualization, Inc. It is one of the best in the industry, used in AAA titles like Far Cry 5, Assassin's Creed Unity, Battlefield 4 and many more. As of today, the SDK for version 7 is leaked, and the source codes of version 4 are avaiable.

The version that Metin2 uses is v1.6.0.
