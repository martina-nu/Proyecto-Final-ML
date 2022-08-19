### Cosas que agregaría al explore:

# histogramas variables numéricas #
df_interim_p.hist()
plt.show()
df_interim_z.hist()
plt.show()

# gráfico de lineas (P vs Z) con x = tiempo (semana o mes), y = cantidad de tweets que los mencionan #
# hay que crear un data frame con la unidad de tiempo en la fila, una columna que identifique P o Z, y la variable a graficar
sns.lineplot(data=df_plot, x = 'hour', y = 'rate', hue = 'source', markers = True, style = 'source', dashes = False)
plt.show()

# mostrar texto original del tweet y usuario, al mostrar los más frecuentes, o más retweeteados #

# tweets que mencionen a ambos, están en los 2 datasets? en ese caso armar un tercero con esos tweets

# yo sacaría estas palabras: vladimir, putin, volodymyr, zelensky, russia, russian, ukraine, ukranian, u

# csv con palabras y sentimiento asociado #
# URL: http://saifmohammad.com/WebPages/lexicons.html  
nrc = pd.read_csv('../data/raw/NRC.csv', names=['word','sentiment','polarity'])
nrc = nrc.query('polarity == 1')

# partir texto en palabras, se asocia cada palabra a un sentimiento
df_word_split = (df
                 .drop(['text', 'created_at', 'retweet_count', 'favorite_count'], axis = 1)
                 .assign(text = df['text_clean'].str.split())).explode('text').drop('text_clean', axis = 1).rename(columns = {'text':'word'})
df_word_split

df_word_split.shape # ver cuantas palabras hay en c/u

# inner join para traer más info, nrc contiene la palabra y su sentimiento
df_word_split.merge(nrc[['word', 'sentiment']], on = 'word', how = 'inner')

# data frame con frecuencia de cada sentimiento #
df_sent = df_word_split.\
    merge(nrc[['word', 'sentiment']], on = 'word', how = 'inner').\
    groupby(['source', 'sentiment']).agg(count = ('sentiment', 'count')).\
    reset_index().pivot_table(index = ['sentiment'], columns = ['source'], values = 'count').\
    reset_index().\
    rename(columns = {'Twitter for Android': 'Android', 'Twitter for iPhone': 'iPhone'})
df_sent

# frecuencias relativas, odds ratio
df_odd_ratio = df_sent.\
              assign(odd_ratio = (df_sent['Android']/(df_sent['Android'].sum()-df_sent['Android']))/(df_sent['iPhone']/(df_sent['iPhone'].sum()-df_sent['iPhone'])))
df_odd_ratio['log_or'] = np.log(df_odd_ratio['odd_ratio'])

# creamos intervalos de confianza
df_odd_ratio['se'] = np.sqrt(1/df_odd_ratio['Android'] + 1/(df_odd_ratio['Android'].sum()-df_odd_ratio['Android'])+1/df_odd_ratio['iPhone']+1/(df_odd_ratio['iPhone'].sum()-df_odd_ratio['iPhone']))
df_odd_ratio['conf_low'] = df_odd_ratio['log_or'] - norm.ppf(0.975)*df_odd_ratio['se']
df_odd_ratio['conf_high'] = df_odd_ratio['log_or'] + norm.ppf(0.975)*df_odd_ratio['se']
df_odd_ratio.sort_values(by = 'log_or', ascending = False)

# graficar intervalos de confianza para el sentimiento
df_odd_ratio = df_odd_ratio.sort_values(by = 'log_or', ascending = True)
plt.errorbar(df_odd_ratio['log_or'], df_odd_ratio['sentiment'], marker = 's', xerr = ((df_odd_ratio.log_or-df_odd_ratio.conf_low),(df_odd_ratio.conf_high-df_odd_ratio.log_or)))
plt.show()

# si queremos crear un clasificador hay que crear la variable, ej sentimientos negativos o positivos, ref clase 29

# app: traer tweets que los mencionen y clasificarlos?