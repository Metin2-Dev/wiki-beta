# Handshake

A Handshake is the standard synchrony integrity verification, it is used 
to make sure that agents communicating with each other are valid and aware
of phase states, encryption and time synchronization

It is always used first before data incoming to the game or authentication
agent can be accepted, and it is also performed when a phase change occurs


## Shaking
To perform a handshake, the server generates a *Hand* which we are
going to call the `right hand`, gets it current time and a time delta (used for
synchronizing the time with the other agent) and puts it in a
[Handshake](../Data/Packets/Handshake.md) packet

It stores the hand and after that it sends it to the other agent and in the
**next instruction**, stores the current time and flags that a handshake
is happening, so that it can be used later for validation and synchronization

When the packet is received by the client agent, it generates a *Hand*
which we will call the `left hand`, stores the received server time contained
in the packet, creates a new equally formatted Handshake packet, puts the left
hand in it and sends it to the server agent

When the server agent receives it, checks if the hand is still the same as the
one that was last sent, if it isn't the connection is terminated

Next it checks if it is in the Handshake Phase, if so it will validate if the
time between shakes is valid and synchronized, the process is explained below

If it is valid and synchronized, other synchronizations are perform, like the
[IPE](IPE.md)


## Synchronization validation

First it will start by checking if the received time delta from the packet
is below 0, if so it will return as invalid

Then it will check the time difference, adding the received Handshake packet's
time and delta and subtracting to the current server time, for example:
`current_server_time - handshake_packet_time + handshake_packet_delta`

Then it will check if the result is inbetween a range, by default is from `0`
to `50`, and if it is it means the handshake is valid, so it will store
the current time as the client agent's time and set the handshake as done

Otherwise, if it is not in the range, the server agent will generate a new
delta by getting the current server time and subtracting it to the Handshake
packet time, then divided by two, for example:
`(current_server_time - handshake_packet_time) / 2`

Then it will increase the retry count by one and send it to the client
and the same process as since the whole beginning will occur, it will store
the time of when the packet was sent, the client will send it back to the
server, then validate and so on...

There is a limit for how many times this process can be retried,
by default its `32` times, but depends on the server settings for this
option


## Hand generation
The hand is a pseudo random number from `0` to `4.294.967.295`
(the range of a 32-bit unsigned integer)

[//]: # (TODO: Investigate the details of hand generation)


