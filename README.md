# python_scan
Python ip scan tool using multiprocessing

This little tool has come about because of my dive into learning more about multiprocessing and multithreading in python.

There is more that I would like to add onto this. Like the ability to also see how many threads are avaiable and allow the user to pick between cores, threads, or both to see a time differance.

The current setup of course only works for the /24 ip range. I would like to try an make it a little bit more flexable. 

-----------
  Running 
-----------

```python ip_scan.py```

It will first show a list of network interfaces that it finds. Enter the number for the interface you want to use.
The program will start to scan.
When it is completed, it will print out a list of alive ip addresses.

----------------
  Future Plans 
----------------

1. Allow the user to save the alive ip addresses to a file. Should have done this from the start.....
2. ~~To implament a process where it grabs the ip address off of the interface that is selected, so that the user does not have to manually edit it.~~
3. Implament a way for the user to specify the first three octets of a target ip.
4. See if there is a way to allow the user to input a ip with a subnet. ex: 192.168.1.0/24
5. Have a way that the last octet range can be auto generated based on the subnet info provided by the user.
