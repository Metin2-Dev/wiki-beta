# Flow
Networking in metin2 is composed by multiple agents, most of the agents
have the purpose of serving for a specific task, them being:

 - Client (program the player uses to play)
 - Game (serves the game to the client)
 - Channels (individual game server processes that are clones of the server) 
 - Database (stores/gives data for the game)
 - Authentication (authenticates the clients along with the game)

We will go through how these communicate with each other at a concept
level step by step, assuming all the agents above are operational

For the rest of this page we are going to call the agents above as agents,
but keep in mind they can be an unique server process, a process of a
server, a client or what corresponds to their task


## Concept
Let's imagine we start the client, while starting the UI the first
thing it does is read from the settings which are the channels
to connect to and their respective ports

It starts a background task to probe the state of those channels,
if they are online and game information (like if the channel can be 
accessed, how many players, and so on)

Assuming there is an available channel, we can now try to log in
by typing a username and password, it will try to send it to the
Authentication agent but before that synchronization comes first, after
being synchronized the data packets are encrypted and sent


### Synchronization
Both agents need to be synchronized so that they know they are both valid
within each other, so to do that they use a [Handshake](Synchronization/Handshake.md)
or [IPE](Synchronization/IPE.md) method, or even both, if the latter is enabled

We are not going into detail on these methods here, but you should check
how they work to keep in mind for situations were they may come in the future

The final step is setting the phase, the authentication agent sends a packet
that tells the client that they will now be operating on the login phase,
you can read more on phases to also keep in mind, because they are an essential
part of the network flow, telling which packets are accepted at a given moment
depending on the current phase


### Encryption
After they are synchronized, any packet data that will be exchanged between
agents will need to be encrypted, once again we are not going into detail,
so you can check how [Encryption](Encryption/Encryption.md) works to keep in mind

