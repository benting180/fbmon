def send_telegram(message):
    import requests
    TOKEN = '6897025438:AAF3FwXvgxi0BYuQSggTgZry_mwWBNuWH2g'
    CHAT_ID = 427588354

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"

    response = requests.get(url).json()
    return 

def filter(df):
    stadiums = ['瑞和街', '牛頭角', '彩榮道', '牛池灣', '九龍灣', '振華道', '調景嶺']
    df['user'] = df['user'].apply(lambda x: x['name'] if 'name' in x else None)
    include_stadiums_condition = df['text'].apply(lambda x: any(word in x for word in stadiums))
    level_3 = '初中'
    level_4 = '初高'
    exclude_level_3_condition = ~df['text'].str.contains(level_3)
    exclude_level_4_condition = ~df['text'].str.contains(level_4)
    filter_condition = (include_stadiums_condition & exclude_level_3_condition & exclude_level_4_condition)
    df_filtered = df[filter_condition]
    df_filtered = df_filtered.drop_duplicates(subset=['text'])
    return df_filtered

def df2msg(df):
    msg = []
    for index, row in df.iterrows():
        msg.append("\n場主: " + row['user'] + "\n")
        msg.append(row['text'])
        msg.append("\n\n")
        msg.append("------------------------------")
        msg.append("\n\n")
    msg = "".join(msg)
    return msg
    