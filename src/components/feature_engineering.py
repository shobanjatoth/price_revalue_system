# import sys
# import os
# import pandas as pd
# import joblib

# from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# from src.logger.logger import get_logger
# from src.exceptions.exceptions import CustomException

# logger = get_logger(__name__)


# class FeatureEngineering:

#     def __init__(self, config, schema):
#         try:
#             self.config = config
#             self.schema = schema

#             self.target_column = schema["target_column"]

#             self.encoder_path = config["artifacts"]["encoder_path"]
#             self.train_processed_path = config["artifacts"]["train_processed_path"]
#             self.test_processed_path = config["artifacts"]["test_processed_path"]

#             os.makedirs(os.path.dirname(self.encoder_path), exist_ok=True)

#         except Exception as e:
#             raise CustomException(str(e), sys)

#     # -----------------------------------
#     # Step 1: Cleaning
#     # -----------------------------------
#     def clean_data(self, df):
#         try:
#             df = df.copy()

#             # Remove invalid values
#             if "Age_Oldest_TL" in df.columns:
#                 df = df[df["Age_Oldest_TL"] != -99999]

#             # Remove columns with too many -99999
#             columns_to_remove = []
#             for col in df.columns:
#                 if (df[col] == -99999).sum() > 10000:
#                     columns_to_remove.append(col)

#             df.drop(columns=columns_to_remove, inplace=True, errors="ignore")

#             # Remove duplicates
#             df.drop_duplicates(inplace=True)

#             logger.info(f"Removed columns: {columns_to_remove}")

#             return df

#         except Exception as e:
#             raise CustomException(str(e), sys)

#     # -----------------------------------
#     # Step 2: Encoding
#     # -----------------------------------
#     def encode(self, X_train, X_test, y_train, y_test):
#         try:
#             # -------- EDUCATION mapping --------
#             education_map = {
#                 'SSC': 1,
#                 '12TH': 2,
#                 'GRADUATE': 3,
#                 'UNDER GRADUATE': 3,
#                 'POST-GRADUATE': 4,
#                 'OTHERS': 1,
#                 'PROFESSIONAL': 3
#             }

#             if "EDUCATION" in X_train.columns:
#                 X_train["EDUCATION"] = X_train["EDUCATION"].map(education_map).fillna(0)
#                 X_test["EDUCATION"] = X_test["EDUCATION"].map(education_map).fillna(0)

#             # -------- OneHot --------
#             cols = ['MARITALSTATUS', 'GENDER', 'last_prod_enq2', 'first_prod_enq2']
#             cols = [c for c in cols if c in X_train.columns]

#             encoder = OneHotEncoder(
#                 drop='first',
#                 sparse_output=False,
#                 handle_unknown='ignore'
#             )

#             encoder.fit(X_train[cols])

#             train_encoded = encoder.transform(X_train[cols])
#             test_encoded = encoder.transform(X_test[cols])

#             encoded_cols = encoder.get_feature_names_out(cols)

#             train_df = pd.DataFrame(train_encoded, columns=encoded_cols, index=X_train.index)
#             test_df = pd.DataFrame(test_encoded, columns=encoded_cols, index=X_test.index)

#             X_train = X_train.drop(columns=cols)
#             X_test = X_test.drop(columns=cols)

#             X_train = pd.concat([X_train, train_df], axis=1)
#             X_test = pd.concat([X_test, test_df], axis=1)

#             # -------- Label Encode Target --------
#             label_encoder = LabelEncoder()
#             y_train = label_encoder.fit_transform(y_train)
#             y_test = label_encoder.transform(y_test)

#             # Save encoder
#             joblib.dump(encoder, self.encoder_path)

#             return X_train, X_test, y_train, y_test

#         except Exception as e:
#             raise CustomException(str(e), sys)

#     # -----------------------------------
#     # Main Pipeline
#     # -----------------------------------
#     def process(self, train_df, test_df):
#         try:
#             logger.info("Feature Engineering Started")

#             train_df = self.clean_data(train_df)
#             test_df = self.clean_data(test_df)

#             # Split X & y
#             y_train = train_df[self.target_column]
#             y_test = test_df[self.target_column]

#             X_train = train_df.drop(columns=[self.target_column])
#             X_test = test_df.drop(columns=[self.target_column])

#             # Encode
#             X_train, X_test, y_train, y_test = self.encode(
#                 X_train, X_test, y_train, y_test
#             )

#             # Save processed data
#             X_train.to_csv(self.train_processed_path, index=False)
#             X_test.to_csv(self.test_processed_path, index=False)

#             logger.info("Feature Engineering Completed")

#             return X_train, X_test, y_train, y_test

#         except Exception as e:
#             raise CustomException(str(e), sys)



