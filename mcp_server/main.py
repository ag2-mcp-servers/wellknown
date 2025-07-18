# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T12:12:52+00:00



import argparse
import json
import os
from typing import *

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity

app = MCPProxy(
    contact={
        'email': 'cfortuner@gmail.com',
        'name': 'Wellknown',
        'url': 'https://wellknown.ai',
    },
    description='A registry of AI Plugins.',
    title='Wellknown',
    version='1.0.0',
    servers=[{'url': 'https://wellknown.ai/api'}],
)


@app.get(
    '/api/plugins',
    description=""" Returns a list of Wellknown ai-plugins json objects from the Wellknown ai-plugins registry. """,
    tags=['api_plugin_management'],
)
def get_api_plugins():
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/plugins',
    description=""" List all the Wellknown AI Plugins. Returns ai-plugin.json objects in an array """,
    tags=['api_plugin_management'],
)
def get_provider():
    """
    List all the Wellknown AI Plugins.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
