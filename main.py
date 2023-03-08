import pandas as pd
import matplotlib.pyplot as plt
import config


def plot_graph(file_type, file_path, plot_type, x_label, y_label, column_name, labels=None, x_col_name=None, y_col_name=None):
    if file_type == "local":
        try:
            data = pd.read_csv(file_path)
        except Exception as e:
            print(e)
            return
    elif file_type == "online":
        try:
            data = pd.read_csv(file_path)
        except Exception as e:
            print(e)
            return
    else:
        print("Invalid file type")
        return

    if x_col_name and y_col_name:
        x = data[x_col_name]
        y = data[y_col_name]
    else:
        try:
            x = data[column_name]
            y = data.drop(column_name, axis=1)
        except Exception as e:
            print(e)
            return

    if plot_type == config.PLOT_TYPES[0]:
        if labels:
            plt.pie(x, labels=labels)
        else:
            plt.pie(x)
        plt.title(y_label)
    elif plot_type == config.PLOT_TYPES[1]:
        plt.plot(x, y)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(y_label)
    elif plot_type == config.PLOT_TYPES[2]:
        plt.scatter(x, y)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(y_label)

    plt.show()
