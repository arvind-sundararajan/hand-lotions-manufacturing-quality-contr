```json
{
    "memory/long_term_memory.py": {
        "content": "
import logging
from typing import Dict, List
from crewai import StateGraph

class LongTermMemory:
    """
    A class used to represent long term memory in the Non-Stationary Stochastic Quality Control Engine.

    Attributes:
    ----------
    non_stationary_drift_index : Dict[str, float]
        a dictionary to store the non-stationary drift index for each lotion type
    stochastic_regime_switch : List[float]
        a list to store the stochastic regime switch probabilities

    Methods:
    -------
    update_non_stationary_drift_index(lotion_type: str, drift_index: float)
        updates the non-stationary drift index for a given lotion type
    update_stochastic_regime_switch(probabilities: List[float])
        updates the stochastic regime switch probabilities
    get_non_stationary_drift_index(lotion_type: str) -> float
        returns the non-stationary drift index for a given lotion type
    get_stochastic_regime_switch() -> List[float]
        returns the stochastic regime switch probabilities
    """

    def __init__(self):
        """
        Initializes the LongTermMemory class.

        Initializes the non_stationary_drift_index dictionary and the stochastic_regime_switch list.
        """
        self.non_stationary_drift_index: Dict[str, float] = {}
        self.stochastic_regime_switch: List[float] = []
        self.state_graph = StateGraph()

    def update_non_stationary_drift_index(self, lotion_type: str, drift_index: float) -> None:
        """
        Updates the non-stationary drift index for a given lotion type.

        Args:
        ----
        lotion_type (str): the type of lotion
        drift_index (float): the non-stationary drift index

        Returns:
        -------
        None
        """
        try:
            logging.info(f'Updating non-stationary drift index for {lotion_type}')
            self.non_stationary_drift_index[lotion_type] = drift_index
            self.state_graph.add_node(lotion_type, drift_index)
        except Exception as e:
            logging.error(f'Error updating non-stationary drift index: {e}')

    def update_stochastic_regime_switch(self, probabilities: List[float]) -> None:
        """
        Updates the stochastic regime switch probabilities.

        Args:
        ----
        probabilities (List[float]): the stochastic regime switch probabilities

        Returns:
        -------
        None
        """
        try:
            logging.info('Updating stochastic regime switch probabilities')
            self.stochastic_regime_switch = probabilities
            self.state_graph.add_edge('stochastic_regime_switch', probabilities)
        except Exception as e:
            logging.error(f'Error updating stochastic regime switch probabilities: {e}')

    def get_non_stationary_drift_index(self, lotion_type: str) -> float:
        """
        Returns the non-stationary drift index for a given lotion type.

        Args:
        ----
        lotion_type (str): the type of lotion

        Returns:
        -------
        float: the non-stationary drift index
        """
        try:
            logging.info(f'Getting non-stationary drift index for {lotion_type}')
            return self.non_stationary_drift_index[lotion_type]
        except Exception as e:
            logging.error(f'Error getting non-stationary drift index: {e}')
            return None

    def get_stochastic_regime_switch(self) -> List[float]:
        """
        Returns the stochastic regime switch probabilities.

        Returns:
        -------
        List[float]: the stochastic regime switch probabilities
        """
        try:
            logging.info('Getting stochastic regime switch probabilities')
            return self.stochastic_regime_switch
        except Exception as e:
            logging.error(f'Error getting stochastic regime switch probabilities: {e}')
            return None

if __name__ == '__main__':
    # Create a LongTermMemory instance
    long_term_memory = LongTermMemory()

    # Update non-stationary drift index for lotion type 'A'
    long_term_memory.update_non_stationary_drift_index('A', 0.5)

    # Update stochastic regime switch probabilities
    long_term_memory.update_stochastic_regime_switch([0.2, 0.3, 0.5])

    # Get non-stationary drift index for lotion type 'A'
    print(long_term_memory.get_non_stationary_drift_index('A'))

    # Get stochastic regime switch probabilities
    print(long_term_memory.get_stochastic_regime_switch())
",
        "commit_message": "feat: implement specialized long_term_memory logic"
    }
}
```