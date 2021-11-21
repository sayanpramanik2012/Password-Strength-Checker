First, we need to know what is BF-
Trying out all possible combinations of characters until the “correct answer” is found. This process can take a very long time, so dictionaries and lists of common passwords like "qwerty" or "123456" are usually used.

We should also know how to check whether our password is breached or not- We use Have I Been Pwned, a reputable service that collects information about account and password leaks. In this software I have used regular expression used oin python to get the input from user and check the password.

So initially, a password must have 8 characters or more than that.
To have a strong password we must have a digit, a lowercase, an uppercase and a special character or else it is considered as weak.

Packet sniffing, a network attack strategy, captures network traffic at the Ethernet frame level. After capture, this data can be analyzed and sensitive information can be retrieved. Such a network attack starts with a tool such as Wireshark. Wireshark allows you to capture and examine data that is flowing across your network. Any data that is not encrypted is readable, and unfortunately, many types of traffic on your network are passed as unencrypted data — even passwords and other sensitive data.
Obviously, this situation represents a danger to your corporate data. Many applications that house corporate data (even those with slick Windows-based GUIs) still use Telnet as the data transfer mechanism. Telnet is a clear text, unencrypted data transfer mechanism. A person with a packet sniffer can view this data as it crosses your network.
FTP logon data captured behind the FTP window is shown, showing the user’s password. Having your FTP password known allows the attacker to have your level of access to your FTP site, and any secret data that may be there; on top of that, many users who use the same password for all systems on the network. Now the attacker may have access to several of your corporate systems.
 
In addition to capturing cleartext sessions, such as login traffic, an attacker can have an application that captures only specific data from a network, such as network authentication packets, which she then reviews to crack network passwords.
If you are using switch-based network, you make packet sniffing a little tougher. On a switch-based network, the sniffer will see only data going to and from the sniffer’s own network device or broadcast traffic, unless the attacker uses a monitoring port on a switch. If you have not secured your switches and your switch configuration documentation with a strong password, you are leaving yourself open to a packet-sniffing attack.
A packet-sniffing attack on a switch-based network happens like this: The attacker connects to a switch and uses information from that switch to locate his own MAC address. The attacker locates his MAC address via show address-database, which lets him know what port the address is seen on.
The attacker can follow the path until he finds the switch to which he is connected. From there, the attacker can enable a monitor port as the port to which he connected. Now he can see all the traffic on that switch and can start a packet capture of data.

Although packet sniffers are tools of the trade for network engineers, they are also prevalent in some reputable antivirus software and as malware in nefarious email attachments.
Packet sniffers can gather almost any type of data. They can record passwords and login information, along with the websites visited by a computer user and what the user viewed while on the site. They can be used by companies to keep track of employee network use and scan incoming traffic for malicious code. In some cases, a packet sniffer can record all traffic on a network.


Aim)
   The aim to present a software to prevent users or customers to use weak password which can easily be BF.




Scope)
	My scope of this project is to provide a strong password which could not be easily be BF.

 We know how a packed can be captured and it can be decrypted by the different software to achieve the password for the different software, if the password is secure with special symbols which makes it had to decrypted in that case.
 
Packet sniffers or protocol analyzers are tools used by network technicians to diagnose network-related problems. Hackers use packet sniffers for less noble purposes, such as spying on network user traffic and collecting passwords.
Packet sniffers come in several forms. Some packet sniffers used by network technicians are single-purpose hardware solutions. In contrast, other packet sniffers are software applications that run on standard consumer-grade computers, using the network hardware provided on the host device to perform packet capture and injection tasks.




The algorithm used is:

1.	START
2.	That user input for the password
3.	If user input password is less than 8 it prints invalid password and jumps to step 6.
4.	If the password is more than 8, it checks weather its has condition of strong password.
5.	If it meets the condition for strong password it prints password is strong
6.	If it meets the condition for week password it prints week password.
7.	STOP.
