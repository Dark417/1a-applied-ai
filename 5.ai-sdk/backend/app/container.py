"""Composition root: the only place that wires settings -> providers -> registry -> service."""

from dataclasses import dataclass

from app.config import Settings, get_settings
from app.core.registry import AdapterRegistry
from app.core.sessions import SessionRegistry
from app.providers import build_profiles
from app.providers.profile import ProviderProfile
from app.services.run_service import RunService


@dataclass
class Container:
    settings: Settings
    providers: dict[str, ProviderProfile]
    registry: AdapterRegistry
    sessions: SessionRegistry
    runs: RunService


def build_container(
    settings: Settings | None = None, *, adapter_specs: dict[str, str] | None = None
) -> Container:
    settings = settings or get_settings()
    providers = build_profiles(settings)
    registry = AdapterRegistry(settings, adapter_specs)
    sessions = SessionRegistry()
    runs = RunService(registry, providers, sessions, settings)
    return Container(settings, providers, registry, sessions, runs)
