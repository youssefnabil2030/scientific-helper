import pytest
from science_experiment_helper import load_experiments, get_random_experiment, list_materials, save_favorite, load_favorites

# Sample data for tests
sample_experiment = {
    "name": "Volcano Eruption",
    "materials": ["baking soda", "vinegar", "food coloring"],
    "instructions": ["Add baking soda", "Add food coloring", "Pour vinegar"]
}

def test_load_experiments():
    experiments = load_experiments("experiments.csv")
    assert len(experiments) > 0

def test_get_random_experiment():
    experiments = [sample_experiment]
    experiment = get_random_experiment(experiments)
    assert experiment == sample_experiment

def test_list_materials():
    materials = list_materials(sample_experiment)
    assert materials == ["baking soda", "vinegar", "food coloring"]

def test_save_and_load_favorites(tmp_path):
    favorite_file = tmp_path / "favorites.txt"
    save_favorite(sample_experiment, filename=favorite_file)
    favorites = load_favorites(filename=favorite_file)
    assert sample_experiment["name"] in favorites
