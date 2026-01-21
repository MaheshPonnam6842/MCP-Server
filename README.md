

A lightweight **Model Context Protocol (MCP)** server that powers MakeYourTrip’s next-gen **Cab Service Platform**.  
This project combines **Google Maps** and a custom **Cab Booking** system to help users plan trips, explore routes, and book rides — all through natural conversation with tools like **Claude Desktop**.

---

## 🧠 Overview

The Cab Service MCP acts as the cab-management layer in a travel-planning assistant.  
It connects with a pre-built **Google Maps MCP** to understand routes, estimate travel times, and help users move efficiently between destinations.

With this server running, you can:

- 🏙️ **Book cabs** to any destination  
- ❌ **Cancel bookings** when plans change  
- 🚗 **View driver details** for confirmed rides  
- 🗺️ **Combine it with Google Maps MCP** to plan full itineraries automatically  

Example natural-language prompts you can use inside Claude Desktop:  
> “Plan an 8-hour trip from Vadodara to Ahmedabad with 3 must-visit places and book the cabs.”  
> “I’m visiting Delhi for the weekend — create a sightseeing route and arrange rides between landmarks.”  
> “Find the best street-food spots in Lucknow and book cabs between them.”

---

## 🧩 How It Works

Claude (or any MCP-compatible LLM) communicates with two servers:

```
Claude / LLM
│
├── Google Maps MCP → Handles routes, ETA, and destinations  
└── Cab Service MCP → Handles cab booking, cancellation, and driver info
```

Together, they make your AI assistant capable of real-time travel planning and booking.



