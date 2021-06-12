from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram


class PeerQ2(Peer):
    def send_data_to_backend(self):
        """
        Question 2:
        This method should return an _array_ of the peer's
        connection durations.
        """
        return list(self.peer_pool.values())


class SimulationQ2(Simulation):
    def generate_network(self):
        self.network = [PeerQ2() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
        Question 2:
        This method should do all necessary processing to return
        the connection durations histogram bins counts.
        Don't call `plot_histogram` in this method, we just want
        to compute the histogram bins counts!
        """
        connection_durations = []
        for peer in self.network:
            connection_durations += peer.send_data_to_backend()

        # Both peers in a connection know about the connection duration which means we count them both times
        # Given the precision on connection times in this exercise (14 digits), it is likely safe to assume two connections will never have the exact same connection duration
        # Thus the use of a set
        return compute_histogram_bins(set(connection_durations), BINS)


if __name__ == "__main__":

    s = SimulationQ2(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()
