# import sys
# import joblib
# import mlflow
# import mlflow.sklearn
# from xgboost import XGBRegressor
# from logger.logger import get_logger
# from exceptions.exceptions import CustomException

# logger = get_logger(__name__)


# class ModelTrainer:

#     def __init__(self, config):
#         self.config = config
#         self.model_path = config["model"]["model_path"]
#         self.n_estimators = config["training"]["n_estimators"]
#         self.max_depth = config["training"]["max_depth"]

#     def train(self, X_train, y_train):

#         try:
#             model =  XGBRegressor(
#                 n_estimators=self.n_estimators,
#                 max_depth=self.max_depth,
#                 random_state=self.config["training"]["random_state"]
#             )



#             model.fit(X_train, y_train)

#             joblib.dump(model, self.model_path)
#             logger.info("Model training completed")

#             return model

#         except Exception as e:
#             logger.error(e)
#             raise CustomException(str(e), sys)

# import sys
# import os
# import joblib
# from xgboost import XGBRegressor
# from logger.logger import get_logger
# from exceptions.exceptions import CustomException

# logger = get_logger(__name__)


# class ModelTrainer:

#     def __init__(self, config):
#         try:
#             self.config = config

#             self.model_path = config["model"]["model_path"]
#             training_config = config["training"]

#             # Extract all XGBoost params
#             self.params = {
#                 "objective": training_config["objective"],
#                 "n_estimators": training_config["n_estimators"],
#                 "max_depth": training_config["max_depth"],
#                 "learning_rate": training_config["learning_rate"],
#                 "subsample": training_config["subsample"],
#                 "colsample_bytree": training_config["colsample_bytree"],
#                 "reg_lambda": training_config["reg_lambda"],
#                 "reg_alpha": training_config["reg_alpha"],
#                 "min_child_weight": training_config["min_child_weight"],
#                 "random_state": training_config["random_state"]
#             }

#             os.makedirs(os.path.dirname(self.model_path), exist_ok=True)

#             logger.info("ModelTrainer initialized successfully")

#         except Exception as e:
#             raise CustomException(str(e), sys)

#     # --------------------------------------------------
#     # Training
#     # --------------------------------------------------
#     def train(self, X_train, y_train):
#         try:
#             logger.info("Model training started")

#             # Initialize model with all parameters
#             model = XGBRegressor(**self.params)

#             # Train model
#             model.fit(X_train, y_train)

#             # Save model
#             joblib.dump(model, self.model_path)

#             logger.info("Model training completed successfully")

#             return model

#         except Exception as e:
#             logger.error(e)
#             raise CustomException(str(e), sys)


# import sys
# import os
# import joblib
# from xgboost import XGBRegressor

# from src.logger.logger import get_logger
# from src.exceptions.exceptions import CustomException

# logger = get_logger(__name__)


# class ModelTrainer:

#     def __init__(self, config):
#         self.config = config

#         self.model_path = config["artifacts"]["model_path"]
#         training_config = config["training"]

#         self.params = training_config

#         os.makedirs(os.path.dirname(self.model_path), exist_ok=True)

#     def train(self, X_train, y_train):
#         try:
#             model = XGBRegressor(**self.params)
#             model.fit(X_train, y_train)

#             joblib.dump(model, self.model_path)

#             logger.info("Model training completed")

#             return model

#         except Exception as e:
#             raise CustomException(str(e), sys)


import sys
import os
import joblib

from xgboost import XGBRegressor

from src.logger.logger import get_logger
from src.exceptions.exceptions import CustomException

logger = get_logger(__name__)


class ModelTrainer:

    def __init__(self, config):

        self.config = config

        self.model_path = (
            config["artifacts"]["model_path"]
        )

        training_config = config["training"]

        # Remove unsupported params
        self.params = {
            k: v
            for k, v in training_config.items()
            if k != "log_target"
        }

        os.makedirs(
            os.path.dirname(self.model_path),
            exist_ok=True
        )

    def train(self, X_train, y_train):

        try:

            model = XGBRegressor(
                **self.params
            )

            model.fit(
                X_train,
                y_train
            )

            joblib.dump(
                model,
                self.model_path
            )

            logger.info(
                "Model training completed"
            )

            return model

        except Exception as e:
            raise CustomException(str(e), sys)