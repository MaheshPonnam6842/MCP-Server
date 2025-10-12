from mcp.server.fastmcp import FastMCP
from bookings import book_cab, cancel_cab, get_driver_details

# Initialize the MCP server
mcp = FastMCP("cab_service")

# ✅ Register your tools using the latest FastMCP API
mcp.add_tool(book_cab, name="book_cab", description="Book a cab from pickup to dropoff")
mcp.add_tool(cancel_cab, name="cancel_cab", description="Cancel an existing cab booking")
mcp.add_tool(get_driver_details, name="get_driver_details", description="Get driver details for a booking")

if __name__ == "__main__":
    print("🚀 Starting Cab Service MCP Server (FastMCP latest API)...")
    mcp.run()
