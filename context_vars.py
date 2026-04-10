"""MCP context variables — shared across bridge and tool handlers.

Extracted so modules like src/orchestration/task_board.py can read the current
session_id without importing vetka_mcp_bridge (which would cause a cycle).

MARKER_PHASE8O.CONTEXT_VARS: session-scoped exhaustion counter infrastructure.
"""

import contextvars

# Current session_id for the in-flight MCP tool call.
# - Set once per bridge process in init_client() (src/mcp/vetka_mcp_bridge.py).
# - Read by task_board.complete_task() to look up SessionActionTracker counter.
# - Default "default" keeps legacy behavior when no session is attached.
session_context: contextvars.ContextVar[str] = contextvars.ContextVar(
    "session_id", default="default"
)
