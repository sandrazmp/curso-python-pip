import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A','B','C']
    values = [200,14,120]

    fig, ax = plt.subplots();
    ax.pie(values,labels=labels)
    #plt.show() al ejecuctarse se detiene el proyecto
    plt.savefig('pie.png')
    plt.close()