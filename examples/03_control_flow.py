"""
Example 3: Control Flow with Loops

Demonstrates using native Python control flow (loops, conditionals)
to handle complex workflows.

Key benefit: Eliminates the need for complex multi-step tool orchestration.
Without code execution, this would require multiple rounds of model inference.
"""

import asyncio
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from servers import slack


async def wait_for_deployment():
    """
    Poll a Slack channel until a deployment completion message appears.

    Without code execution:
    - Step 1: Call slack.get_channel_history()
    - Step 2: Model checks messages
    - Step 3: Model decides to wait
    - Step 4: Repeat from step 1
    - Requires multiple model inference rounds

    With code execution:
    - Single code block with loop
    - Model inference only needed once
    - Much faster and more efficient
    """
    print("Example 3: Control Flow with Loops")
    print("=" * 60)
    print()

    print("Waiting for deployment notification in Slack channel...")
    print()

    # In a real implementation, we'd actually poll
    # For this demo, we'll simulate the final check
    attempt = 0
    max_attempts = 1  # For demo purposes

    found = False
    while not found and attempt < max_attempts:
        attempt += 1
        print(f"Checking channel (attempt {attempt})...")

        # Get recent messages from the deployment channel
        result = await slack.get_channel_history({'channel': 'C123456'})
        messages = result['messages']

        # Check if any message contains the completion signal
        found = any('deployment complete' in msg['text'] for msg in messages)

        if found:
            print("✓ Deployment notification received!")
            print()
            print("Recent messages:")
            for msg in messages:
                print(f"  - {msg['text']}")
        else:
            print("  No deployment notification yet, waiting...")
            await asyncio.sleep(1)  # Would be 5 seconds in real implementation

    print()
    print("Key insight: This entire polling loop runs in one execution.")
    print("Without code execution, each check would require a separate")
    print("model inference call, making it much slower and more expensive.")


if __name__ == '__main__':
    asyncio.run(wait_for_deployment())
