# Plotting Wrapper for Seaborn / MPL plots
def tick_adjust(plotter, keep_ind, rotation):
    plot = plotter
    for ind, label in enumerate(plot.get_xticklabels()):
        if ind % keep_ind == 0:
            label.set_visible(True)
        else:
            label.set_visible(False)

    plt.xticks(rotation=rotation)
