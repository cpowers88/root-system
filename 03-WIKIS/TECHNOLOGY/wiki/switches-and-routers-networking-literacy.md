---
type: reference
timeline: reference
tags: [technology, networking]
created: 2026-08-11
---

# Switches and Routers — Networking Literacy

*Chris's own study notes, written from a networking-literacy source. Filed to the wiki
rather than `raw\` because this is his synthesis, not a captured source.*


So switches connect devices within a LAN and routers connect multiple LANs together.

### Switches

Operate within local area networks (LANs), directing traffic among devices.
- **Managed Switch** allows more advanced configurations, most notably, VLAN or virtual local area network support and some advanced security settings. Managed switch in terms of supporting things like VLANs has advanced software configuration capabilities, so that when you have many switches, you can define different VLANs using just the software configuration, which can isolate these computers from those computers, even though they're all connected into the same switches. 
- **Unmanaged Switch** is essentially just plug and play.
- **2 and 3 layer switches** this refers to the layers of the OSI model, and layer 2 is the data link layer, and layer 3 is the network layer. This is where the big **difference** in switches and routers come in as switches operate at layer 2.
- **Layer 2** in terms of addressing and managing traffic, uses MAC addresses or media access control.
So, switches facilitate communication amongst devices using their MAC address. Layer 3, which again is the network layer, uses IP addresses → where the routing happens.

 anywhere where there is a local area network, you need to have switches, and they're used to implement network segmentation and to reduce congestion, typically through the use of VLANs in more larger environments. But even in smaller environments, if you have multiple physical switches that are unmanaged and just very simple devices, you can still determine for yourself which systems should all be plugged into the same switches so that they make up local area network 1.

### Routers

Routers connect multiple networks and manage Internet traffic. Routers work entirely by IP addresses, but there are layer 3 switches, which in short means that a layer 3 switch can provide both switching and routing. You typically won't see a layer 3 switch used for very-high level routing, example → at Internet service providers, but within a smaller environments, they certainly can be used and are in home Internet routers.

Static routing and dynamic routing are the two types of routing. Dynamic routing can make routing decisions live. 

#### Types of Routers
- Home/small business routers: provide Wi-Fi, firewall and basic networking
- Enterprise routers: have advanced routing capabilities for high-performance networks
- Core routers: used in very large-scale Internet service provider networks for backbone connectivity. In short support the internet.

| Feature | Switch | Router |
| --- | --- | --- |
| Primary Role | Connect device within a LAN | Connects different networks |
| Layer | Operates Layer 2 (Data Link) or Layer 3 (Network) | Operates at Layer 3 (network) |
| Packet Forwarding | Uses MAC addresses | Uses IP addresses |
| Common Use Cases | LAN traffic management | Internet access and routing |



So switches connect devices within a LAN (computer to computer) and routers connect multiple LANs together (LAN to Internet service provider(ISP). 

Optimize their performance by configuring things like VLANs for network segmentation to control and manage traffic a little more effectively
 implement services such as quality of service, which can prioritize traffic based on the type. In other words, you can allocate more bandwidth to more demanding applications and less bandwidth to less demanding applications, and finally, monitor and maintain both types of devices using really any type of monitoring application. But there are specific protocols known as SNMP, Simple Network Management Protocol, and Syslog-based monitoring tools, which can gather up information from the devices and allow you to analyze their logs to see what's been going on, and be sure to update the firmware whenever possible.

