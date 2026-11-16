import os
import json
import argparse
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

def format_telemetry_event(model: str, input_tokens: int, output_tokens: int, metadata_only: bool = True) -> dict:
    """Formats a standardized telemetry payload safe for observability pipelines."""
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "provider": "anthropic",
        "model": model,
        "usage": {
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": input_tokens + output_tokens,
        },
        "privacy_mode": "metadata_only" if metadata_only else "full",
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Claude Telemetry Formatter")
    parser.add_argument("--mode", default="metadata-only", choices=["metadata-only", "full"])
    args = parser.parse_args()

    sample_event = format_telemetry_event(
        model="claude-3-7-sonnet-latest",
        input_tokens=420,
        output_tokens=185,
        metadata_only=(args.mode == "metadata-only"),
    )
    print(json.dumps(sample_event, indent=2))
