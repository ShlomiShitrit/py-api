from main import PyAPI

api = PyAPI()

api.load_model("data/pokemon.csv")
api.load_model("data/trainer.csv")

print(api.models)

api.deploy()
