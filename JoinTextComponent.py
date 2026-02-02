from lfx.custom.custom_component.component import Component
from lfx.io import HandleInput, Output
from lfx.schema.message import Message


class JoinTextComponent(Component):
    display_name: str = "Join Text"
    description: str = "Extracts the 'text' field from each input item and joins them with spaces."
    icon = "type"  # icon name can be anything valid in your build
    name: str = "JoinText"

    inputs = [
        HandleInput(
            name="data_inputs",
            display_name="Input",
            info="List of Data/Message-like items that have a .text property.",
            input_types=["Data", "DataFrame", "Message"],
            required=True,
        ),
    ]

    outputs = [
        Output(display_name="Joined Text", name="joined_text", method="join_text"),
    ]

    def join_text(self, data_inputs):
        # Defensive: data_inputs might be a single item or iterable
        if data_inputs is None:
            return Message(text="")

        # If the upstream gives a single object instead of a list
        items = data_inputs if isinstance(data_inputs, (list, tuple)) else [data_inputs]

        texts = []
        for item in items:
            # Most Langflow items expose `.text`
            t = getattr(item, "text", None)

            # Some objects may store text differently; add fallbacks if needed
            if not t and hasattr(item, "data") and isinstance(item.data, dict):
                t = item.data.get("text")

            if t:
                texts.append(str(t).strip())

        joined = " ".join(x for x in texts if x)
        return Message(text=joined)
