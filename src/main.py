"""Main entry point for stealth-browser-mcp package."""

# Import and run the server module
from server import *

if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(description="Stealth Browser MCP Server with 90 tools")
    parser.add_argument("--transport", choices=["stdio", "http"], default="stdio",
                      help="Transport protocol to use")
    parser.add_argument("--port", type=int, default=8000,
                      help="Port for HTTP transport")
    parser.add_argument("--host", default="0.0.0.0",
                      help="Host for HTTP transport")

    parser.add_argument("--disable-browser-management", action="store_true",
                      help="Disable browser management tools (spawn, navigate, close, etc.)")
    parser.add_argument("--disable-element-interaction", action="store_true",
                      help="Disable element interaction tools (click, type, scroll, etc.)")
    parser.add_argument("--disable-element-extraction", action="store_true",
                      help="Disable element extraction tools (styles, structure, events, etc.)")
    parser.add_argument("--disable-file-extraction", action="store_true",
                      help="Disable file-based extraction tools")
    parser.add_argument("--disable-network-debugging", action="store_true",
                      help="Disable network debugging and interception tools")
    parser.add_argument("--disable-cdp-functions", action="store_true",
                      help="Disable CDP function execution tools")
    parser.add_argument("--disable-progressive-cloning", action="store_true",
                      help="Disable progressive element cloning tools")
    parser.add_argument("--disable-cookies-storage", action="store_true",
                      help="Disable cookie and storage management tools")
    parser.add_argument("--disable-tabs", action="store_true",
                      help="Disable tab management tools")
    parser.add_argument("--disable-debugging", action="store_true",
                      help="Disable debug and system tools")
    parser.add_argument("--disable-dynamic-hooks", action="store_true",
                      help="Disable dynamic network hook system")

    parser.add_argument("--minimal", action="store_true",
                      help="Enable only core browser management and element interaction (disable everything else)")
    parser.add_argument("--list-sections", action="store_true",
                      help="List all available tool sections and exit")

    args = parser.parse_args()

    if args.list_sections:
        print("Available tool sections:")
        print("  browser-management: Core browser operations (11 tools)")
        print("  element-interaction: Page interaction and element manipulation (8 tools)")
        print("  element-extraction: Element cloning and extraction (10 tools)")
        print("  file-extraction: File-based extraction tools (9 tools)")
        print("  network-debugging: Network monitoring and interception (10 tools)")
        print("  cdp-functions: Chrome DevTools Protocol function execution (15 tools)")
        print("  progressive-cloning: Advanced element cloning system (10 tools)")
        print("  cookies-storage: Cookie and storage management (3 tools)")
        print("  tabs: Tab management (5 tools)")
        print("  debugging: Debug and system tools (6 tools)")
        print("  dynamic-hooks: AI-powered network hook system (12 tools)")
        print("\nUse --disable-<section-name> to disable specific sections")
        print("Use --minimal to enable only core functionality")
        sys.exit(0)

    # Import DISABLED_SECTIONS and update it based on arguments
    from server import DISABLED_SECTIONS, mcp

    if args.minimal:
        DISABLED_SECTIONS.update([
            "element-extraction", "file-extraction", "network-debugging",
            "cdp-functions", "progressive-cloning", "cookies-storage",
            "tabs", "debugging", "dynamic-hooks"
        ])

    if args.disable_browser_management:
        DISABLED_SECTIONS.add("browser-management")
    if args.disable_element_interaction:
        DISABLED_SECTIONS.add("element-interaction")
    if args.disable_element_extraction:
        DISABLED_SECTIONS.add("element-extraction")
    if args.disable_file_extraction:
        DISABLED_SECTIONS.add("file-extraction")
    if args.disable_network_debugging:
        DISABLED_SECTIONS.add("network-debugging")
    if args.disable_cdp_functions:
        DISABLED_SECTIONS.add("cdp-functions")
    if args.disable_progressive_cloning:
        DISABLED_SECTIONS.add("progressive-cloning")
    if args.disable_cookies_storage:
        DISABLED_SECTIONS.add("cookies-storage")
    if args.disable_tabs:
        DISABLED_SECTIONS.add("tabs")
    if args.disable_debugging:
        DISABLED_SECTIONS.add("debugging")
    if args.disable_dynamic_hooks:
        DISABLED_SECTIONS.add("dynamic-hooks")

    if DISABLED_SECTIONS:
        print(f"Disabled tool sections: {', '.join(sorted(DISABLED_SECTIONS))}", file=sys.stderr)

    if args.transport == "http":
        mcp.run(transport="http", host=args.host, port=args.port)
    else:
        mcp.run(transport="stdio")