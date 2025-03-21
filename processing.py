import pandas as pd

# Read the data into a DataFrame
half_1 = pd.read_csv("raw data/aapl_2016_2020.csv", low_memory=False)
half_2 = pd.read_csv("raw data/aapl_2021_2023.csv", low_memory=False)
df = pd.concat([half_1, half_2], ignore_index=True)
df.columns = df.columns.str.strip()
print(df.columns)

# Convert Unix timestamps to datetime
df['[QUOTE_DATETIME]'] = pd.to_datetime(df['[QUOTE_UNIXTIME]'], unit='s')
df['[EXPIRE_DATETIME]'] = pd.to_datetime(df['[EXPIRE_UNIX]'], unit='s')

# Convert columns that should be numeric
numeric_cols = ['[QUOTE_TIME_HOURS]', '[UNDERLYING_LAST]', '[DTE]', '[C_DELTA]', '[C_GAMMA]', '[C_VEGA]',
                '[C_THETA]', '[C_RHO]', '[C_IV]', '[C_VOLUME]', '[C_LAST]', '[C_BID]', '[C_ASK]', '[STRIKE]',
                '[P_BID]', '[P_ASK]', '[P_LAST]', '[P_DELTA]', '[P_GAMMA]', '[P_VEGA]', '[P_THETA]', '[P_RHO]',
                '[P_IV]', '[P_VOLUME]', '[STRIKE_DISTANCE]', '[STRIKE_DISTANCE_PCT]']
df[numeric_cols] = df[numeric_cols].apply(lambda col: pd.to_numeric(col, errors='coerce'))

# Parse call and put size columns into bid and ask sizes
def parse_size(size_str):
    try:
        bid_size, ask_size = size_str.split('x')
        return int(bid_size.strip()), int(ask_size.strip())
    except:
        return None, None

df[['[C_BID_SIZE]', '[C_ASK_SIZE]']] = df['[C_SIZE]'].apply(lambda x: pd.Series(parse_size(x)))
df[['[P_BID_SIZE]', '[P_ASK_SIZE]']] = df['[P_SIZE]'].apply(lambda x: pd.Series(parse_size(x)))

# Calculate equilibrium prices
df['[CALL_EQUI_PRICE]'] = (df['[C_BID]'] + df['[C_ASK]']) / 2
df['[PUT_EQUI_PRICE]'] = (df['[P_BID]'] + df['[P_ASK]']) / 2

cols_to_keep = ['[UNDERLYING_LAST]', '[DTE]', '[STRIKE]', 
                '[C_BID]', '[C_ASK]', '[CALL_EQUI_PRICE]', 
                '[P_BID]', '[P_ASK]', '[PUT_EQUI_PRICE]']
df_reduced = df[cols_to_keep].copy()
df_reduced.to_csv("processed_data.csv", index=False)