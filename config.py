from environs import Env

env = Env()
env.read_env()

config = {
    "dashboard":{
        "url_link": env.str("url_link"), 
        "file": env.str("file_name")
        },
    "port": env.int("port")
    }
