```json
{
    "agents/supply_chain_agent.py": {
        "content": "
import logging
from typing import Dict, List
from crewai import StateGraph
from lightweight_mmm import MemoryManagement

class SupplyChainAgent:
    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initialize the SupplyChainAgent.

        Args:
        - non_stationary_drift_index (float): The index of non-stationary drift in the supply chain.
        - stochastic_regime_switch (bool): Whether to switch to a stochastic regime.

        Returns:
        - None
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch
        self.memory_management = MemoryManagement()
        self.state_graph = StateGraph()
        self.logger = logging.getLogger(__name__)

    def optimize_supply_chain(self, demand_forecast: List[float]) -> Dict[str, float]:
        """
        Optimize the supply chain based on the demand forecast.

        Args:
        - demand_forecast (List[float]): The forecasted demand.

        Returns:
        - Dict[str, float]: The optimized supply chain parameters.

        Raises:
        - Exception: If the optimization fails.
        """
        try:
            self.logger.info('Optimizing supply chain...')
            optimized_parameters = self.state_graph.optimize(demand_forecast, self.non_stationary_drift_index, self.stochastic_regime_switch)
            self.logger.info('Optimization successful.')
            return optimized_parameters
        except Exception as e:
            self.logger.error(f'Optimization failed: {str(e)}')
            raise

    def manage_memory(self, data: Dict[str, float]) -> None:
        """
        Manage the memory of the agent.

        Args:
        - data (Dict[str, float]): The data to store in memory.

        Returns:
        - None

        Raises:
        - Exception: If the memory management fails.
        """
        try:
            self.logger.info('Managing memory...')
            self.memory_management.store(data)
            self.logger.info('Memory management successful.')
        except Exception as e:
            self.logger.error(f'Memory management failed: {str(e)}')
            raise

if __name__ == '__main__':
    # Simulation of the 'Rocket Science' problem
    agent = SupplyChainAgent(non_stationary_drift_index=0.5, stochastic_regime_switch=True)
    demand_forecast = [100.0, 120.0, 150.0]
    optimized_parameters = agent.optimize_supply_chain(demand_forecast)
    print(optimized_parameters)
    data = {'parameter1': 10.0, 'parameter2': 20.0}
    agent.manage_memory(data)
",
        "commit_message": "feat: implement specialized supply_chain_agent logic"
    }
}
```