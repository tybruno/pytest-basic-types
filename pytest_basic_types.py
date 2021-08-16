from dataclasses import dataclass, field
from typing import Iterable, Generator, Container, Mapping
from converters import IterableToGenerator
import pytest

iterable_to_generator = IterableToGenerator()


@dataclass
class MappingToContainers:
    container_types: Iterable

    def __call__(self, mapping: Mapping):
        dictionary = {dict: mapping}
        for container_type in self.container_types:

            dictionary[container_type] = container_type(
                iterable_to_generator(mapping.values())
            )
        return dictionary


@pytest.fixture
def basic_types():
    return {int: 1, float: 1.1, str: "string1"}


@pytest.fixture
def basic_types2():
    return {int: 2, float: 2.1, str: "string2"}


@pytest.fixture
def basic_containers(basic_types):
    mapping_to_container = MappingToContainers(
        container_types=(list, set, tuple)
    )
    basic_containers = mapping_to_container(basic_types)
    return basic_containers


@pytest.fixture
def basic_containers2(basic_types2):
    mapping_to_container = MappingToContainers(
        container_types=(list, set, tuple)
    )
    basic_containers2 = mapping_to_container(basic_types2)
    return basic_containers2
