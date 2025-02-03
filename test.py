from main import PyAPI, Model

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


if __name__ == "__main__":

    def print_data(data):
        for ind, item in enumerate(data):
            print(ind, item.__dict__, end="\n\n")

    # print_data(api.models)
    # print_data(api.tables)

# api.deploy()
