import reflex as rx
from app.states.simulation_state import SimulationState


def sidebar_button(sim: dict) -> rx.Component:
    """A button for the sidebar to select a simulation."""
    return rx.el.button(
        rx.icon(sim["icon"], class_name="h-4 w-4 mr-3"),
        rx.el.span(sim["name"]),
        on_click=lambda: SimulationState.select_simulation(sim["id"]),
        class_name=rx.cond(
            SimulationState.selected_simulation_id == sim["id"],
            "w-full flex items-center px-3 py-2 text-sm font-medium rounded-lg bg-gray-700 text-white text-left",
            "w-full flex items-center px-3 py-2 text-sm font-medium rounded-lg text-gray-300 hover:bg-gray-700 hover:text-white text-left",
        ),
        width="100%",
    )


def sidebar() -> rx.Component:
    """The sidebar component for navigation."""
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.icon("shield-alert", class_name="h-8 w-8 text-white"),
                rx.el.h1("ThreatSim", class_name="text-2xl font-bold text-white"),
                class_name="flex items-center gap-3 p-4 border-b border-gray-700",
            ),
            rx.el.nav(
                rx.foreach(SimulationState.simulations, sidebar_button),
                class_name="flex flex-col gap-1 p-4",
            ),
            class_name="flex flex-col",
        ),
        class_name="fixed top-0 left-0 h-full w-80 bg-gray-800 border-r border-gray-700 z-10",
    )