# 🐍 py-api

**py-api** is a lightweight and flexible Python library designed to make building and running APIs with [FastAPI](https://fastapi.tiangolo.com/) easier than ever. Whether you're uploading models manually or from CSV files, `py-api` helps you get your API up and running in just a few lines of code.

---

## 🚀 Features

- 📦 Simple model loading – define your models manually or from a CSV file
- ⚡ Fast and async – powered by **FastAPI**
- 🛠️ Auto-generates CRUD endpoints for your data
- 🧪 Built-in support for validation and response models
- 🐳 Easy to integrate with Docker or other deployment setups

## 🧠 Usage
```python
from pyapi import PyAPI, Model

# create an instance of PyAPI
api = PyAPI()

# create Models
pokemon_model = Model()
trainer_model = Model()

# load data from csv files to models
pokemon_model.load_model_from_file(file_path="data/pokemon.csv", name="pokemon")
trainer_model.load_model_from_file(file_path="data/trainer.csv", name="trainer")

# set primary key, unique columns, and foreign key
pokemon_model.set_primary_key("id")
trainer_model.set_primary_key("id")

pokemon_model.set_unique("name")
trainer_model.set_unique("name")

trainer_model.set_foreign_key("pokemon_id", pokemon_model)

# load models to PyAPI
api.load_model(pokemon_model)
api.load_model(trainer_model)

# run the API
api.deploy()
```
