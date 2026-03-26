```json
{
    "tests/test_supply_chain_agent.py": {
        "content": "
import logging
from typing import Dict, List
from crewai import StateGraph
from boltons import setdefault
from lightweight_mmm import MemoryManager

logging.basicConfig(level=logging.INFO)

class SupplyChainAgent:
    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initialize the SupplyChainAgent.

        Args:
        - non_stationary_drift_index (float): The index of non-stationary drift in the supply chain.
        - stochastic_regime_switch (bool): Whether to enable stochastic regime switch.

        Returns:
        - None
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch
        self.memory_manager = MemoryManager()

    def optimize_supply_chain(self, demand_forecast: List[float]) -> Dict[str, float]:
        """
        Optimize the supply chain based on the demand forecast.

        Args:
        - demand_forecast (List[float]): The forecasted demand.

        Returns:
        - Dict[str, float]: The optimized supply chain parameters.
        """
        try:
            # Create a StateGraph to model the supply chain
            state_graph = StateGraph()
            state_graph.add_node('demand', demand_forecast)
            state_graph.add_node('supply', [0.0] * len(demand_forecast))

            # Use the memory manager to store the state graph
            self.memory_manager.store('state_graph', state_graph)

            # Optimize the supply chain using the state graph
            optimized_parameters = self._optimize_supply_chain(state_graph)

            return optimized_parameters
        except Exception as e:
            logging.error(f'Error optimizing supply chain: {e}')
            return {}

    def _optimize_supply_chain(self, state_graph: StateGraph) -> Dict[str, float]:
        """
        Optimize the supply chain using the state graph.

        Args:
        - state_graph (StateGraph): The state graph modeling the supply chain.

        Returns:
        - Dict[str, float]: The optimized supply chain parameters.
        """
        try:
            # Use the LangGraph StateGraph to optimize the supply chain
            optimized_parameters = state_graph.optimize(self.non_stationary_drift_index, self.stochastic_regime_switch)
            return optimized_parameters
        except Exception as e:
            logging.error(f'Error optimizing supply chain: {e}')
            return {}

def main():
    # Create a SupplyChainAgent
    agent = SupplyChainAgent(non_stationary_drift_index=0.5, stochastic_regime_switch=True)

    # Simulate the 'Rocket Science' problem
    demand_forecast = [10.0, 20.0, 30.0]
    optimized_parameters = agent.optimize_supply_chain(demand_forecast)

    # Print the optimized parameters
    print(optimized_parameters)

if __name__ == '__main__':
    main()
",
        "commit_message": "feat: implement specialized test_supply_chain_agent logic"
    }
}
```