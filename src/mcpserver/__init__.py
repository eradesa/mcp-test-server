# mcpserver/__init__.py
from .deployment import register as register_deployment
from .prompt_server import register as register_prompts
from .resources import register as register_resources
from .local_Notes import register as register_local_Notes
from .local_DB import register as register_local_DB
from .vector_store import register as register_vector_store