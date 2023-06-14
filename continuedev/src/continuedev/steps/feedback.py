from typing import Coroutine
from ..core.main import Models
from ..core.main import Step
from ..core.sdk import ContinueSDK
from ..libs.util.telemetry import capture_event


class FeedbackStep(Step):
    user_input: str
    name = "Thanks for your feedback!"

    async def describe(self, models: Models):
        return f"`{self.user_input}`\n\nWe'll see your feedback and make improvements as soon as possible. If you'd like to directly email us, you can send an email to [nate@continue.dev](mailto:nate@continue.dev?subject=Feedback%20On%20Continue)."

    async def run(self, sdk: ContinueSDK):
        capture_event("feedback", {"feedback": self.user_input})