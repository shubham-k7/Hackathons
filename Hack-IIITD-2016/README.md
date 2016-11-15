# NeSNis(Network Sniffing Analysis)

##Theme: IoT
##Team Members: Vasisht Duddu, Viraj Parimi, Mayank Mohindra

#Motivation

The project was started with the idea that a professor should be able to monitor the internet usage by students in the class.
They should also be given an oppurtunity to block a user for a temporary duration of time.

This idea could be extended to coporate environments and parental guidance at home.

#Working

![flowchart](https://cloud.githubusercontent.com/assets/20644368/17896754/5f472e10-696f-11e6-8e78-2c1e3550f738.png)

There is a Raspberry Pi which is mounted in the classroom. The Raspberry Pi sniffs user data and af filters it. The filtered output includes a bunch of .txt files contaning source IPs, destination IPs, Mac addresses of users,etc. These are then sent over to the web server via ssh which parses the files and uses High Charts to give a graphical analysis of websites being used. The web Application has an option to deauthenticate the user which is done using aireplay-ng.






