import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=pd.read_csv('C:/Users/Isabela Amorim/Downloads/ecommerce_preparados.csv')
pd.set_option('display.width', None)


df.drop_duplicates()
df.fillna({'Desconto': 0}, inplace=True)
df.fillna({'Gênero':'Não identificado'}, inplace=True)
print('Tipos:', df.dtypes)

#Preparação de dados para gráfico de pizza
df['Gênero']=df['Gênero'].replace({'Bebês':'Infantil','Meninas':'Feminino','Meninos':'Masculino','Não identificado':'Sem gênero',
'Sem gênero infantil':'Infantil','Mulher':'Feminino','short menina verao look mulher':'Feminino','roupa para gordinha pluss P ao 52':
'Feminino', 'Unissex':'Sem gênero', 'menino':'Masculino','bermuda feminina brilho Blogueira':'Feminino'})
x = df['Gênero'].value_counts().index
y = df['Gênero'].value_counts().values
plt.figure(figsize=(8,4))
plt.pie(y,labels=x,autopct='%.1f%%', startangle=90)
plt.title('Peças vendidas por Gênero')
plt.show()

#Histograma
plt.hist(df['Nota'])
plt.title('Nota dos Usuários')
plt.xlabel('Notas')
plt.ylabel('Número de avaliações')
plt.show()

#Gráfico de Dispersão
plt.scatter(df['Nota'],df['Gênero'])
plt.title('Dispersão - Nota e Gênero')
plt.xlabel('Nota')
plt.show()

#Heatmap
df['Marca'] = df['Marca'].str.title()
df_corr=df[['Marca_Freq','Qtd_Vendidos_Cod','Material_Freq','Preço_MinMax','Desconto_MinMax']].corr()
plt.figure(figsize=(8,4))
sns.heatmap(df_corr,annot=True,fmt=".2f")
plt.title('Mapa de Calor da Correlação entre Variáveis')
plt.show()

#Gráfico de Barras
plt.figure(figsize=(10,6))
df['Nota'].value_counts().plot(kind='bar', color='#cf040b')
plt.title('Notas das avaliações')
plt.show()

#Gráfico de Densidade
plt.figure(figsize=(8, 6))
sns.kdeplot(data=df, x='Preço', hue='Gênero', shade=True)
plt.title("Gráfico de Densidade de Preço por Gênero", fontsize=16)
plt.xlabel("Preço", fontsize=12)
plt.ylabel("Densidade", fontsize=12)
plt.grid(True)
plt.show()

#Gráfico de Regressão

x = 'Preço'          
y = 'Nota'           

# Criando o gráfico de regressão
plt.figure(figsize=(8, 6))
sns.regplot(x=df[x], y=df[y], scatter_kws={'alpha': 0.6}, line_kws={'color': 'red'})
plt.title(f"Gráfico de Regressão - {y} vs {x}", fontsize=16)
plt.xlabel(x, fontsize=12)
plt.ylabel(y, fontsize=12)
plt.grid(True)
plt.show()






