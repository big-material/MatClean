import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
from sklearn.impute import KNNImputer


def filled_df_except_miss_col(df_with_null: pd.DataFrame, missing_col: str) -> pd.DataFrame:
    """
    Fill the missing values in the dataframe except the missing column
    填充缺失值，但是不填充miss_col列
    :param df_with_null: 存在缺失值的dataframe
    :param missing_col: 当前需要填充的列
    :return:
    """
    knn_impute = KNNImputer()
    df_filled = knn_impute.fit_transform(df_with_null.copy())
    df_filled_except_miss_col = pd.DataFrame(df_filled, columns=df_with_null.columns)
    df_filled_except_miss_col[missing_col] = df_with_null[missing_col]
    return df_filled_except_miss_col


def fill_with_model(df_with_null: pd.DataFrame, missing_col: str, model: BaseEstimator) -> pd.DataFrame:
    """
    Fill the missing values in missing_col column of the dataframe with model
    使用模型填充当前missing_col列的缺失值
    :param df_with_null: the dataframe with missing values
    :param missing_col: the column with missing values
    :param model: the model to fill the missing values
    :return: the dataframe with missing values filled
    """
    df_filled_except_miss_col = filled_df_except_miss_col(df_with_null, missing_col)
    train_df = df_filled_except_miss_col.dropna()
    X_train = train_df.drop(missing_col, axis=1)
    y_train = train_df[missing_col]
    model.fit(X_train, y_train)
    miss_index = df_with_null[df_with_null[missing_col].isnull()].index
    predict_X = df_filled_except_miss_col.loc[miss_index].drop(missing_col, axis=1)
    predict_y = model.predict(predict_X)
    df_filled = df_with_null.copy()
    df_filled.loc[miss_index, missing_col] = predict_y
    return df_filled


def fill_with_extratrees(df_with_null, missing_col):
    """
    Fill the missing values in missing_col column of the dataframe with ExtraTreesRegressor
    :param df_with_null: the dataframe with missing values
    :param missing_col: the column with missing values
    :return:
    """
    et = ExtraTreesRegressor()
    return fill_with_model(df_with_null, missing_col, et)


class MatImputer(BaseEstimator, TransformerMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._model = ExtraTreesRegressor()

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Fill the missing values in the dataframe df
        :param df: the dataframe with missing values
        :return: the dataframe with missing values filled
        """
        missing_ratio = df.isnull().sum() / df.shape[0]
        cols = missing_ratio.sort_values().index.tolist()
        cols = [col for col in cols if missing_ratio[col] > 0]
        for col in cols:
            df_col_filled = fill_with_extratrees(df, col)
            df[col] = df_col_filled[col]
        return df


def outlier_remove(df: pd.DataFrame, target_col: str, threshold: float = 0.1) -> pd.DataFrame:
    """
    Remove the outliers in the dataframe    :param df:  the dataframe
    :param target_col: the target column
    :param threshold: the threshold to remove the outliers
    :return: the dataframe without outliers
    """
    n_original = df.shape[0]
    n_keep = int(n_original * (1 - threshold))
    while df.shape[0] > n_keep:
        model = RandomForestRegressor()
        X = df.drop(target_col, axis=1)
        y = df[target_col]
        model.fit(X, y)
        pred_y = model.predict(X)
        df["residual"] = y - pred_y
        std = df["residual"].std()
        df["std_residual"] = df["residual"] / std
        hat_matrix = np.matmul(np.matmul(X.values, np.linalg.inv(np.matmul(X.values.T, X.values))), X.values.T)
        leverage = np.diagonal(hat_matrix)
        df["leverage"] = leverage
        outliers = df[(abs(df["std_residual"]) >= 1.7) | ((abs(df["std_residual"]) < 1.7) & (df["leverage"] > 0.2))]
        df = df.drop(outliers.index)
        df = df.drop(["residual", "std_residual", "leverage"], axis=1)
    return df
