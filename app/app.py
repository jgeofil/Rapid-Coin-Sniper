import reflex as rx
from app.states.simulation_state import SimulationState
from app.components.sidebar import sidebar
from app.components.simulations.xss_simulation import xss_simulation


def simulation_header() -> rx.Component:
    """Header for the main content area showing simulation details."""
    return rx.el.header(
        rx.cond(
            SimulationState.selected_simulation,
            rx.el.div(
                rx.el.h2(
                    SimulationState.selected_simulation["name"],
                    class_name="text-2xl font-bold text-gray-900",
                ),
                rx.el.p(
                    SimulationState.selected_simulation["description"],
                    class_name="text-sm text-gray-600 mt-1",
                ),
            ),
            rx.el.div(
                rx.el.h2(
                    "No Simulation Selected",
                    class_name="text-2xl font-bold text-gray-900",
                )
            ),
        ),
        class_name="p-6 border-b border-gray-200",
    )


def simulation_content() -> rx.Component:
    """The main content area where simulations are displayed."""
    return rx.el.div(
        simulation_header(),
        rx.match(
            SimulationState.selected_simulation_id,
            ("xss", xss_simulation()),
            rx.el.div(
                rx.el.p("Select a simulation from the sidebar to begin."),
                class_name="p-8 text-center text-gray-500",
            ),
        ),
    )


def index() -> rx.Component:
    """The main page of the threat simulation platform."""
    return rx.el.div(
        sidebar(),
        rx.el.main(simulation_content(), class_name="ml-80"),
        class_name="font-['Inter'] bg-gray-50 min-h-screen",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)