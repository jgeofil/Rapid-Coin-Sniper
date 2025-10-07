import reflex as rx
from app.states.xss_state import XSSState


def comment_display(comment: rx.Var[dict]) -> rx.Component:
    """Displays a single comment, rendering it safely or unsafely."""
    return rx.el.div(
        rx.el.div(
            rx.el.p("Anonymous", class_name="font-semibold text-sm text-gray-800"),
            rx.el.p("Just now", class_name="text-xs text-gray-500"),
            class_name="flex items-center justify-between",
        ),
        rx.cond(
            comment["is_safe"],
            rx.el.p(comment["content"], class_name="mt-2 text-sm text-gray-700"),
            rx.html(comment["content"]),
        ),
        class_name="p-4 bg-white rounded-lg border border-gray-200",
    )


def xss_simulation() -> rx.Component:
    """The UI for the XSS simulation."""
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Simulation Controls", class_name="text-lg font-semibold text-gray-800"
            ),
            rx.el.p(
                "Toggle between Vulnerable and Secure modes to see the effect of input sanitization.",
                class_name="text-sm text-gray-600 mt-1",
            ),
            rx.el.div(
                rx.el.label("Mode:", class_name="font-medium text-gray-700"),
                rx.el.div(
                    rx.el.button(
                        rx.icon("shield-off", class_name="mr-2 h-4 w-4"),
                        "Vulnerable",
                        on_click=XSSState.toggle_vulnerability,
                        class_name=rx.cond(
                            XSSState.is_vulnerable,
                            "flex items-center px-4 py-2 text-sm font-medium text-white bg-red-600 rounded-l-lg hover:bg-red-700 focus:z-10 focus:ring-2 focus:ring-red-500",
                            "flex items-center px-4 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-l-lg hover:bg-gray-100 hover:text-red-700 focus:z-10 focus:ring-2 focus:ring-red-500",
                        ),
                    ),
                    rx.el.button(
                        rx.icon("shield-check", class_name="mr-2 h-4 w-4"),
                        "Secure",
                        on_click=XSSState.toggle_vulnerability,
                        class_name=rx.cond(
                            ~XSSState.is_vulnerable,
                            "flex items-center px-4 py-2 text-sm font-medium text-white bg-green-600 rounded-r-lg hover:bg-green-700 focus:z-10 focus:ring-2 focus:ring-green-500",
                            "flex items-center px-4 py-2 text-sm font-medium text-gray-900 bg-white border border-gray-200 rounded-r-lg hover:bg-gray-100 hover:text-green-700 focus:z-10 focus:ring-2 focus:ring-green-500",
                        ),
                    ),
                    class_name="inline-flex rounded-md shadow-sm mt-2",
                ),
                class_name="mt-4",
            ),
        ),
        rx.el.div(
            rx.el.textarea(
                placeholder="Leave a comment... try the payload below!",
                on_change=XSSState.set_current_comment,
                class_name="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500",
                rows=3,
                default_value=XSSState.current_comment,
            ),
            rx.el.div(
                rx.el.p(
                    "Example Payload:", class_name="text-xs font-mono text-gray-500"
                ),
                rx.el.code(
                    XSSState.example_payload,
                    class_name="text-xs text-red-600 bg-gray-100 p-1 rounded",
                ),
                class_name="mt-2",
            ),
            rx.el.div(
                rx.el.button(
                    "Post Comment",
                    on_click=XSSState.add_comment,
                    class_name="px-4 py-2 bg-blue-600 text-white font-semibold rounded-lg hover:bg-blue-700",
                ),
                rx.el.button(
                    "Clear Comments",
                    on_click=XSSState.clear_comments,
                    class_name="px-4 py-2 bg-gray-200 text-gray-700 font-semibold rounded-lg hover:bg-gray-300",
                ),
                class_name="flex justify-between mt-2",
            ),
            class_name="mt-6",
        ),
        rx.el.div(
            rx.el.h4(
                "Comment Section", class_name="text-md font-semibold text-gray-800 mb-4"
            ),
            rx.el.div(
                rx.foreach(XSSState.comments, comment_display), class_name="space-y-4"
            ),
            class_name="mt-8 p-6 bg-gray-100 rounded-lg",
        ),
        class_name="p-8",
    )