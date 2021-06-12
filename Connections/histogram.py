from random import randint
import matplotlib.pyplot as plt


def compute_histogram_bins(data=[], bins=[]):
    """
    Question 1:
    Given:
        - data, a list of numbers you want to plot a histogram from,
        - bins, a list of sorted numbers that represents your histogram
          bin thresdholds,
    return a data structure that can be used as input for plot_histogram
    to plot a histogram of data with buckets bins.
    You are not allowed to use external libraries other than those already
    imported.
    """
    bins_count = []
    bins_name = []
    for i, bin_start in enumerate(bins[:-1]):
        bin_end = bins[i + 1]
        bins_name.append(f"{bin_start}-{bin_end}")
        bins_count.append(len([x for x in data if bin_start <= x < bin_end]))

    # Deal with the "100-+" bin
    bins_name.append(f"{bins[-1]}-+")
    bins_count.append(len([x for x in data if x >= bins[-1]]))

    return {"bins_name": bins_name, "bins_count": bins_count}


def plot_histogram(bins_count):
    """
    Question 1:
    Implement this function that plots a histogram from the data
    structure you returned from compute_histogram_bins. We recommend using
    matplotlib.pyplot but you are free to use whatever package you prefer.
    You are also free to provide any graphical representation enhancements
    to your output.
    """
    counts, names = bins_count.get("bins_count"), bins_count.get("bins_name")
    plt.bar(range(len(counts)), counts, 0.9, tick_label=names)
    plt.title("Some kind of distribution")
    plt.ylabel("Count")
    plt.xlabel("Bins")
    plt.savefig("histogram_result.png")


if __name__ == "__main__":
    # EXAMPLE:

    # inputs
    data = [randint(0, 100) for x in range(200)]
    bins = [0, 10, 20, 30, 40, 70, 100]

    # compute the bins count
    histogram_bins = compute_histogram_bins(data=data, bins=bins)

    # plot the histogram given the bins count above
    plot_histogram(histogram_bins)
