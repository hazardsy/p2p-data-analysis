### Questions

#### Question 1

Fill in the two functions `compute_histogram_bins` and `plot_histogram` in `histogram.py`. As an example, we would like to be able to plot something similar to `histogram_example.png` as a minimum result.

#### Question 2

Go to the file `question2.py`:
1. fill in `send_data_to_backend` so that it returns an _array_ of the peer's connection durations.
2. fill in `process_backend_data` which must do all necessary processing to return the connection durations histogram bins counts. **Don't call `plot_histogram` in this method, we just want to compute the histogram bins counts**.

#### Question 3

With peers sending such datastructure and our _backend_ server making such operations, we retrieve exactly **all** the connection durations on the network at the moment of the snapshot and we are able to plot the _exact distribution_ of the connection durations.
`question2.py` main has several simulations with increasing numbers of peers and peer pool size. Run the simulations with your implementation. What do you see? Can you explain the limitations of the implementations of question 2 taking into account that a _real_ peer network can have _millions_ of peers? (answer below in this file)
>> Processing the backend takes an increasing amount of time when the number of connections increases (i.e. either the number of peers or the number of connections by peers increases). The issue lies with the fact that the number of connections is multiplicative with the number of peers and the number of connections by peers. It means that looking at each connection individually is not sustainable when the network grows. The solution I propose is to aggregate connection durations at the peer-level in a way that makes computation a lot more effective e.g. average, 95 percentile, median, etc. The choice of the aggregation function depends on the desired outcome i.e. is the goal to increase the average connection duration, to spot outliers (peers with unusually long or short duration times) or something else entirely ?

#### Question 4

Go to the file `question4.py`:
Propose new implementations of `send_data_to_backend` and `process_backend_data` that can deal with millions of peers _and_ still provide a good representation of the _distribution_ of the connection duration. You are free to add any written comments, add pictures etc. to enhance your answer.
>> I chose to implement the use of an average function at peer-level because it feels relevant to identify whether our network works thanks to a large number of "short duration" peers or rather thanks to a small number of "long duration" peers. In real life, I expect that it wouldn't be as clear cut and most likely would have peers at every end of the histogram.