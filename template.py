import os
from pathlib import Path

proj_name = "src"

list_of_files = [

    f"{proj_name}/__init__.py",
    f"{proj_name}/components/__init__.py",
    f"{proj_name}/components/data_ingestion.py",  
    f"{proj_name}/components/data_validation.py",
    f"{proj_name}/components/data_transformation.py",
    f"{proj_name}/components/model_trainer.py",
    f"{proj_name}/components/model_evaluation.py",
    f"{proj_name}/components/model_pusher.py",
    f"{proj_name}/configuration/__init__.py",
    f"{proj_name}/configuration/mongo_db_connection.py",
    f"{proj_name}/configuration/aws_connection.py",
    f"{proj_name}/cloud_storage/__init__.py",
    f"{proj_name}/cloud_storage/aws_storage.py",
    f"{proj_name}/data_access/__init__.py",
    f"{proj_name}/data_access/proj1_data.py",
    f"{proj_name}/constants/__init__.py",
    f"{proj_name}/entity/__init__.py",
    f"{proj_name}/entity/config_entity.py",
    f"{proj_name}/entity/artifact_entity.py",
    f"{proj_name}/entity/estimator.py",
    f"{proj_name}/entity/s3_estimator.py",
    f"{proj_name}/exception/__init__.py",
    f"{proj_name}/logger/__init__.py",
    f"{proj_name}/pipline/__init__.py",
    f"{proj_name}/pipline/training_pipeline.py",
    f"{proj_name}/pipline/prediction_pipeline.py",
    f"{proj_name}/utils/__init__.py",
    f"{proj_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")