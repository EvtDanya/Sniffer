import matplotlib.pyplot as plt

def draw_statistics(data, xlabel, ylabel, title, position):
    '''
    Draw statistics with the given parameters
    '''
    labels = data.keys()
    values = data.values()

    ax = plt.subplot(position)
    ax.bar(labels, values)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

def show_statistics():
    '''
    Displays a window with statistics graphs
    '''
    ip_statistics = {
        'TCP': 100,
        'UDP': 50,
        'ICMP': 20
    }

    port_statistics = {
        'HTTP': 80,
        'SSH': 22,
        'FTP': 21
    }

    plt.figure(figsize=(10, 6)) 

    draw_statistics(
        ip_statistics,
        'Протокол',
        'Количество пакетов',
        'Статистика по айпи',
        211
    )
    
    draw_statistics(
        port_statistics,
        'Порт',
        'Количество пакетов',
        'Статистика по портам',
        212
    )

    plt.tight_layout()  
    plt.show()

show_statistics()