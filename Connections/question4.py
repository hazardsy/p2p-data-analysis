"""
    addition
"""
import random

from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram


class PeerQ4(Peer):
    def send_data_to_backend(self):
        """
        Question 4: implement this method
        """
        return sum(self.peer_pool.values()) / len(self.peer_pool.values())


class SimulationQ4(Simulation):
    def generate_network(self):
        self.network = [PeerQ4() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
        Question 4: implement this method
        """
        connection_durations = [peer.send_data_to_backend() for peer in self.network]

        return compute_histogram_bins(connection_durations, BINS)


if __name__ == "__main__":

    s = SimulationQ4(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()
