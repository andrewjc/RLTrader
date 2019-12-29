import talib as ta

def add_indicators(df):
    df['RSI'] = ta.RSI(df['close'])
    df['MFI'] = ta.MFI(df['high'], df['low'], df['close'], df['volume'])
    df['ADX'] = ta.ADX(df['high'], df['low'], df['close'])

    macd, macdsignal, macdhist = ta.MACD(df['close'])
    df['macd'] = macd
    df['macd_signal'] = macdsignal
    df['macd_hist'] = macdhist

    aroondown, aroonup = ta.AROON(df['high'], df['low'])
    df['aroon_up'] = aroonup
    df['aroon_down'] = aroondown

    df['trix'] = ta.TRIX(df['close'])

    df['uo'] = ta.ULTOSC(df['high'], df['low'], df['close'])

    upperband, middleband, lowerband = ta.BBANDS(df['close'])

    df['wbb_upper'] = upperband
    df['wbb_lower'] = lowerband
    df['wbb_mid'] = middleband

    df['chaikin_line'] = ta.AD(df['high'], df['low'], df['close'], df['volume'])
    df['chaikin_osc'] = ta.ADOSC(df['high'], df['low'], df['close'], df['volume'])
    df['obv'] = ta.OBV(df['close'], df['volume'])

    df.fillna(method='bfill', inplace=True)

    return df