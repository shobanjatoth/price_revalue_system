# import sys
# import joblib
# import pandas as pd
# import numpy as np

# from src.utils.utils import load_yaml
# from src.logger.logger import get_logger
# from src.exceptions.exceptions import CustomException
# from src.components.feature_engineering import FeatureEngineering

# logger = get_logger(__name__)


# class InferencePipeline:

#     def __init__(self, config_path: str):
#         try:
#             self.config = load_yaml(config_path)
#             self.schema = load_yaml("config/schema.yaml")

#             self.model_path = self.config["artifacts"]["model_path"]
#             self.encoder_path = self.config["artifacts"]["encoder_path"]

#             self.model = joblib.load(self.model_path)
#             self.encoder = joblib.load(self.encoder_path)

#             # Reuse feature engineering
#             self.fe = FeatureEngineering(self.config, self.schema)

#         except Exception as e:
#             raise CustomException(str(e), sys)

#     # --------------------------------------------------
#     # Preprocessing
#     # --------------------------------------------------
#     def preprocess(self, input_df: pd.DataFrame):
#         try:
#             logger.info("Starting preprocessing for inference")

#             # Step 1: Feature engineering
#             df = self.fe.create_features(input_df)

#             # Step 2: Drop unwanted columns
#             df = df.drop(columns=["Price", "Price_log"], errors="ignore")

#             # 🚨 CRITICAL: Remove any raw text columns (safety)
#             # (handles Car_Name leakage issue)
#             df = df.drop(columns=["Car_Name", "car_name"], errors="ignore")

#             # Step 3: Handle categorical columns
#             categorical_cols = list(self.encoder.feature_names_in_)

#             # Ensure all expected categorical columns exist
#             for col in categorical_cols:
#                 if col not in df.columns:
#                     df[col] = "Unknown"

#             # Extract only categorical columns for encoding
#             df_cat = df[categorical_cols]

#             # Encode
#             encoded = self.encoder.transform(df_cat)

#             encoded_df = pd.DataFrame(
#                 encoded,
#                 columns=self.encoder.get_feature_names_out(categorical_cols),
#                 index=df.index
#             )

#             # Drop original categorical columns
#             df = df.drop(columns=categorical_cols)

#             # Combine numerical + encoded
#             df = pd.concat([df.reset_index(drop=True), encoded_df], axis=1)

#             # 🚨 FINAL SAFETY: ensure ONLY numeric data goes to model
#             df = df.select_dtypes(include=[np.number])

#             logger.info("Preprocessing completed")

#             return df

#         except Exception as e:
#             raise CustomException(str(e), sys)

#     # --------------------------------------------------
#     # Prediction
#     # --------------------------------------------------
#     def predict(self, input_df: pd.DataFrame):
#         try:
#             processed = self.preprocess(input_df)

#             # Predict (log scale)
#             preds_log = self.model.predict(processed)

#             # Convert back to actual price
#             preds = np.expm1(preds_log)

#             logger.info("Prediction completed")

#             return [round(p, 2) for p in preds]

#         except Exception as e:
#             raise CustomException(str(e), sys)

import sys
import joblib
import numpy as np
import pandas as pd

from src.utils.utils import load_yaml
from src.logger.logger import get_logger
from src.exceptions.exceptions import CustomException
from src.components.feature_engineering import (
    FeatureEngineering
)

logger = get_logger(__name__)


class InferencePipeline:

    def __init__(self, config_path: str):

        try:

            self.config = load_yaml(config_path)

            self.schema = load_yaml(
                "config/schema.yaml"
            )

            self.model_path = (
                self.config["artifacts"]["model_path"]
            )

            self.encoder_path = (
                self.config["artifacts"]["encoder_path"]
            )

            self.model = joblib.load(
                self.model_path
            )

            self.encoder = joblib.load(
                self.encoder_path
            )

            self.fe = FeatureEngineering(
                self.config,
                self.schema
            )

        except Exception as e:
            raise CustomException(str(e), sys)

    # ----------------------------------------------
    # PREPROCESS
    # ----------------------------------------------
    def preprocess(self, input_df):

        try:

            df = self.fe.clean_data(input_df)

            categorical_cols = list(
                self.encoder.feature_names_in_
            )

            for col in categorical_cols:

                if col not in df.columns:
                    df[col] = "Unknown"

            encoded = self.encoder.transform(
                df[categorical_cols]
            )

            encoded_df = pd.DataFrame(
                encoded,
                columns=self.encoder.get_feature_names_out(
                    categorical_cols
                ),
                index=df.index
            )

            df = df.drop(
                columns=categorical_cols
            )

            df = pd.concat(
                [df, encoded_df],
                axis=1
            )

            df = df.select_dtypes(
                include=[np.number]
            )

            return df

        except Exception as e:
            raise CustomException(str(e), sys)

    # ----------------------------------------------
    # PREDICT
    # ----------------------------------------------
    def predict(self, input_df):

        try:

            processed = self.preprocess(
                input_df
            )

            preds_log = self.model.predict(
                processed
            )

            preds = np.expm1(preds_log)

            return [
                round(float(p), 2)
                for p in preds
            ]

        except Exception as e:
            raise CustomException(str(e), sys)