import sys
import os
import joblib
import numpy as np
import pandas as pd

from sklearn.preprocessing import OneHotEncoder

from src.logger.logger import get_logger
from src.exceptions.exceptions import CustomException

logger = get_logger(__name__)


class FeatureEngineering:

    def __init__(self, config, schema):

        self.config = config
        self.schema = schema

        self.target_column = schema["target_column"]

        self.encoder_path = config["artifacts"]["encoder_path"]

        self.train_processed_path = (
            config["artifacts"]["train_processed_path"]
        )

        self.test_processed_path = (
            config["artifacts"]["test_processed_path"]
        )

        os.makedirs(
            os.path.dirname(self.encoder_path),
            exist_ok=True
        )

    # ------------------------------------------------
    # CLEANING
    # ------------------------------------------------
    def clean_data(self, df):

        try:

            df = df.copy()

            # Remove duplicates
            df.drop_duplicates(inplace=True)

            # Fill missing values
            categorical_cols = [
                "Car Name",
                "Fuel",
                "Location",
                "Drive",
                "Type"
            ]

            numerical_cols = [
                "Year",
                "Distance",
                "Owner"
            ]

            for col in categorical_cols:
                if col in df.columns:
                    df[col] = df[col].fillna("Unknown")

            for col in numerical_cols:
                if col in df.columns:
                    df[col] = df[col].fillna(df[col].median())

            logger.info("Data cleaning completed")

            return df

        except Exception as e:
            raise CustomException(str(e), sys)

    # ------------------------------------------------
    # ENCODING
    # ------------------------------------------------
    def encode(
        self,
        X_train,
        X_test,
        y_train,
        y_test
    ):

        try:

            categorical_cols = [
                "Car Name",
                "Fuel",
                "Location",
                "Drive",
                "Type"
            ]

            categorical_cols = [
                col for col in categorical_cols
                if col in X_train.columns
            ]

            encoder = OneHotEncoder(
                handle_unknown="ignore",
                sparse_output=False
            )

            encoder.fit(X_train[categorical_cols])

            train_encoded = encoder.transform(
                X_train[categorical_cols]
            )

            test_encoded = encoder.transform(
                X_test[categorical_cols]
            )

            encoded_cols = encoder.get_feature_names_out(
                categorical_cols
            )

            train_encoded_df = pd.DataFrame(
                train_encoded,
                columns=encoded_cols,
                index=X_train.index
            )

            test_encoded_df = pd.DataFrame(
                test_encoded,
                columns=encoded_cols,
                index=X_test.index
            )

            X_train = X_train.drop(
                columns=categorical_cols
            )

            X_test = X_test.drop(
                columns=categorical_cols
            )

            X_train = pd.concat(
                [X_train, train_encoded_df],
                axis=1
            )

            X_test = pd.concat(
                [X_test, test_encoded_df],
                axis=1
            )

            # Save encoder
            joblib.dump(encoder, self.encoder_path)

            logger.info("Encoding completed")

            return (
                X_train,
                X_test,
                y_train,
                y_test
            )

        except Exception as e:
            raise CustomException(str(e), sys)

    # ------------------------------------------------
    # MAIN PROCESS
    # ------------------------------------------------
    def process(self, train_df, test_df):

        try:

            logger.info(
                "Feature Engineering Started"
            )

            train_df = self.clean_data(train_df)
            test_df = self.clean_data(test_df)

            # -----------------------------------------
            # LOG TARGET
            # -----------------------------------------
            if self.config["training"]["log_target"]:

                train_df["Price_log"] = np.log1p(
                    train_df["Price"]
                )

                test_df["Price_log"] = np.log1p(
                    test_df["Price"]
                )

                self.target_column = "Price_log"

            else:

                self.target_column = "Price"

            # -----------------------------------------
            # SPLIT X & y
            # -----------------------------------------
            y_train = train_df[self.target_column]
            y_test = test_df[self.target_column]

            X_train = train_df.drop(
                columns=["Price", "Price_log"],
                errors="ignore"
            )

            X_test = test_df.drop(
                columns=["Price", "Price_log"],
                errors="ignore"
            )

            # -----------------------------------------
            # ENCODE
            # -----------------------------------------
            X_train, X_test, y_train, y_test = (
                self.encode(
                    X_train,
                    X_test,
                    y_train,
                    y_test
                )
            )

            # -----------------------------------------
            # SAVE
            # -----------------------------------------
            X_train.to_csv(
                self.train_processed_path,
                index=False
            )

            X_test.to_csv(
                self.test_processed_path,
                index=False
            )

            logger.info(
                "Feature Engineering Completed"
            )

            return (
                X_train,
                X_test,
                y_train,
                y_test
            )

        except Exception as e:
            raise CustomException(str(e), sys)