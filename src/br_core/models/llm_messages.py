"""
LLM Messages Module
"""
import json
from abc import ABC
from typing import List, Optional, Dict, Any
from dataclasses import dataclass

class BaseLLMMessage(ABC):
    """Abstract base class for LLM messages."""

@dataclass
class SystemMessage(BaseLLMMessage):
    """System message containing instructions for the LLM."""
    content: str

@dataclass
class UserMessage(BaseLLMMessage):
    """User message containing text and optional images."""
    content: str
    images: Optional[List[str]] = None  # Base64 encoded images   

@dataclass
class ToolCall:
    """Represents a tool call made by the LLM."""
    id: str
    name: str
    arguments: Dict[str, Any]

@dataclass
class AIMessage(BaseLLMMessage):
    """AI response message with optional tool calls."""
    content: str
    tool_calls: Optional[List[ToolCall]] = None

@dataclass
class ToolResponseMessage(BaseLLMMessage):
    """Tool response message containing the result of a tool call."""
    id: str  # References the tool call ID
    content: str  # String content or JSON dump of dict response

    @classmethod
    def from_result(cls, tool_call_id: str, result: Dict[str, Any]) -> "ToolResponseMessage":
        """Create a ToolResponseMessage from a tool call result."""
        if isinstance(result, str):
            content = result
        else:
            content = json.dumps(result)
        return cls(id=tool_call_id, content=content)

