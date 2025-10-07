import reflex as rx
from typing import TypedDict, Optional


class Simulation(TypedDict):
    id: str
    name: str
    description: str
    category: str
    icon: str


class SimulationState(rx.State):
    """Manages the list of simulations and the currently selected one."""

    simulations: list[Simulation] = [
        {
            "id": "xss",
            "name": "Cross-Site Scripting (XSS)",
            "description": "Simulate how an attacker can inject malicious scripts into a web page, which then execute in the victim's browser.",
            "category": "Injection",
            "icon": "syringe",
        },
        {
            "id": "phishing",
            "name": "Phishing Attack",
            "description": "Simulate a phishing attempt to steal user credentials through a deceptive login form.",
            "category": "Social Engineering",
            "icon": "users",
        },
        {
            "id": "idor",
            "name": "Insecure Object Reference",
            "description": "Demonstrate how an attacker might access unauthorized data by manipulating object references like IDs in URLs.",
            "category": "Broken Access Control",
            "icon": "key-round",
        },
    ]
    selected_simulation_id: str = "xss"

    @rx.var
    def selected_simulation(self) -> Optional[Simulation]:
        """Returns the currently selected simulation dict."""
        for sim in self.simulations:
            if sim["id"] == self.selected_simulation_id:
                return sim
        return None

    @rx.event
    def select_simulation(self, sim_id: str):
        """Selects a simulation by its ID."""
        self.selected_simulation_id = sim_id