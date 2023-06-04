import pynecone as pc

class MyappConfig(pc.Config):
    pass

config = MyappConfig(
    app_name="myapp01",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)