#pip install matplotlib
import matplotlib.pyplot as plt #deve de instalado antes de roda o codigo, na area que o arquivo vai esta e vai dá muitos error
#exemplo01
'''fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 150, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruta cor e algum número que eu não sei')
ax.legend(title='Fruit color')

plt.show()'''
#exemplo02_ funcionalidade do eixo x e y
'''x=[1,2,3]
y=[2,4,6]
plt.plot(x,y)
plt.show()#exibe o gráfico'''



import math  #proprio do pytron

eixo_x=[]
eixo_y=[]
for x in range(-4,5):
    eixo_x.append(x)
    y= math.pow(x,2) #outra formula de elevar a um valor
    eixo_y.append(y)
plt.plot(eixo_x,eixo_y, linestyle=(5, (10, 3)), color='greenyellow', linewidth=5, label= 'valor') #linestyle= , muda o estilo da linha para essa biblioteca, o estilo estão cartalogado no site,
# o mesmo vale para o color= e o linewidth= muda a grossura da linha, label= adiciona um titulo
plt.xlabel('Variação de x', color= 'gold', loc='left') #color= tambem funciona para cá e loc= muda a posição da legenda
plt.ylabel('Variação de y', color= 'silver', fontsize=20) #coloca um titulo do eixo #fontsize= muda o tamanho da fonte

plt.title('exemplo', loc='center') #coloca um titulo no gráfico

plt.legend(loc= 'upper center') #adiciona uma legenda do gráfico
plt.grid() #coloca grade no grafico
#plt.savefig(fname= 'exp.', dpi=1080) #salva a imagem #fname= dá um titulo a imagem e dpi= alterar a qualidade
plt.show()