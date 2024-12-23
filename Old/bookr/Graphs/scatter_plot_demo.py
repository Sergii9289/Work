from plotly.offline import plot
import plotly.graph_objs as graphs


def generate_scatter_plot(x_axis, y_axis):
    """Generate a scatter plot for the provided x and
    y-axis values."""
    figure = graphs.Figure()  # create an object to act as a container for the graph
    scatter = graphs.Scatter(x=x_axis, y=y_axis)  # create a new Scatter object
    figure.add_trace(scatter)  # add it to the graph’s Figure container
    return plot(figure, output_type='file')  # generate the HTML to render this plot inside a web page


def generate_html(plot_html):
    """Generate an HTML page for the provided plot."""
    html_content = f"<html><head><title>Plot Demo</title></head><body>{plot_html}</body></html>"
    try:
        with open('plot_demo.html', 'w') as plot_file:
            # открыть для записи, содержимое удаляется, если файла нет, создаётся новый
            plot_file.write(html_content)
    except (IOError, OSError) as file_io_error:
        print(f"Unable to generate plot file. Exception: {file_io_error}")


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    y = [3, 8, 7, 9, 20]
    plo_html = generate_scatter_plot(x, y)
    generate_html(plo_html)
