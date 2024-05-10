from matplotlib import pyplot as plt

def generate_pie_chart():
    labels = ['A','B','C']
    values = [200,50,100]

    fig, ax = plt.subplots()
    print(f'ax {ax}')

    ax.pie(values, labels=labels)
    plt.savefig('imgs/pie.png')

    plt.close()