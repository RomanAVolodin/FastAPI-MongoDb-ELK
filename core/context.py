from contextvars import ContextVar

ctx_request_id: ContextVar[str] = ContextVar('request_id')
