import talib as ta

def add_indicators(df):
    df['RSI'] = ta.RSI(df['Close'])
    df['MFI'] = ta.MFI(df['High'], df['Low'], df['Close'], df['VolumeFrom'])
    df['ADX'] = ta.ADX(df['High'], df['Low'], df['Close'])

    macd, macdsignal, macdhist = ta.MACD(df['Close'])
    df['macd'] = macd
    df['macd_signal'] = macdsignal
    df['macd_hist'] = macdhist

    aroondown, aroonup = ta.AROON(df['High'], df['Low'])
    df['aroon_up'] = aroonup
    df['aroon_down'] = aroondown

    df['trix'] = ta.TRIX(df['Close'])

    df['uo'] = ta.ULTOSC(df['High'], df['Low'], df['Close'])

    upperband, middleband, lowerband = ta.BBANDS(df['Close'])

    df['wbb_upper'] = upperband
    df['wbb_lower'] = lowerband
    df['wbb_mid'] = middleband

    df['chaikin_line'] = ta.AD(df['High'], df['Low'], df['Close'], df['VolumeFrom'])
    df['chaikin_osc'] = ta.ADOSC(df['High'], df['Low'], df['Close'], df['VolumeFrom'])
    df['obv'] = ta.OBV(df['Close'], df['VolumeFrom'])

    df.fillna(method='bfill', inplace=True)

    return df