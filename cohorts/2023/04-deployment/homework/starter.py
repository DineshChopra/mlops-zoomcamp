#!/usr/bin/env python
# coding: utf-8
import sys
import pickle
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error


def get_input_url(year, month):
    input_file = f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet'
    return input_file

categorical = ['PULocationID', 'DOLocationID']
def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

def load_model():
    with open('model.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)
    return dv, model

def apply_model(df):
    dicts = df[categorical].to_dict(orient='records')
    dv, model = load_model()
    print('model : ', model)
    print('dv : ', dv)
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)
    return y_pred

def get_matrix(y_val, y_pred):
    rmse = mean_squared_error(y_val, y_pred, squared=False)
    mae = mean_absolute_error(y_val, y_pred)
    return rmse, mae



def write_prediction(df, y_pred, year, month):
    output_file = f'{year:04d}-{month:02d}.parquet'
    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
    df_result = pd.DataFrame()
    df_result['ride_id'] = df['ride_id']
    df_result['predicted_duration'] = y_pred
    
    df_result.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False
    )

def run():
    year = int(sys.argv[1]) # year = 2022
    print("year --- ", year )
    month = int(sys.argv[2]) # month = 2
    print("month --- ", month )
    print("run method is called ----")
    input_file = get_input_url(year, month)
    print('input file: ', input_file)
    df = read_data(input_file)
    y_pred = apply_model(df)
    print('prediction -- ', len(y_pred))

    y_val = df.duration.values
    rmse, mae = get_matrix(y_val, y_pred)
    print('rmse -- ', rmse)
    print('mae -- ', mae)
    write_prediction(df, y_pred, year, month)


if __name__ == '__main__':
    run()
