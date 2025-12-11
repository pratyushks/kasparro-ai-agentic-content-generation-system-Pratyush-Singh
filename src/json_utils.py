import json
from typing import Any, Dict

class LLMJsonError(RuntimeError):
    pass


def extract_json_object(text: str) -> Dict[str, Any]:
    if not text or not text.strip():
        raise LLMJsonError("Empty response from LLM, cannot parse JSON.")

    # Remove common code fence wrappers
    stripped = text.strip()
    if stripped.startswith("```"):
        # remove ```json or ``` and ending ```
        stripped = stripped.strip("`")
        # sometimes: json\n{...}
        if "{" in stripped:
            stripped = stripped[stripped.find("{") :]

    # Find outermost JSON object
    start = stripped.find("{")
    end = stripped.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise LLMJsonError(
            f"Could not find JSON object in LLM response. Raw response:\n{stripped[:500]}"
        )

    candidate = stripped[start : end + 1]

    try:
        return json.loads(candidate)
    except json.JSONDecodeError as e:
        raise LLMJsonError(
            f"Failed to parse JSON from LLM response. "
            f"Slice that failed:\n{candidate[:500]}"
        ) from e