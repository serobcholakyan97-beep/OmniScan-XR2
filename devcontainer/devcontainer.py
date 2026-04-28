{

    "name": "OmniScan-XR Cloud Core",

    "image": "mcr.microsoft.com/devcontainers/python:3.10",

    "customizations": {

        "vscode": {

            "extensions": [

                "ms-python.python",

                "ms-azuretools.vscode-docker"

            ]

        }

    },

    "postCreateCommand": "pip install -r requirements.txt",

    "remoteEnv": {

        "LOCAL_BACKEND_URL": "http://localhost:5001"

    }

}
