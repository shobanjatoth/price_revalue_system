# import sys
# import mlflow
# from utils.utils import load_yaml
# from components.data_ingestion import DataIngestion
# from components.data_validation import DataValidation
# from components.feature_engineering import FeatureEngineering
# from components.model_trainer import ModelTrainer
# from components.model_evaluation import ModelEvaluation
# from logger.logger import get_logger
# from exceptions.exceptions import CustomException

# logger = get_logger(__name__)


# class TrainingPipeline:

#     def __init__(self):
#         self.config = load_yaml("config/config.yaml")
#         self.schema = load_yaml("config/schema.yaml")

#     def run(self):

#         try:
#             logger.info("Training pipeline started")

#             # 1️⃣ Ingestion
#             ingestion = DataIngestion(self.config)
#             df = ingestion.load_data()

#             # 2️⃣ Validation
#             validator = DataValidation(
#                 self.schema,
#                 "artifacts/validation_report.json"
#             )

#             if not validator.validate(df):
#                 raise Exception("Data validation failed")

#             # 3️⃣ Split
#             train_df, test_df = ingestion.split_data(
#                 df,
#                 self.schema["target_column"]
#             )

#             # 4️⃣ Feature Engineering
#             fe = FeatureEngineering(self.schema)

#             X_train, X_test, y_train, y_test = fe.process(
#                 train_df,
#                 test_df
#             )

#             # 5️⃣ MLflow
#             mlflow.set_experiment(
#                 self.config["mlflow"]["experiment_name"]
#             )

#             with mlflow.start_run():

#                 # 6️⃣ Train
#                 trainer = ModelTrainer(self.config)
#                 model = trainer.train(X_train, y_train)

#                 mlflow.log_params(self.config["training"])

#                 # 7️⃣ Evaluate
#                 evaluator = ModelEvaluation(self.config)
#                 metrics = evaluator.evaluate(model, X_test, y_test)

#                 mlflow.log_metrics(metrics)

#                 mlflow.sklearn.log_model(
#                     model,
#                     artifact_path="model",
#                     registered_model_name=self.config["mlflow"]["registered_model_name"]
#                 )

#             logger.info("Training pipeline completed successfully")

#         except Exception as e:
#             logger.error(e)
#             raise CustomException(str(e), sys)

# import sys
# import mlflow
# import mlflow.xgboost
# from utils.utils import load_yaml
# from components.data_ingestion import DataIngestion
# from components.data_validation import DataValidation
# from components.feature_engineering import FeatureEngineering
# from components.model_trainer import ModelTrainer
# from components.model_evaluation import ModelEvaluation
# from logger.logger import get_logger
# from exceptions.exceptions import CustomException

# logger = get_logger(__name__)


# class TrainingPipeline:

#     def __init__(self):
#         self.config = load_yaml("config/config.yaml")
#         self.schema = load_yaml("config/schema.yaml")

#     def run(self):

#         try:
#             logger.info("Training pipeline started")

#             # 1️⃣ Ingestion
#             ingestion = DataIngestion(self.config)
#             df = ingestion.load_data()

#             # 2️⃣ Validation
#             validator = DataValidation(
#                 self.schema,
#                 "artifacts/validation_report.json"
#             )

#             if not validator.validate(df):
#                 raise Exception("Data validation failed")

#             # 3️⃣ Split
#             train_df, test_df = ingestion.split_data(
#                 df,
#                 self.schema["target_column"]
#             )

#             # 4️⃣ Feature Engineering
#             fe = FeatureEngineering(self.schema)

#             X_train, X_test, y_train, y_test = fe.process(
#                 train_df,
#                 test_df
#             )

#             # 5️⃣ MLflow Setup
#             mlflow.set_experiment(
#                 self.config["mlflow"]["experiment_name"]
#             )

#             with mlflow.start_run(run_name="xgboost_car_price"):

#                 # 6️⃣ Train
#                 trainer = ModelTrainer(self.config)
#                 model = trainer.train(X_train, y_train)

#                 # Log important params only
#                 mlflow.log_params({
#                     "n_estimators": self.config["training"]["n_estimators"],
#                     "max_depth": self.config["training"]["max_depth"],
#                     "learning_rate": self.config["training"]["learning_rate"],
#                 })

#                 # 7️⃣ Evaluate
#                 evaluator = ModelEvaluation(self.config)
#                 metrics = evaluator.evaluate(model, X_test, y_test)

#                 mlflow.log_metrics(metrics)

#                 # Optional: Fail if model is weak
#                 if metrics["r2_score"] < 0.7:
#                     raise Exception("Model performance is too low")

#                 # 8️⃣ Log model (correct for XGBoost)
#                 mlflow.xgboost.log_model(
#                     model,
#                     artifact_path="model",
#                     registered_model_name=self.config["mlflow"]["registered_model_name"]
#                 )

#             logger.info("Training pipeline completed successfully")

#         except Exception as e:
#             logger.error(e)
#             raise CustomException(str(e), sys)



import sys
import mlflow
import mlflow.sklearn

from src.utils.utils import load_yaml
from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.feature_engineering import FeatureEngineering
from src.components.model_trainer import ModelTrainer
from src.components.model_evaluation import ModelEvaluation
from src.logger.logger import get_logger
from src.exceptions.exceptions import CustomException

logger = get_logger(__name__)


class TrainingPipeline:

    def __init__(self, config_path: str, schema_path: str):
        try:
            self.config = load_yaml(config_path)
            self.schema = load_yaml(schema_path)

        except Exception as e:
            raise CustomException(str(e), sys)

    def run_pipeline(self):
        try:
            logger.info("Training Pipeline started")

            # -------------------------------
            # Data Ingestion
            # -------------------------------
            ingestion = DataIngestion(self.config)
            df = ingestion.load_data()

            # -------------------------------
            # Data Validation
            # -------------------------------
            validator = DataValidation(
                self.schema,
                report_path="artifacts/validation_report.json"
            )

            status = validator.validate(df)

            if not status:
                raise Exception("Data validation failed. Check report.")

            # -------------------------------
            # Split Data
            # -------------------------------
            train_df, test_df = ingestion.split_data(
                df,
                target_column="Price"
            )

            # -------------------------------
            # Feature Engineering
            # -------------------------------
            fe = FeatureEngineering(self.config, self.schema)

            X_train, X_test, y_train, y_test = fe.process(
                train_df, test_df
            )

            # -------------------------------
            # MLflow Setup
            # -------------------------------
            mlflow.set_experiment(
                self.config["mlflow"]["experiment_name"]
            )

            with mlflow.start_run():

                # -------------------------------
                # Model Training
                # -------------------------------
                trainer = ModelTrainer(self.config)
                model = trainer.train(X_train, y_train)

                # -------------------------------
                # Model Evaluation
                # -------------------------------
                evaluator = ModelEvaluation(self.config)
                metrics = evaluator.evaluate(model, X_test, y_test)

                # -------------------------------
                # Log params
                # -------------------------------
                mlflow.log_params(self.config["training"])

                # -------------------------------
                # Log metrics
                # -------------------------------
                mlflow.log_metrics(metrics)

                # -------------------------------
                # Log model + REGISTER
                # -------------------------------
                mlflow.sklearn.log_model(
                    sk_model=model,
                    name="model",
                    registered_model_name=self.config["mlflow"]["registered_model_name"]
                )

            logger.info("Training Pipeline completed successfully")

        except Exception as e:
            logger.error(e)
            raise CustomException(str(e), sys)
