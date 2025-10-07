import reflex as rx
import html


class Comment(rx.Base):
    """Represents a single comment in the simulation."""

    content: str
    is_safe: bool


class XSSState(rx.State):
    """State for the XSS simulation."""

    comments: list[Comment] = []
    current_comment: str = ""
    is_vulnerable: bool = True

    @rx.event
    def toggle_vulnerability(self):
        """Toggles the vulnerable/secure mode."""
        self.is_vulnerable = not self.is_vulnerable

    @rx.event
    def add_comment(self):
        """Adds a comment to the list, applying sanitization if in secure mode."""
        if not self.current_comment.strip():
            return
        is_safe_render = not self.is_vulnerable
        new_comment = Comment(content=self.current_comment, is_safe=is_safe_render)
        self.comments.append(new_comment)
        self.current_comment = ""

    @rx.event
    def clear_comments(self):
        """Clears all comments from the display."""
        self.comments = []

    @rx.var
    def example_payload(self) -> str:
        """Provides an example XSS payload."""
        return "<script>alert('XSS Attack Successful!');</script>"